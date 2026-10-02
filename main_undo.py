from sistem_layanan import StackUndo

s = StackUndo()

print("=== SIMULASI FITUR UNDO (SOAL NO. 9 & 10) ===")

# Langkah 1: Push
s.push("08:00", "Tambah Antrean A001")

# Langkah 2: Push
s.push("08:05", "Tambah Antrean A002")

# Langkah 3: Pop (Undo)
s.pop()

# Langkah 4: Push
s.push("08:10", "Tambah Antrean A003")

# Langkah 5: Pop (Undo)
s.pop()

print("\n--- Kondisi Akhir Antrean ---")
s.tampilkan_stack()