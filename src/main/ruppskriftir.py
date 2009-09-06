# encoding: utf-8

class Ruppskriftir:
    def __init__(self):
        self.magn = ""
        self.eining = ""
        self.vara = ""
        self.nafnInnihald = ""
        self.endurkvaemt = False
    
    # Falls sem á að skrifa út umbeðna uppskrift    
    def innihald(self, magn, eining, vara, innihald="", endurkvaemt=False):
        pass
    
    # Fall gæti tekið klasa af uppskriftum
    def buaTilUppskrift(self):
        pass
    
    # Fall sem skrifar í skrá
    def skrifaSkra(self):
        pass

    # Fall sem les uppúr skrá
    def lesaSkra(self):
        pass
