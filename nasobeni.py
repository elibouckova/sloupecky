import random
import time

def priklad():
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    print("Kolik je " + str(a) + " * " + str(b) + "?")
    tip = input()

    if int(tip) == a*b :
        print("spravne")
        return 1
    else :
        print("Odpoved mela byt: " + str(a*b))
        return 0

pocet = 0
celkem = 0
t0= time.time()

for i in range(23):
    pocet = pocet + priklad()
    celkem = celkem + 1
    
t1 = time.time() - t0    
print("Spravne vypocteno: " + str(pocet) + " z " + str(celkem))
print("Time elapsed(s): ", t1) # CPU seconds elapsed (floating point)
print("Time elapsed(m): ", str(t1/60)) # CPU seconds elapsed (floating point)
