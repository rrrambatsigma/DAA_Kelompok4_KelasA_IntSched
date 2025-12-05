import json, argparse, time
from pathlib import Path


# -------------------------------------
# ALGO A: Greedy Earliest Finish Time
# -------------------------------------
def algo_A(instance):
    jobs = sorted(instance["jobs"], key=lambda x: x["finish"])
    result = []
    last_finish = -1

    for job in jobs:
        if job["start"] >= last_finish:
            result.append(job)
            last_finish = job["finish"]

    return result


# -------------------------------------
# ALGO B: Greedy Profit Density
# -------------------------------------
def algo_B(instance):
    jobs = sorted(instance["jobs"],
                  key=lambda x: x["profit"] / (x["finish"] - x["start"]),
                  reverse=True)

    result = []
    active = []

    for job in jobs:
        overlap = False
        for a in active:
            # cek bentrok interval
            if not (job["finish"] <= a["start"] or job["start"] >= a["finish"]):
                overlap = True
                break

        if not overlap:
            result.append(job)
            active.append(job)

    return result


# -------------------------------------
# Evaluator: Total Profit
# -------------------------------------
def evaluate(output):
    return sum(j["profit"] for j in output)


# -------------------------------------
# MAIN EXECUTION
# -------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True,
                        help="Path ke file JSON misalnya: data/interval_dummy.json")
    parser.add_argument("--algo", choices=["A", "B"], default="A")
    args = parser.parse_args()

    # Path instance berdasarkan struktur dosen:
    # DAA_Instances/run.py  ← file ini
    # data/... berada di luar folder ini
    base_dir = Path(__file__).resolve().parent.parent
    instance_path = base_dir / args.instance

    if not instance_path.exists():
        raise FileNotFoundError(f"Instance file tidak ditemukan: {instance_path}")

    # load instance
    with open(instance_path, "r", encoding="utf-8") as f:
        inst = json.load(f)

    t0 = time.perf_counter()
    out = algo_A(inst) if args.algo == "A" else algo_B(inst)
    dt = (time.perf_counter() - t0) * 1000
    score = evaluate(out)

    print(f"\nAlgo = {args.algo}")
    print(f"Total Profit = {score}")
    print(f"Time = {dt:.2f} ms")
    print("\nOutput Jobs:")
    for job in out:
        print(job)


if __name__ == "__main__":
    main()
