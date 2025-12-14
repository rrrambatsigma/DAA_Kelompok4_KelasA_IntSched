# ==========================================================
# run.py
# Experiment Runner (LOCKED JSON Instances)
# Greedy EFT vs Greedy Profit Density
# ==========================================================

import json
import argparse
import time
from pathlib import Path
import pandas as pd

# ==========================================================
# GREEDY ALGORITHMS (IDENTIK NOTEBOOK)
# ==========================================================

def run_algo_eft(data: pd.DataFrame):
    t0 = time.perf_counter()

    sorted_data = data.sort_values(
        by=["finish_abs", "start_abs", "id"],
        kind="mergesort"
    )

    schedule = []
    last_finish = -1

    for _, row in sorted_data.iterrows():
        if row["start_abs"] >= last_finish:
            schedule.append(row)
            last_finish = row["finish_abs"]

    runtime_ms = (time.perf_counter() - t0) * 1000
    return schedule, runtime_ms


def run_algo_density(data: pd.DataFrame):
    t0 = time.perf_counter()

    sorted_data = data.sort_values(
        by=["profit_density", "finish_abs", "id"],
        ascending=[False, True, True],
        kind="mergesort"
    )

    schedule = []
    occupied = []

    for _, row in sorted_data.iterrows():
        s, f = row["start_abs"], row["finish_abs"]
        conflict = False

        for os, of in occupied:
            if s < of and f > os:
                conflict = True
                break

        if not conflict:
            schedule.append(row)
            occupied.append((s, f))

    runtime_ms = (time.perf_counter() - t0) * 1000
    return schedule, runtime_ms


# ==========================================================
# EVALUATOR
# ==========================================================

def evaluate_schedule(schedule):
    total_sks = sum(row["SKS"] for row in schedule)
    return {
        "n_selected": len(schedule),
        "total_sks": total_sks
    }


# ==========================================================
# LOAD JSON INSTANCES
# ==========================================================

def load_instances(json_path: Path):
    with open(json_path, "r", encoding="utf-8") as f:
        content = json.load(f)

    return content["instances"]


# ==========================================================
# MAIN
# ==========================================================

def main():
    parser = argparse.ArgumentParser(
        description="Run Interval Scheduling Experiments from LOCKED JSON Instances"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Path ke file JSON instance (locked_instances.json)"
    )

    parser.add_argument(
        "--algo",
        choices=["EFT", "DENSITY"],
        required=True,
        help="Algoritma yang dijalankan"
    )

    args = parser.parse_args()

    json_path = Path(args.data).resolve()
    if not json_path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {json_path}")

    instances = load_instances(json_path)

    print("\n==============================================")
    print(" INTERVAL SCHEDULING – EXPERIMENT RUNNER")
    print("==============================================")
    print(f"Algorithm : {args.algo}")
    print(f"Instances : {len(instances)}")

    # ======================================================
    # LOOP INSTANCE
    # ======================================================

    for inst in instances:
        df = pd.DataFrame(inst["data"])

        print("\n----------------------------------------------")
        print(f"Instance ID     : {inst['instance_id']}")
        print(f"n (intervals)   : {inst['num_intervals']}")
        print(f"Seed            : {inst['seed']}")

        if args.algo == "EFT":
            schedule, runtime = run_algo_eft(df)
        else:
            schedule, runtime = run_algo_density(df)

        eval_res = evaluate_schedule(schedule)

        print(f"Runtime (ms)    : {runtime:.4f}")
        print(f"Jumlah Kelas    : {eval_res['n_selected']}")
        print(f"Total SKS       : {eval_res['total_sks']}")
        print("Selected IDs    :", [row["id"] for row in schedule])

    print("\n==============================================")
    print(" EXPERIMENT FINISHED")
    print("==============================================")


if __name__ == "__main__":
    main()
