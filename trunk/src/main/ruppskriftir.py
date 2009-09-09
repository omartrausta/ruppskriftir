# encoding: utf-8
import os, sys, pickle 
from fractions import Fraction

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
            
    # Fall sem les uppúr skrá
    def lesaSkra(self):
        path = self.path
        uppskrift = {}
        verd = {}
        einingar = {}
        
        try:
            file = open(path, 'r')
            line = file.readline()
            while len(line)> 0:
                line = line.rstrip()
                dalkar = line.split()
                if len(dalkar) == 4:
                    dalkarUpphaf = dalkar
                if len(dalkar) == 7:
                    dalkarForm = dalkar
                if len(dalkar) == 3:
                    dalkarForm = dalkarUpphaf + dalkar
                #print dalkarForm
                if (len(dalkar) == 3 or len(dalkar) == 7):
                    # setja inn inn í dictonary
                    # ef stak 3 og 6 eru eins setjum við inn í einingar
                    if dalkarForm[2] == dalkarForm[6]:
                        print dalkarForm[2]
                        fractEin = Fraction(int(dalkarForm[4]),int(dalkarForm[0]))
                        eining = dalkarForm[5]
                        unit = dalkarForm[1]
                        tup = [(unit,fractEin,eining)]
                        if einingar.has_key(dalkarForm[2]):
                            #tupListi = []
                            tupEin = einingar[dalkarForm[2]] + tup
                            #tupListi.append(tupEin)
                            #tupEin.append(tup)
                            einingar[dalkarForm[2]]=tupEin
                        else:
                            einingar[dalkarForm[2]]=tup
      

                #if dalkarForm[2] == dalkarForm[6]:
                    #print dalkarForm[2]
                
                
                line = file.readline()  
                
            #ars = einingar["*"]
            print einingar
            print einingar["basil"][0][0]
                
        except IOError as (errno):
            print "I/O error({0}): ".format(errno)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
      
    def setPath(self,currdir):
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
    #print listi
    
if __name__== "__main__": main()