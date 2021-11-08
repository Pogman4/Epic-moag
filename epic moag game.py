import random
b = 0
while b < 3:
 a = random.randint(1,3)
 print("anyone sus")
 answer = input()
 if (a == 1):
    print(answer + " " "was the Impostor")
    print("YOU WIN")
    b = 10
 if (a > 1):
    print(answer + " " "was not the Impostor")
    b = b+1
    a=0
 if (b == 3):
    print("you lost")
