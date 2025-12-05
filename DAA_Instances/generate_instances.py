import json, random
from pathlib import Path

# -------------------------------------
# Lokasi folder data (satu level di atas DAA_Instances)
# -------------------------------------
BASE = Path(__file__).resolve().parent.parent / "data"
BASE.mkdir(exist_ok=True)

def save(name, obj):
    p = BASE / name
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
    return p


# -------------------------------------
# Generator Instance Interval Scheduling
# -------------------------------------
def generate(seed=1):
    random.seed(seed)
    jobs = []

    # jumlah job bervariasi
    n = 8 + (seed % 5)

    for i in range(n):
        start = random.randint(7, 14)          # jam mulai
        duration = random.randint(1, 3)        # lama kegiatan
        finish = start + duration
        profit = random.randint(5, 20)         # bobot / profit

        jobs.append({
            "id": i + 1,
            "start": start,
            "finish": finish,
            "profit": profit
        })

    return {
        "project": "interval",
        "jobs": jobs
    }


# -------------------------------------
# MAIN – generate beberapa instance
# -------------------------------------
def main():
    for i in range(1, 6):
        inst = generate(seed=100 + i)
        save(f"interval_G{i:02d}.json", inst)

    print("Generated 5 interval scheduling instances inside /data folder.")


if __name__ == "__main__":
    main()
