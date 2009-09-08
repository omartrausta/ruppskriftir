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
            
    # Fall sem les uppúr skrá
    def lesaSkra(self):
        path = self.path
        try:
            f = open(path, 'r')
            
            for line in f.readline():
                indented = line[0] == " "
                line = line.rstrip()
                
                dalkar = line.split()
                if len(dalkar) > 0:
                    if len(dalkar) >= 6:
                        magn, ein, nafn, er, magn2, ein2 = dalkar[:6]
                        if len(dalkar)==7:
                            nafn2 = dalkar[6]
                        else:
                            nafn2 = nafn
                        
                        print magn, ein, nafn, magn2, ein2, nafn2
                elif len(dalkar) == 4:
                    magn, ein, nafn, = dalkar[:3]
                    print "Byrjum uppskrift", magn, ein, nafn
                    indentline=f.readline()
                    while len(indentline.rstrip())>0:
                        indentline = f.readline()
                        print "indentuð", indentline
                else:
                    print "ég skil ekki", line
                
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
    print listi
    
if __name__== "__main__": main()