import unittest
from main.ruppskriftir import Ruppskriftir

class TestRuppskriftir(unittest.TestCase):
    
    magn = ""
    eining = ""
    vara = ""
    innihald= ""
    endurkvaemt=False
    
    def testInnihald(self):
        uppskrift = Ruppskriftir()
        uppskrift.innihald(self.magn,self.eining,self.vara,self.innihald,self.endurkvaemt)
    
    def testBuaTilUppskrift(self):
        uppskrift = Ruppskriftir()
        uppskrift.buaTilUppskrift()