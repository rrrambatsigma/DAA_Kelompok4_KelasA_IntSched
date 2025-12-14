```md
# DAA Instance Package – Interval Scheduling

Proyek ini berisi **instance scheduling berbasis interval** yang digunakan untuk eksperimen
perbandingan algoritma **Greedy Earliest Finish Time (EFT)** dan **Greedy Profit Density**  
pada mata kuliah *Desain dan Analisis Algoritma (DAA)*.

Seluruh instance **dikunci (locked)** agar hasil eksperimen **reproducible** dan
konsisten dengan notebook eksperimen.

---

## Struktur Folder

```

DAA_Kelompok4_KelasA_IntSched/
│
├── DAA_Instances/
│   ├── run.py                 # Eksekusi algoritma EFT / Density dari JSON
│   └── generate_instances.py  # Generator instance (CSV → JSON terkunci)
│
├── data/
│   └── locked_instances.json  # Instance hasil randomisasi yang dikunci
│
├── notebook/
│   └── 02 Bentuk Jupyter file dengan break .ipynb
│
└── README.md

````

---

## Format Instance JSON

Setiap instance mewakili **1 kombinasi Hari + Ruang**.

Struktur utama:
```json
{
  "group": "G04",
  "source_dataset": "...normalized_fix_2.csv",
  "instances": [
    {
      "instance_id": "Kamis_R001",
      "num_intervals": 11,
      "data": [ ... ]
    }
  ]
}
````

Setiap interval memiliki atribut:

* Hari
* Mata Kuliah
* SKS
* Ruang
* start, finish
* duration
* profit_density

---

## Cara Pakai (Quick Start)

Masuk ke folder `DAA_Instances`:

```bash
cd DAA_Instances
```

### 1. Jalankan Algoritma Greedy EFT

```bash
python run.py --data ../data/locked_instances.json --algo EFT
```

### 2. Jalankan Algoritma Greedy Profit Density

```bash
python run.py --data ../data/locked_instances.json --algo DENSITY
```

---

## Output Program

Untuk setiap instance, program akan menampilkan:

* Instance ID
* Algoritma yang digunakan
* Jumlah interval terpilih
* Total SKS
* Runtime (ms)
* Validitas jadwal (tidak konflik)
* Daftar interval terpilih

---

## Algoritma yang Digunakan

### 1. Greedy Earliest Finish Time (EFT)

* Urut berdasarkan `finish_abs`
* Ambil interval yang selesai paling cepat dan tidak konflik

**Kompleksitas Waktu**

```
O(n log n)
```

---

### 2. Greedy Profit Density

* Urut berdasarkan `profit_density` (descending)
* Cek konflik terhadap interval yang sudah dipilih

**Kompleksitas Waktu**

```
O(n log n + n²)
```

---

## Reproducibility

* Randomisasi dilakukan **di notebook**
* Instance disimpan ke `locked_instances.json`
* `run.py` **tidak melakukan randomisasi**
* Hasil CLI = hasil notebook

---

## Tujuan Penggunaan

* Membandingkan EFT vs Density secara adil
* Analisis runtime, jumlah interval, dan total SKS
* Menunjukkan trade-off optimalitas vs kecepatan
* Eksperimen dapat direproduksi tanpa notebook

---

## Catatan

* File `locked_instances.json` **tidak boleh diubah**
* Jika ingin eksperimen baru, gunakan `generate_instances.py`
* Notebook hanya untuk eksplorasi dan analisis

---

## Contoh Perintah Lengkap

```bash
python run.py --data ../data/locked_instances.json --algo EFT
python run.py --data ../data/locked_instances.json --algo DENSITY
```

```
