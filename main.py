import markovmodel as m
import generate as g
import trainTransitions as train
import time

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
gen = g.generate(mymodel)
while(True):
 print("1.give1stWord\n2.noStartNeeded\n3.SecondMarkov\n4.exit")
 choice = int(input("enter ur choice"))
 #getting start
 if (choice==1):
  firstWord = input("enter:\n>")
  gen.giveLine(firstWord)
 elif(choice == 2):
  gen.fromStart() 
 elif(choice == 3):
  gen.giveSecondLine()
 elif(choice == 4):
  print("i hope u had fun with this thing")
  print("[> <]")
  break
 else:
  print("enter valid number")