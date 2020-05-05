
import random


presented = []

lives = 8
nums = ["0","1","2","3","4","5","6","7","8","9"," "]
syms = ["!","£","$","%","^","&","*","(",")","#",",",";",":","@","~","-","*","/","+","{","}","[","]",".",",",">","<","?","/","_","=","'","|",'"',"`","¬","\\"]

def present(steve):
  global presented
  presented = []
  n = (len(correct_list))
  start = 0
  while start < n:
    if (correct_list[start] in guessed_letters):
      presented.append(correct_list[start])
      start +=1
    else:
      presented.append("-")
      start +=1
  print ("".join(presented))


print("H A N G M A N")

Word_List = ['python', 'java', 'kotlin', 'javascript']

y = 0
while y != "exit" or "play":
  print ("""Type "play" to play the game, "exit" to quit:""")
  y = input()
  if y == "play":
    lives = 8
    w = random.choice(Word_List)
    correct_list =[]
    correct_list =[ch for ch in w]
    guessed_letters = set()
    while lives != 0:
      print("")
      present(correct_list)
      if (presented == correct_list):
        print ("You guessed the word!\nYou survived!")
        break
      else:
        x = input("Input a letter:")
        if len(x)>1: #make sure its a single letter and not number.
          print ("You should print a single letter")
        else:
          for ch in x: #make sure its not CAPITAL LETTER
            if x.isupper() or x in syms or x in nums:
              print("It is not an ASCII lowercase letter")
            else:
              if x in guessed_letters:
                print ("You already typed this letter")
              else:
                for ch in x:
                    if x not in correct_list:
                      print ("No such letter in the word")
                      guessed_letters.add(x)
                      lives -=1
                    elif x in guessed_letters:
                      print ("No improvements")
                      lives -=1
                    else:
                      guessed_letters.add(x)
    else:
        print("You are hanged!\n ")
        y = 0 

  else:
    if y == "exit":
      break