# encoding: utf-8
import os, sys, pickle

class Ruppskriftir:
    
    def __init__(self,currdir=None):
        self.magn = ""
        self.eining = ""
        self.vara = ""
        self.nafnInnihald = ""
        self.endurkvaemt = False
        self.path = self.setPath(currdir)
    
    # Fall sem á að skrifa út umbeðna uppskrift    
    def innihald(self, magn, eining, vara, innihald="", endurkvaemt=False):
        pass
    
    # Fall gæti tekið klasa af uppskriftum
    def buaTilUppskrift(self):
        pass
    
    # Fall sem skrifar í skrá
    def skrifaSkra(self,object):
        path = self.path
        try:
            f = open(path, 'w')
            pickle.dump(object, f)
            f.close()
        except IOError as (errno, picklerror):
            print "I/O error({0}): {1}".format(errno, picklerror)
        except pickle.PickleError:
            print "Picle error."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
            
    # Fall sem les uppúr skrá
    def lesaSkra(self):
        f = None
        path = self.path
        try:
            f = open(path, 'r')
            object = pickle.load(f)
            f.close()
            return object
        except IOError as (errno, picklerror):
            print "I/O error({0}): {1}".format(errno, picklerror)
        except pickle.PickleError:
            print "Picle error."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
      
    def setPath(self,currdir):
        if currdir == None:
            os.chdir(os.getcwd() + '/../..')
        else:
            os.chdir(currdir + '/../..')
        path = os.getcwd()
        path = path + os.sep + 'tmp' + os.sep + 'gogn'
        print path
        return path
    
def main():
    listi = { 'einingar': {'bolli': (200,'g'), 'msk':[(15,'ml'),(3,'tsk')]} }
    uppsrkiftir = Ruppskriftir()
    uppsrkiftir.skrifaSkra(listi)
    listi = uppsrkiftir.lesaSkra()
    print listi
    einingar = listi['einingar']
    msk = einingar['msk']
    print msk
    
if __name__== "__main__": main()