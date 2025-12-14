Siap 👍
Aku **generate ulang FULL README.md UTUH (tidak terpisah-pisah)**, sudah **rapi**, **konsisten**, dan **100% sesuai konteks proyek kamu + instruksi gambar** + **pakai `locked_instances.json`**.

Silakan **langsung copas satu blok ini** ke `README.md`.

---

```md
# DAA Instance Package  
**Proyek:** Interval Scheduling – Greedy Algorithms (EFT vs Profit Density)

Repository ini berisi *instance scheduling* yang telah **dikunci (locked)** berdasarkan hasil eksperimen pada notebook, beserta skrip Python untuk mengeksekusi algoritma **Earliest Finish Time (EFT)** dan **Greedy Profit Density** secara konsisten dan reproducible.

---

## Struktur Folder

```

DAA_Kelompok4_KelasA_IntSched/
│
├── DAA_Instances/
│   ├── run.py                  # Eksekusi algoritma pada instance JSON
│   ├── generate_instances.py   # Generator instance (berbasis hasil eksperimen)
│
├── data/
│   ├── locked_instances.json   # Instance hasil randomisasi yang sudah dikunci
│   └── normalized_fix_2.csv    # Dataset asli
│
└── README.md

````

---

## Deskripsi File

### 📁 `data/locked_instances.json`
- Berisi **instance interval scheduling yang sudah dikunci**
- Dibangkitkan dari eksperimen notebook dengan:
  - ukuran instance (`n`)
  - seed random
- Digunakan agar:
  - hasil eksperimen **tidak berubah**
  - evaluasi algoritma **reproducible**
- Setiap instance merepresentasikan:
  - Hari
  - Ruang
  - Sekumpulan interval (kelas)
  - Atribut waktu, SKS, dan profit density

---

### 🐍 `run.py`
Script utama untuk **menjalankan algoritma greedy langsung dari file JSON**, tanpa randomisasi ulang.

Algoritma yang tersedia:
- `EFT` → Earliest Finish Time
- `DENSITY` → Greedy Profit Density

Fungsi utama:
- Load instance dari JSON
- Jalankan algoritma per instance
- Hitung:
  - jumlah interval terpilih
  - total SKS
  - runtime
  - validitas jadwal (tanpa konflik)

---

### 🧪 `generate_instances.py`
Script untuk **membuat instance JSON** dari dataset CSV.

Digunakan untuk:
- Menghasilkan instance berbasis eksperimen notebook
- Mengunci hasil randomisasi ke dalam JSON
- Menjamin hasil `run.py` sama dengan notebook

---

## Cara Pakai Cepat

### Masuk ke folder eksekusi
```bash
cd DAA_Instances
````

### 1. Jalankan algoritma EFT

```bash
python run.py --data ..\data\locked_instances.json --algo EFT
```

### 2. Jalankan algoritma Greedy Density

```bash
python run.py --data ..\data\locked_instances.json --algo DENSITY
```

---

## Output Program

Untuk setiap instance, program akan menampilkan:

* ID instance
* Algoritma yang digunakan
* Jumlah interval (kelas) terpilih
* Total SKS
* Runtime (ms)
* Status validitas jadwal (tidak konflik)

## Kompleksitas Algoritma

| Algoritma                  | Kompleksitas Waktu |
| -------------------------- | ------------------ |
| Earliest Finish Time (EFT) | O(n log n)         |
| Greedy Profit Density      | O(n log n + n²)    |

Keterangan:

* `n` = jumlah interval dalam satu instance
* Faktor `n²` pada Density berasal dari pengecekan konflik antar interval

---

## Tujuan Penggunaan

* Evaluasi performa algoritma greedy
* Perbandingan kualitas solusi (total SKS)
* Analisis runtime
* Studi best case dan worst case
* Dokumentasi eksperimen DAA yang reproducible

---

**Catatan Akhir:**
File `locked_instances.json` merupakan **ground truth eksperimen**.
Notebook digunakan untuk eksplorasi, sedangkan `run.py` digunakan untuk eksekusi cepat dan validasi hasil.

```