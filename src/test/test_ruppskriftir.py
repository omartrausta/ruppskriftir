# encoding: utf-8
import unittest
from main.ruppskriftir import Ruppskriftir

class TestRuppskriftir(unittest.TestCase):
    
    magn = ""
    eining = ""
    vara = ""
    innihald = ""
    endurkvaemt = False
    
    def setUp(self):
        self.uppskrift = Ruppskriftir()
    
    def testInnihald(self):
        self.uppskrift.innihald(self.magn, self.eining, self.vara, self.innihald, self.endurkvaemt)
    
    def testBuaTilUppskrift(self):
        self.uppskrift.buaTilUppskrift()
        
    def testSkrifaSkra(self):
        self.uppskrift.skrifaSkra()

    def testLesaSkra(self):
        self.uppskrift.lesaSkra()

if __name__ == '__main__': unittest.main()
