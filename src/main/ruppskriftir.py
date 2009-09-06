# encoding: utf-8
import os, pickle

class Ruppskriftir:
    
    def __init__(self):
        self.magn = ""
        self.eining = ""
        self.vara = ""
        self.nafnInnihald = ""
        self.endurkvaemt = False
    
    # Fall sem á að skrifa út umbeðna uppskrift    
    def innihald(self, magn, eining, vara, innihald="", endurkvaemt=False):
        pass
    
    # Fall gæti tekið klasa af uppskriftum
    def buaTilUppskrift(self):
        pass
    
    # Fall sem skrifar í skrá
    def skrifaSkra(self,object):
        path = self.getPath()
        try:
            f = open(path, 'w')
            pickle.dump(object, f)
            f.close()
        except IOError:
            print 'cannot open', path
            
    # Fall sem les uppúr skrá
    def lesaSkra(self):
        f = None
        path = self.getPath()
        try:
            f = open(path, 'r')
            object = pickle.load(f)
            f.close()
            return object
        except IOError:
            print 'cannot open', path
      
    def getPath(self):
        os.chdir(os.getcwd() + '/../..')
        path = os.getcwd()
        #print path
        path = path + os.sep + 'tmp' + os.sep + 'gogn'
        return path
    
def main():
    listi = { 'einingar': {'bolli': (200,'g'), 'msk':(15,'ml')} }
    uppsrkiftir = Ruppskriftir()
    uppsrkiftir.skrifaSkra(listi)
    listi = uppsrkiftir.lesaSkra()
    print listi

if __name__== "__main__": main()