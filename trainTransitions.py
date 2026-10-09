import markovmodel as m
import generate as g

class train:
    def __init__(self,markovmodel:object):
        self.model = markovmodel
#pass line(list)
    def addline(self,line):
        for i in range(0,len(line)-1):
           #end case 
           if i == len(line)-2:
              self.model.appendNextWord(line[i+1].strip(),"<EOS>")
           self.model.appendNextWord(line[i].strip(),line[i+1].strip())
    def addData(self,data:list):
     for line in data:
        self.addline(line)
    
           


