class generate:
    def __init__(self,model:object):
        self.generate = model

    def giveLine(self,start):
        nextWord = self.generate.generateNextWord(start)
        count = 0
        print("__line__\n",start,end=" ")
        while(True):
            count +=1
            if count > 200 or nextWord is None or nextWord == "<EOS>":
                print("_")
                break
            print(nextWord,end=" ")
            temp = nextWord
            nextWord = self.generate.generateNextWord(temp)
    def giveSecondLine(self):
        start = self.generate.generateSecondStart()
        nextWord = self.generate.generateSecondNextWord(start[0],start[1])
        count = 0
        temp=start[1]
        temp1=nextWord 
        print("==2nd markov==")
        print(start[0].strip(), start[1].strip(), end=" ")
        
        while True:
            count+=1
            if count>200 or nextWord is None or nextWord == "<EOS>":
                print("_")
                break
            print(nextWord,end=" ")
            nextWord = self.generate.generateSecondNextWord(temp,temp1)
            temp = temp1
            temp1 = nextWord


    def fromStart(self):
        start =self.generate.generateStart()
        self.giveLine(start)
