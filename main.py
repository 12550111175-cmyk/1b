# Memanggil/mengimpor kelas dari file sistem_layanan.py
from sistem_layanan import QueueAntrean, StackUndo

print("=== SIMULASI FITUR ANTREAN ===")
q = QueueAntrean()

# Jalankan operasi Antrean
q.enqueue("A001", "Budi Santoso")
q.enqueue("A002", "Siti Aminah")
print("Mahasiswa Terdepan (Peek):", q.peek())
q.dequeue()
q.tampilkan_antrean()

print("\n=== SIMULASI FITUR UNDO ===")
s = StackUndo()

# Jalankan operasi Undo
s.push("2026-10-01 08:00", "Menambahkan antrean A001")
s.push("2026-10-01 08:05", "Menambahkan antrean A002")
print("Aktivitas Teratas (Peek):", s.peek())
s.pop()
s.tampilkan_stack()