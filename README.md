# mdi-employee-insights

Mini tool buat baca dan ngeringkas data karyawan dari file CSV (tugas Manajemen Data & Informasi). 
Fokus ke 3 hal: **gender**, **status karyawan**, dan **performance score**, plus hitung **turnover**.

## Fitur
- Bersihin kolom kosong (semisal `Unnamed:*`)
- Parse tanggal rapi (StartDate, ExitDate, DOB)
- Ringkasan cepat:
  - Distribusi Gender
  - Status Karyawan (Active / Future Start / Terminated)
  - Turnover = Terminated / (Active + Terminated)
  - Performance Score (count per kategori)
  - Rata-rata Rating per Divisi
  - Status per Divisi (pivot) untuk gambaran sebaran

## Requirements
- Python 3.11+
- pandas

## Install
```powershell
py -m pip install pandas
