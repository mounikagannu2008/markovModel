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







        