import pandas as pd
import os
import glob
import sys

csv_files = glob.glob("*.csv")
excel_files = glob.glob("*.xlsx")

if not csv_files and not excel_files:
    print("❌ Tidak ada file CSV/XLSX di folder ini.")
    print("➡ Silakan tambahkan file data karyawan (CSV/Excel) ke folder repo.")
    sys.exit()

if csv_files:
    file_path = csv_files[0]
    df = pd.read_csv(file_path)
    print(f"✅ File CSV ditemukan: {file_path}")
else:
    file_path = excel_files[0]
    df = pd.read_excel(file_path)
    print(f"✅ File Excel ditemukan: {file_path}")

drop_cols = [c for c in df.columns if c.startswith("Unnamed:")]
if drop_cols:
    df = df.drop(columns=drop_cols)

if "StartDate" in df.columns:
    df["StartDate"] = pd.to_datetime(df["StartDate"], errors="coerce")
if "ExitDate" in df.columns:
    df["ExitDate"] = pd.to_datetime(df["ExitDate"], errors="coerce")
if "DOB" in df.columns:
    df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce")

print(">> 5 baris pertama:")
print(df.head(), "\n")

print("--- INFO DATASET (setelah bersih) ---")
print(df.info(), "\n")

print("--- DISTRIBUSI GENDER ---")
if "GenderCode" in df.columns:
    print(df["GenderCode"].value_counts(), "\n")
else:
    print("Kolom 'GenderCode' tidak ditemukan.\n")

print("--- STATUS KARYAWAN ---")
if "EmployeeStatus" in df.columns:
    status_counts = df["EmployeeStatus"].value_counts()
    print(status_counts, "\n")
else:
    status_counts = pd.Series(dtype=int)
    print("Kolom 'EmployeeStatus' tidak ditemukan.\n")

active_mask = df.get("EmployeeStatus", pd.Series()).astype(str).str.contains("Active", na=False)
term_mask   = df.get("EmployeeStatus", pd.Series()).astype(str).str.contains("Terminated", na=False)

active_n = int(active_mask.sum()) if not isinstance(active_mask, bool) else 0
term_n   = int(term_mask.sum()) if not isinstance(term_mask, bool) else 0
denom    = active_n + term_n
turnover = (term_n / denom) if denom > 0 else 0.0

print(f"--- TURNOVER ---\nTerminated: {term_n} | Active: {active_n} | Turnover: {turnover:.3%}\n")

print("--- PERFORMANCE SCORE ---")
if "Performance Score" in df.columns:
    print(df["Performance Score"].value_counts(), "\n")
else:
    print("Kolom 'Performance Score' tidak ditemukan.\n")

print("--- RATA-RATA RATING PER DIVISI (TOP–BOTTOM) ---")
if "Division" in df.columns and "Current Employee Rating" in df.columns:
    avg_rating_div = (
        df.groupby("Division")["Current Employee Rating"]
          .mean().sort_values(ascending=False)
    )
    print(avg_rating_div.to_string(), "\n")
else:
    print("Kolom 'Division' atau 'Current Employee Rating' tidak ditemukan.\n")

print("--- STATUS PER DIVISI (pivot) ---")
if "Division" in df.columns and "EmployeeStatus" in df.columns and "EmpID" in df.columns:
    pivot = pd.pivot_table(
        df, index="Division", columns="EmployeeStatus",
        values="EmpID", aggfunc="count", fill_value=0
    )
    print(pivot.to_string(), "\n")
else:
    print("Pivot tidak bisa dibuat: pastikan 'Division', 'EmployeeStatus', 'EmpID' ada.\n")