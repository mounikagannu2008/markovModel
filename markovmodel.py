import random

class markovmodel:
    def __init__(self):
        self.transition ={}
        self.starts={}

    def appendWord(self,word):
        if word not in self.transition:
          self.transition[word] = {}

    def appendStart(self,word):
         self.starts[word] = self.starts.get(word,0)+1

    def appendNextWord(self,word,next):
        self.appendWord(word)
        self.transition[word][next]=self.transition[word].get(next,0)+1

    def nextProbabilites(self,word):
        if word not in self.transition:
            return None
        return self.transition[word]

    def start_probabilites(self,word):
        if word not in self.starts:
            return None
        total =0
        for w in self.starts.values():
            total+=w
        return self.starts[word]/total

    def pairProbabilites(self,word,next):
        if word not in self.transition or next not in self.transition[word]:
            return None
        total=0
        for w in self.transition[word].values():
            total+=w
        return self.transition[word][next]/total
    

    def generateNextWord(self, word):
     if word not in self.transition:
        return None

     next_words = list(self.transition[word].keys())
     weights = list(self.transition[word].values())
     #end
     if next_words == []:
         return None

     return random.choices(next_words, weights=weights, k=1)[0] 

    def generateStart(self):
        start = list(self.starts.keys())  
        weight = list(self.starts.values())

        return random.choices(start,weights=weight,k=1)[0]

