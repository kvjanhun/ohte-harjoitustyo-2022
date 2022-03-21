import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(0)

    def test_rahaa_aluksi_oikea_maara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_aluksi_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_aluksi_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisesti_kateisella_vahentaa_oikean_summan(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaasti_kateisella_vahentaa_oikean_summan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullisesti_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), 760)

    def test_maukkaasti_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)

    def test_edullisesti_laskuri_kasvaa_yhdella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaasti_laskuri_kasvaa_yhdella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisesti_palauttaa_rahat_jos_kateinen_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(101), 101)

    def test_maukkaasti_palauttaa_rahat_jos_kateinen_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(106), 106)

    def test_edullisesti_ei_kasvata_laskuria_jos_kateinen_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(125)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaasti_ei_kasvata_laskuria_jos_kateinen_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(180)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisesti_maksukortilla_onnistuu(self):
        self.maksukortti.lataa_rahaa(240)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_edullisesti_maksukortilla_kasvattaa_laskuria(self):
        self.maksukortti.lataa_rahaa(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_maksukortilla_ei_onnistu_kun_saldo_ei_riita(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_epaonnistunut_edullisesti_maksukortilla_ei_kasvata_laskuria(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaasti_maksukortilla_onnistuu(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaasti_maksukortilla_kasvattaa_laskuria(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_maksukortilla_ei_onnistu_kun_saldo_ei_riita(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_epaonnistunut_maukkaasti_maksukortilla_ei_kasvata_laskuria(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_maksaminen_ei_vaikuta_kassan_saldoon(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteella_rahan_lataaminen_maksukortille_kasvattaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kassapaatteella_rahan_lataaminen_maksukortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kassapaatteella_ladattu_negatiivinen_summa_ei_vaikuta_kortin_saldoon(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 0)
