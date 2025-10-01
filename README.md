# MDI Employee Insights

<img width="1522" height="701" alt="image" src="https://github.com/user-attachments/assets/b2c5f1b3-8ba2-43a5-bfe1-c4340683f3d7" />

Mini tool buat baca dan ngeringkas data karyawan dari file CSV dan Excel (tugas Manajemen Data & Informasi). 
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
pip -r install requirements.txt
#jika setelah di run, hasil install library masih tidak muncul coba cara ini
py -m pip install pandas>=2.0, openpyxl>=3.0
````

## Cara pakai

1. Taruh file `sample employee_data.csv` di folder yang sama dengan `MDI.py`.
2. Jalankan:

```powershell
py .\MDI.py
```

3. Hasil akan tampil di console (nggak ada file yang disimpan).

## Struktur data yang diharapkan (contoh kolom)

* `EmpID, FirstName, LastName, StartDate, ExitDate, GenderCode, EmployeeStatus, Division, Performance Score, Current Employee Rating, ...`

## Catatan

* `DOB` di dataset bisa campur formatnya; script ini nyoba 2 pola umum.
* Kalau ada tanggal yang aneh → otomatis jadi `NaT` (nggak bikin script error).

## Lisensi

MIT (bebas dipakai buat belajar / tugas kuliah).
