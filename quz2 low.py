import random
x=input("yo choom vad heter du type shit?\n ")
print(f"tjenare {x} välkommen till mitt program eller något. ")
z=random.randint(1,10)
cc=int(input("välj ett tal 1 till 10\n "))
if cc>z:
    print("mellan 1 och 10 ditt retard ")
while cc!=z:
    i=0
    print("försök igen")
    cc=int(input("välj ett tal 1 till 10\n "))
    i=i+1 
    if i==3:
        print("du använde alla försök")
        break
if cc==z:
    print(" rätt type shit")

    