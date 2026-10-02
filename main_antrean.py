from sistem_layanan import QueueAntrean

q = QueueAntrean()

print("=== SIMULASI FITUR ANTREAN (SOAL NO. 7 & 8) ===")

# 5 Langkah Simulasi Antrean
q.enqueue("A001", "Budi Santoso")    # Langkah 1
q.enqueue("A002", "Siti Aminah")     # Langkah 2
q.enqueue("A003", "Rian Hidayat")    # Langkah 3
q.dequeue()                          # Langkah 4
q.enqueue("A004", "Dewi Lestari")    # Langkah 5
q.dequeue()                          # Langkah 6
q.enqueue("A005", "Eko Prasetyo")    # Langkah 7

print("\n--- Kondisi Akhir Antrean ---")
q.tampilkan_antrean()