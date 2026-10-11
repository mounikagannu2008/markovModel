from markovmodel import markovmodel as m
from generate import generate as g
from trainTransitions import train 

content1 = open('C:/Users/DELL/markonikavs/shakespeare/input.txt','r',encoding="utf-8")
def txtList(file):
   result =[]
   for line in file:
    temp = list(line.split())
    result.append(temp)
   file.close()
   return result

#model..
mymodel = m()
#train..
trainer = train(mymodel)
data = txtList(content1)
trainer.addData(data)
trainer.addSecondData(data)
#generate
gen = g(mymodel)
while(True):
 print("1.give1stWord\n2.noStartNeeded\n3.SecondMarkov\n4.exit")
 choice = int(input("enter ur choice"))
 #getting start
 if (choice==1):
  rec = int(input("NEED TOP FREQUENCY WORDS:\n if yes enter 1"))
  if (rec == 1):
   re = mymodel.givefive()
   print(re)
  firstWord = input("enter:\n>")
  print("-"*20)
  gen.giveLine(firstWord)
  print("-"*20)
 elif(choice == 2):
  print("-"*20)
  gen.fromStart() 
  print("-"*20)
 elif(choice == 3):
    gen.giveSecondLine()
 elif(choice == 4):
  print("i hope u had fun with this thing")
  print("[> <]")
  break
 else:
  print("enter valid number")