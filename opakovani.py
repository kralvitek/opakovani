import random 

pole=[]
pole1=[]

for i in range(random.randint(1,10)):
        pole.append(random.randint(1,10))
print(pole)

for i in range(random.randint(1,10)):
        pole1.append(random.randint(1,10))
print(pole1)

if len(pole) > len(pole1):
    print("pole je větší než pole1 ")
elif len(pole1) < len(pole):
    print("pole1 je větší než pole")
else: 
    print("jsou oba stejný")

