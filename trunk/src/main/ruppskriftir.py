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
        except IOError:
            print 'cannot open', path

        pickle.dump(object, f)
        f.close()
            
    # Fall sem les uppúr skrá
    def lesaSkra(self):
        path = self.getPath()
        try:
            f = open(path, 'r+')
        except IOError:
            print 'cannot open', path
        
        object = pickle.load(f)
        f.close()
        return object
        
    def getPath(self):
        os.chdir(os.getcwd() + '/../..')
        path = os.getcwd()
        #print path
        path = path + os.sep + 'tmp' + os.sep + 'workfile'
        return path
    
def main():
    listi = [(1,"Halló Heimur"),(2,"Halló Heimur"),(3,"Halló Heimur")]
    uppsrkiftir = Ruppskriftir()
    uppsrkiftir.skrifaSkra(listi)
    print uppsrkiftir.lesaSkra()

if __name__== "__main__": main()