import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_rahaa_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1250)
        self.assertEqual(self.maksukortti.saldo, 2250)

    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(350)
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo, 450)

    def test_saldo_ei_vahene_kun_rahaa_liian_vahan(self):
        self.maksukortti.ota_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_ota_rahaa_palauttaa_true_kun_rahaa_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(200))

    def test_ota_rahaa_palauttaa_false_kun_rahaa_liian_vahan(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1200))

    def test_saldo_tulostuu_merkkijonona_oikein(self):
        self.assertEqual(str(self.maksukortti), f"saldo: 10.0")
        