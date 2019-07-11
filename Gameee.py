import random
name=input("Hello!Enter your name:")
print(name)
print("Well {} ,I am thinking of a number between  1 and 10.")
k=random.randint(1,10)
i=0
while i<5:
    r=int (input("Take a guess:"))
    if r==k :
        print("WIN")
        break
    elif r>k :
        print("Too High")
    else:
        print("Too Low")
    i=i+1
