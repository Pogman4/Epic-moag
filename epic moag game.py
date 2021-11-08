import random
b = 0
while b < 3:
 a = random.randint(1,2)
 print("anyone sus")
 answer = input()
 if (a == 1):
    print(answer + " " "was the Impostor")
    print("YOU WIN")
    b = 3
 if (a == 2):
    print(answer + " " "was not the Impostor")
    b + 1
    a=0
