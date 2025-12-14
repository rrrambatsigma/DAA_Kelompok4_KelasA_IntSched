# ==========================================================
# generate_instances.py
# Generate LOCKED experiment instances from notebook logic
# ==========================================================

import pandas as pd
import json
from pathlib import Path

# ==========================================================
# PATH CONFIG
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR.parent / "data" / "normalized_fix_2.csv"
OUTPUT_PATH = BASE_DIR.parent / "data" / "locked_instances.json"

# ==========================================================
# LOAD & PREPROCESS DATA (IDENTIK NOTEBOOK)
# ==========================================================

def load_dataset(path):
    df = pd.read_csv(path)

    df["profit_density"] = df["profit_density"].fillna(0)

    day_map = {
        'Senin': 0,
        'Selasa': 1,
        'Rabu': 2,
        'Kamis': 3,
        'Jumat': 4,
        'Sabtu': 5,
        'Minggu': 6
    }

    def get_minutes(day, time_str):
        if day not in day_map:
            return -1
        h, m, s = map(int, time_str.split(':'))
        return day_map[day] * 24 * 60 + h * 60 + m

    df["start_abs"] = df.apply(
        lambda x: get_minutes(x["Hari"], x["start"]), axis=1
    )
    df["finish_abs"] = df.apply(
        lambda x: get_minutes(x["Hari"], x["finish"]), axis=1
    )

    # ID HARUS SAMA DENGAN NOTEBOOK
    df["id"] = df.index

    return df


# ==========================================================
# GENERATE LOCKED INSTANCES (MENIRU NOTEBOOK)
# ==========================================================

def generate_locked_instances(df):
    sizes_to_test = [10, 20, 30, 40]
    seeds_to_test = [0, 1]

    instances = []

    for n in sizes_to_test:
        for seed in seeds_to_test:
            subset = df.sample(
                n=n,
                random_state=seed
            ).reset_index(drop=True)

            instances.append({
                "instance_id": f"n{n}_seed{seed}",
                "n": n,
                "seed": seed,
                "num_intervals": len(subset),
                "data": subset.to_dict(orient="records")
            })

    return instances


# ==========================================================
# MAIN
# ==========================================================

def main():
    print("Loading dataset...")
    df = load_dataset(DATASET_PATH)

    print("Generating locked instances (NOTEBOOK-CONSISTENT)...")
    instances = generate_locked_instances(df)

    output = {
        "experiment_id": "Greedy_Scheduling_EFT_vs_Density",
        "source_dataset": str(DATASET_PATH),
        "note": "Instances generated using the same random sampling (n, seed) as notebook experiments",
        "num_instances": len(instances),
        "instances": instances
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("==============================================")
    print("LOCKED INSTANCES GENERATED SUCCESSFULLY")
    print(f"Output file : {OUTPUT_PATH}")
    print(f"Total instances : {len(instances)}")
    print("==============================================")


if __name__ == "__main__":
    main()
