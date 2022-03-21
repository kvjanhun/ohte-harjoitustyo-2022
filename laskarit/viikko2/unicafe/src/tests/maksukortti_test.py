import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataa_rahaa_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(12.50)
        self.assertEqual(self.maksukortti.saldo, 22.50)

    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(3.50)
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(self.maksukortti.saldo, 4.50)

    def test_saldo_ei_vahene_kun_rahaa_liian_vahan(self):
        self.maksukortti.ota_rahaa(25)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_ota_rahaa_palauttaa_true_kun_rahaa_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(2))

    def test_ota_rahaa_palauttaa_false_kun_rahaa_liian_vahan(self):
        self.assertFalse(self.maksukortti.ota_rahaa(12))

    