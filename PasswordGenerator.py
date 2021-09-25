#Programmer : MrDaRkFoRcE
#Telegram : @ThE_DaRkFoRcE

import random
counter = 0
password = ""
while True:
      number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

      capitalletter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

      Lowercaseletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

      special = ['!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

      randompass1 = random.choice(number)
      randompass2 = random.choice(capitalletter)
      randompass3 = random.choice(Lowercaseletters)
      randompass4 = random.choice(special)
      
      temp_pass = randompass1 + randompass2 + randompass3 + randompass4
      password = password + temp_pass
      counter+=4

      if counter == 12:
            print(password)
            break
      else :
            continue
