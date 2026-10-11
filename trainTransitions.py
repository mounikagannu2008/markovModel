import markovmodel as m
import generate as g

class train:
    def __init__(self,markovmodel:object):
        self.model = markovmodel
#pass line(list)
    def addline(self,line):
        for i in range(0,len(line)-1):
           if i==0:
              self.model.appendStart(line[i])
           #end case 
           if i == len(line)-2:
              self.model.appendNextWord(line[i+1].strip(),"<EOS>")
           self.model.appendNextWord(line[i].strip(),line[i+1].strip())

    def addSecondLine(self,line):
       for i in range(0,len(line)-2):
          if i==0:
             self.model.appendSecondStart(line[i],line[i+1])
          if i == len(line)-3:
             self.model.appendSecondNextWord(line[i+1].strip(),line[i+2].strip(),"<EOS>")
          self.model.appendSecondNextWord(line[i].strip(),line[i+1].strip(),line[i+2].strip())
      
    def addData(self,data:list):
     for line in data:
        self.addline(line)

    def addSecondData(self,data):
       for line in data:
         self.addSecondLine(line)
    
           


