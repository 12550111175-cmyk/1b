import unittest
from sistem_layanan import QueueAntrean, StackUndo


# ==========================================
# 1. PENGUJIAN FITUR ANTREAN (QUEUE)
# ==========================================
class TestQueueAntrean(unittest.TestCase):
    def setUp(self):
        self.q = QueueAntrean()

    # 1. Pengujian Penambahan Data (Enqueue)
    def test_enqueue(self):
        self.q.enqueue("A001", "Budi Santoso")
        self.assertEqual(len(self.q.antrean), 1)

    # 2. Pengujian Penghapusan Data (Dequeue)
    def test_dequeue(self):
        self.q.enqueue("A001", "Budi Santoso")
        hasil = self.q.dequeue()
        self.assertEqual(hasil["nomor_urut"], "A001")

    # 3. Pengujian Melihat Data Terdepan (Peek)
    def test_peek(self):
        self.q.enqueue("A001", "Budi Santoso")
        terdepan = self.q.peek()
        self.assertEqual(terdepan["nomor_urut"], "A001")

    # 4. Pengujian Memeriksa Kondisi Kosong (IsEmpty)
    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())


# ==========================================
# 2. PENGUJIAN FITUR UNDO (STACK)
# ==========================================
class TestFiturUndo(unittest.TestCase):

    def setUp(self):
        self.s = StackUndo()

    # 1. Pengujian Penambahan Riwayat / Push
    def test_push(self):
        self.s.push("08:00", "Tambah Antrean A001")
        self.assertEqual(len(self.s.stack), 1)

    # 2. Pengujian Pembatalan / Pop (Undo)
    def test_pop_undo(self):
        self.s.push("08:00", "Tambah Antrean A001")
        hasil = self.s.pop()
        self.assertEqual(hasil["aktivitas"], "Tambah Antrean A001")
        self.assertTrue(self.s.is_empty())

    # 3. Pengujian Melihat Aktivitas Teratas (Peek)
    def test_peek_undo(self):
        self.s.push("08:00", "Tambah Antrean A001")
        teratas = self.s.peek()
        self.assertEqual(teratas["aktivitas"], "Tambah Antrean A001")

    # 4. Pengujian Memeriksa Kondisi Kosong (IsEmpty)
    def test_is_empty_undo(self):
        self.assertTrue(self.s.is_empty())


if __name__ == '__main__':
    unittest.main()