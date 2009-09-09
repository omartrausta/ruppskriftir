# encoding: utf-8
import os, sys
from fractions import Fraction

class Ruppskriftir:
    
    def __init__(self, currdir=None):
        self.magn = ""
        self.eining = ""
        self.vara = ""
        self.nafnInnihald = ""
        self.endurkvaemt = False
        self.path = self.setPath(currdir)
    
    # Fall sem á að skrifa út umbeðna uppskrift    
    def innihald(self, magn, eining, vara, innihald="", endurkvaemt=False):
        pass
            
    # Fall sem les uppúr skrá
    def lesaSkra(self):
        path = self.path
        uppskrift = {}
        uppskriftUnit = {}
        verd = {}
        einingar = {}
        
        try:
            #----------------------
            # opna og lesa úr skrá
            #----------------------            
            file = open(path, 'r')
            line = file.readline()
            while len(line) > 0:
                line = line.rstrip()
                dalkar = line.split()
                if len(dalkar) == 4:
                    dalkarUpphaf = dalkar
                if len(dalkar) == 7:
                    dalkarForm = dalkar
                if len(dalkar) == 3:
                    dalkarForm = dalkarUpphaf + dalkar
                if (len(dalkar) == 3 or len(dalkar) == 7):
                    #----------------------
                    # setja inn inn í dictonary
                    #----------------------
                    
                    #----------------------
                    # ef stak 3 og 6 eru eins setjum við inn í einingar
                    #----------------------
                    if dalkarForm[2] == dalkarForm[6]:
                        #print dalkarForm[2]
                        fractEin = Fraction(int(dalkarForm[4]), int(dalkarForm[0]))
                        eining = dalkarForm[5]
                        unit = dalkarForm[1]
                        tup = [(unit, fractEin, eining)]
                        if einingar.has_key(dalkarForm[2]):
                            tupEin = einingar[dalkarForm[2]] + tup
                            einingar[dalkarForm[2]] = tupEin
                        else:
                            einingar[dalkarForm[2]] = tup
                    #----------------------
                    # setja inn verð á einingum í verd
                    #----------------------                            
                    if dalkarForm[6] == "peningar":
                        verdPerUnit = float(dalkarForm[4]) / float(dalkarForm[0])
                        verd[dalkarForm[2]] = (dalkarForm[1], verdPerUnit)
                    #----------------------
                    # setja inn í uppskriftir og uppskriftirUnit
                    # uppskrfitirUnit halda utan um grunneiningu sem fæst með því að 
                    # vinna úr uppskrift
                    #----------------------
                    if dalkarForm[2] != dalkarForm[6] and dalkarForm[6] != "peningar":
                        magn = Fraction(int(dalkarForm[4]), int(dalkarForm[0]))
                        eining = dalkarForm[5]
                        innih = dalkarForm[6]
                        tup = [(magn, eining, innih)]
                        if uppskrift.has_key(dalkarForm[2]):
                            tupEin = uppskrift[dalkarForm[2]] + tup
                            uppskrift[dalkarForm[2]] = tupEin
                        else:
                            uppskriftUnit[dalkarForm[2]] = (1, dalkarForm[1])
                            uppskrift[dalkarForm[2]] = tup                            
                line = file.readline()  
                
            print einingar
            print einingar["basil"][0][0]
            print verd
            print uppskrift
            print uppskriftUnit
                
        except IOError as (errno):
            print "I/O error({0}): ".format(errno)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
      
    def setPath(self, currdir):
        if currdir == None:
            os.chdir(os.getcwd() + '/../..')
        else:
            os.chdir(currdir + '/../..')
        path = os.getcwd()
        path = path + os.sep + 'tmp' + os.sep + 'testskra.txt'
        print path
        return path
    
def main():
    uppsrkiftir = Ruppskriftir()
    listi = uppsrkiftir.lesaSkra()
    print listi
    
if __name__ == "__main__": main()
