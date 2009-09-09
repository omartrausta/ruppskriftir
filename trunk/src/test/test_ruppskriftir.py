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
        self.uppskrift.innihald(3, "stk", "pepperonipizza")
    
    def testLesaSkra(self):
        object = self.uppskrift.lesaSkra()
    
    def tearDown(self):
        self.uppskrift = None
        
if __name__ == '__main__': unittest.main()