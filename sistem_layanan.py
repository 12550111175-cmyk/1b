from collections import deque

# ==========================================
# 1. IMPLEMENTASI FITUR ANTREAN (QUEUE)
# ==========================================
class QueueAntrean:
    """
    Menggunakan modul collections.deque untuk mengimplementasikan
    prinsip FIFO (First-In, First-Out).
    """
    def __init__(self):
        self.antrean = deque()

    # Enqueue: Menambahkan mahasiswa ke barisan belakang
    def enqueue(self, nomor_urut, nama):
        mahasiswa = {"nomor_urut": nomor_urut, "nama": nama}
        self.antrean.append(mahasiswa)
        print(f"[Enqueue] Mahasiswa {nama} ({nomor_urut}) masuk ke antrean.")

    # Dequeue: Melayani dan mengeluarkan mahasiswa dari barisan depan
    def dequeue(self):
        if not self.is_empty():
            mahasiswa = self.antrean.popleft()
            print(f"[Dequeue] Mahasiswa {mahasiswa['nama']} ({mahasiswa['nomor_urut']}) telah dilayani.")
            return mahasiswa
        print("[Dequeue] Antrean kosong, tidak ada yang dilayani.")
        return None

    # Peek/Front: Melihat mahasiswa paling depan tanpa memprosesnya
    def peek(self):
        if not self.is_empty():
            return self.antrean[0]
        return None

    # IsEmpty: Memeriksa apakah antrean kosong
    def is_empty(self):
        return len(self.antrean) == 0

    # Menampilkan kondisi antrean saat ini
    def tampilkan_antrean(self):
        print("Kondisi Antrean Saat Ini:", list(self.antrean))


# ==========================================
# 2. IMPLEMENTASI FITUR UNDO (STACK)
# ==========================================
class StackUndo:
    """
    Menggunakan list Python biasa untuk mengimplementasikan
    prinsip LIFO (Last-In, First-Out).
    """
    def __init__(self):
        self.stack = []

    # Push: Menyimpan aktivitas baru ke atas tumpukan
    def push(self, tanggal_jam, aktivitas):
        log = {"tanggal_jam": tanggal_jam, "aktivitas": aktivitas}
        self.stack.append(log)
        print(f"[Push] Aktivitas dicatat: '{aktivitas}' pada {tanggal_jam}")

    # Pop: Membatalkan aktivitas paling terakhir (paling atas tumpukan)
    def pop(self):
        if not self.is_empty():
            aktivitas_dibatalkan = self.stack.pop()
            print(f"[Pop/Undo] Membatalkan aktivitas: '{aktivitas_dibatalkan['aktivitas']}'")
            return aktivitas_dibatalkan
        print("[Pop/Undo] Tidak ada aktivitas yang dapat dibatalkan.")
        return None

    # Peek/Top: Melihat aktivitas teratas tanpa membatalkannya
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    # IsEmpty: Memeriksa apakah riwayat aktivitas kosong
    def is_empty(self):
        return len(self.stack) == 0

    # Menampilkan kondisi tumpukan undo saat ini
    def tampilkan_stack(self):
        print("Kondisi Stack Undo Saat Ini:", self.stack)


