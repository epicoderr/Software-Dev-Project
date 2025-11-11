import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def test_alkutila(self):
        paate = Kassapaate()
        self.assertEqual(paate.kassassa_rahaa, 100000)
        self.assertEqual(paate.edulliset, 0)
        self.assertEqual(paate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_riittavasti_rahaa(self):
        paate = Kassapaate()
        vaihtoraha = paate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(paate.kassassa_rahaa, 100240)
        self.assertEqual(paate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_riittavasti_rahaa(self):
        paate = Kassapaate()
        vaihtoraha = paate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(paate.kassassa_rahaa, 100000)
        self.assertEqual(paate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_riittavasti_rahaa(self):
        paate = Kassapaate()
        vaihtoraha = paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(paate.kassassa_rahaa, 100400)
        self.assertEqual(paate.maukkaat, 1)
        
    def test_syo_maukkaasti_kateisella_ei_riittavasti_rahaa(self):
        paate = Kassapaate()
        vaihtoraha = paate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(paate.kassassa_rahaa, 100000)
        self.assertEqual(paate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_riittavasti_rahaa(self):
        paate = Kassapaate()
        kortti = Maksukortti(300)
        tulos = paate.syo_edullisesti_kortilla(kortti)
        self.assertTrue(tulos)
        self.assertEqual(kortti.saldo, 60)
        self.assertEqual(paate.edulliset, 1)
        self.assertEqual(paate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_ei_riittavasti_rahaa(self):
        paate = Kassapaate()
        kortti = Maksukortti(200)
        tulos = paate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(paate.edulliset, 0)
        self.assertEqual(paate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_riittavasti_rahaa(self):
        paate = Kassapaate()
        kortti = Maksukortti(500)
        tulos = paate.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(tulos)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(paate.maukkaat, 1)
        self.assertEqual(paate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_ei_riittavasti_rahaa(self):
        paate = Kassapaate()
        kortti = Maksukortti(200)
        tulos = paate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(paate.maukkaat, 0)
        self.assertEqual(paate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self):
        paate = Kassapaate()
        kortti = Maksukortti(0)
        paate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 500)
        self.assertEqual(paate.kassassa_rahaa, 100500)

    def test_negatiivinen_lataus_ei_muuta_rahaa(self):
        paate = Kassapaate()
        kortti = Maksukortti(200)
        paate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(paate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina(self):
        paate = Kassapaate()
        self.assertEqual(paate.kassassa_rahaa_euroina(), 1000)