import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def test_saldo_euroina(self):
        kortti = Maksukortti(500)
        self.assertEqual(kortti.saldo_euroina(), 5.00)

    def test_str_esitys(self):
        kortti = Maksukortti(9760)
        self.assertEqual(str(kortti), "Kortilla on rahaa 97.60 euroa")

    def test_lataa_rahaa(self):
        kortti = Maksukortti(200)
        kortti.lataa_rahaa(300)
        self.assertEqual(kortti.saldo, 500)

    def test_ota_rahaa_ei_onnistu_jos_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        tulos = kortti.ota_rahaa(300)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 200)

    def test_ota_rahaa_ei_onnistu_jos_on_tarpeeksi(self):
        kortti = Maksukortti(2000)
        tulos = kortti.ota_rahaa(300)
        self.assertTrue(tulos)
        self.assertEqual(kortti.saldo, 1700)

    
