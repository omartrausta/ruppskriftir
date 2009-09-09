# encoding: utf-8
import os, sys
from fractions import Fraction

class Ruppskriftir:

    uppskrift = {}
    uppskriftUnit = {}
    verd = {}
    einingar = {}
    g = 0
          
    def __init__(self, currdir=None):
        self.path = self.setPath(currdir)
        self.lesaSkra()

    
    # Fall sem � a� skrifa �t umbe�na uppskrift    
    def innihald(self, magn, eining, vara, innihald="", endurkvaemt=False):
        if endurkvaemt == False:
            try:
                uppskriftVoru = self.uppskrift[vara]
                for innih in uppskriftVoru:
                    if innihald == "":
                        print  str(innih[0] * Fraction(magn, 1)) + " " + innih[1] + " " + innih[2]
                    elif innihald == innih[2]:
                        print  str(innih[0] * Fraction(magn, 1)) + " " + innih[1] + " " + innih[2]
            except:
                print "Uppskrift fyrir", vara, "fannst ekki"
        elif endurkvaemt == True:
            self.endurkvaemt(magn,eining,vara)
            
    def endurkvaemt(self,magn,eining,vara):
        self.g +=5
        print " "*self.g,"inniheldur",vara
        uppskriftVoru = self.uppskrift[vara]
        for innih in uppskriftVoru:
            #print " "*self.g + "inniheldur " +  str(innih[0] * Fraction(magn, 1)) + " " + innih[1] + " " + innih[2] + " " + str(self.summaVerd(innih[0],innih[1],innih[2]))
            print " "*self.g + "inniheldur " +  str(innih[0] * Fraction(magn, 1)) + " " + innih[1] + " " + innih[2]
            self.summaVerd(innih[0],innih[1],innih[2])
            if innih[2] in self.uppskrift.keys():
                print " "*self.g,innih[2],"á sér undiruppskrift" 
                self.endurkvaemt(innih[0],innih[1],innih[2])
                
                #print self.finnaVerd(eining)
                #print self.summaVerd(magn, finnaVerd(eining), eining)
        self.g-=5      
        
        
            
    def summaVerd(self,magn, maelieining, eining):
        print eining
        print maelieining
        print magn
        
        if eining in self.einingar.keys():
            tup = self.einingar[eining]
            print "tup=",tup
        else:
            print "hmmm"
            #return Fraction(magn, 1)/eining*self.finnaVerd(eining)
    
    def finnaVerd(self,eining):
        if eining in self.verd.keys():
            einingVerd = self.verd[eining]
            return einingVerd[1]
                  
    # Fall sem les upp�r skr�
    def lesaSkra(self):
        path = self.path
        
        try:
            #----------------------
            # opna og lesa �r skr�
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
                    # setja inn inn � dictonary
                    #----------------------
                    
                    #----------------------
                    # ef stak 3 og 6 eru eins setjum vi� inn � einingar
                    #----------------------
                    if dalkarForm[2] == dalkarForm[6]:
                        #print dalkarForm[2]
                        fractEin = Fraction(int(dalkarForm[4]), int(dalkarForm[0]))
                        eining = dalkarForm[5]
                        unit = dalkarForm[1]
                        tup = [(unit, fractEin, eining)]
                        if self.einingar.has_key(dalkarForm[2]):
                            tupEin = self.einingar[dalkarForm[2]] + tup
                            self.einingar[dalkarForm[2]] = tupEin
                        else:
                            self.einingar[dalkarForm[2]] = tup
                    #----------------------
                    # setja inn ver� � einingum � verd
                    #----------------------                            
                    if dalkarForm[6] == "peningar":
                        verdPerUnit = float(dalkarForm[4]) / float(dalkarForm[0])
                        self.verd[dalkarForm[2]] = (dalkarForm[1], verdPerUnit)
                    #----------------------
                    # setja inn � uppskriftir og uppskriftirUnit
                    # uppskrfitirUnit halda utan um grunneiningu sem f�st me� �v� a� 
                    # vinna �r uppskrift
                    #----------------------
                    if dalkarForm[2] != dalkarForm[6] and dalkarForm[6] != "peningar":
                        magn = Fraction(int(dalkarForm[4]), int(dalkarForm[0]))
                        eining = dalkarForm[5]
                        innih = dalkarForm[6]
                        tup = [(magn, eining, innih)]
                        if self.uppskrift.has_key(dalkarForm[2]):
                            tupEin = self.uppskrift[dalkarForm[2]] + tup
                            self.uppskrift[dalkarForm[2]] = tupEin
                        else:
                            self.uppskriftUnit[dalkarForm[2]] = (1, dalkarForm[1])
                            self.uppskrift[dalkarForm[2]] = tup                            
                line = file.readline()  
                
            print self.einingar
            #print self.einingar["basil"][0][0]
            #print self.verd
            #print self.uppskrift
            #print self.uppskriftUnit
                
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
    #listi = uppsrkiftir.lesaSkra()
    uppsrkiftir.innihald(3, "stk", "pepperonipizza","salt",True)
    #print listi
    
if __name__ == "__main__": main()

