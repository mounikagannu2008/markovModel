import markovmodel as m
import generate as g
import trainTransitions as train

content1 = open('wsn1.txt','r',encoding="utf-8")
content2 = open('wsn2.txt','r',encoding='utf-8')
files = [content1,content2]
def txtList(file):
   result =[]
   for line in file:
    temp = list(line.split())
    result.append(temp)
   file.close()
   return result

#model..
mymodel = m.markovmodel()
#train..
trainer = train.train(mymodel)
for file in files:
 data = txtList(file)
 trainer.addData(data)
#generate
firstWord = input("enter:\n>")
gen = g.generate(mymodel)
gen.giveLine(firstWord) 