# encoding: utf-8
import unittest, os
from main.ruppskriftir import Ruppskriftir

class TestRuppskriftir(unittest.TestCase):
    
    magn = ""
    eining = ""
    vara = ""
    innihald = ""
    endurkvaemt = False
    currdir = os.getcwd()
    
    def setUp(self):
        self.uppskrift = Ruppskriftir(self.currdir)
    
    def testInnihald(self):
        self.uppskrift.innihald(self.magn, self.eining, self.vara, self.innihald, self.endurkvaemt)
    
    def testLesaSkra(self):
        object = self.uppskrift.lesaSkra()
        print object
    
    def tearDown(self):
        self.uppskrift = None
        
if __name__ == '__main__': unittest.main()