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
        listi = [(1,"Halló Heimur"),(2,"Halló Heimur"),(3,"Halló Heimur")]
        self.uppskrift.skrifaSkra(listi)

    def testLesaSkra(self):
        object = self.uppskrift.lesaSkra()
        print object
    
    def tearDown(self):
        self.uppskrift = None
        
if __name__ == '__main__': unittest.main()