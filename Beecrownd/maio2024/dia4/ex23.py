import math

a,b,c = input().split()

if a != 0 and b != 0 and c != 0:
    a = float(a)
    b = float(b)
    c = float(c)

    delta = math.sqrt((b**2)-(4*a*c))

    r1 = ((b*-1) + delta )/(2*a)
    r2 = ((b*-1) - delta)/(2*a)

    print(f'{r1:.5f}')
    print(f'{r2:.5f}')

else:
    print("Impossivel calcular")


