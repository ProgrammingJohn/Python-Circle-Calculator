import math
import time

PII = math.pi
PI = math.pi
sqrt = math.sqrt
sleep = time.sleep

print('Welcome to The Circle Calculator! || made by: John Exterkamp')
print('----------------------------------')


def Run():
    global Radius, Diameter, Circumference
    while True:
        PA = input('Would you like to use PI or 3.14| Type PI or 3 --> ')
        if PA == '3':
            PI = 3.14
            break

        if PA == 'PI':
            PI = math.pi
            break

    print('what is the known piece of information?')
    print('what is the known piece of information r=radius, d=diameter, a=area, c=circumference.')
    while True:
        mode = input('what is the information? type here --> ')
        if mode == 'a':
            Area = input('what does area = ')
            break
        else:
            Area = 'N'
        if mode == 'd':
            Diameter = input('what does diameter = ')
            break
        else:
            Diameter = 'N'
        if mode == 'r':
            Radius = input('what does radius = ')
            break
        else:
            Radius = 'N'
        if mode == 'c':
            Circumference = input('what does circumference = ')
            break
        else:
            Circumference = 'N'
        if mode != 'a' and 'd' and 'a' and 'c':
            pass
    print('----------------------------------')
    if Area == 'N':
        pass
    else:
        while True:
            try:
                int(Area)
                Area = int(Area)
                break
            except ValueError:
                try:
                    float(Area)
                    Area = float(Area)
                    break
                except ValueError:
                    Area = input('I\'m sorry but area does not seem to be a int or float please re-enter here --> ')
    if Radius == 'N':
        pass
    else:
        while True:
            try:
                int(Radius)
                Radius = int(Radius)
                break
            except ValueError:
                try:
                    float(Radius)
                    Radius = float(Radius)
                    break
                except ValueError:
                    Radius = input('I\'m sorry but radius does not seem to be a int or float please re-enter here --> ')
    if Diameter == 'N':
        pass
    else:
        while True:
            try:
                int(Diameter)
                Diameter = int(Diameter)
                break
            except ValueError:
                try:
                    float(Diameter)
                    Diameter = float(Diameter)
                    break
                except ValueError:
                    Diameter = input(
                        'I\'m sorry but diameter does not seem to be a int or float please re-enter here --> ')
    if Circumference == 'N':
        pass
    else:
        while True:
            try:
                int(Circumference)
                Circumference = int(Circumference)
                break
            except ValueError:
                try:
                    float(Circumference)
                    Circumference = float(Circumference)
                    break
                except ValueError:
                    Circumference = input(
                        'I\'m sorry but circumference does not seem to be a int or float please re-enter here --> ')
    print('----------------------------------')
    try:
        if int(Radius):
            Diameter = Radius * 2
            Area = PI * Radius ** 2
            Circumference = 2 * PI * Radius
    except ValueError:
        try:
            if int(Diameter):
                Radius = Diameter / 2
                Circumference = PI * Diameter
                Area = PI * Radius ** 2
        except ValueError:
            try:
                if int(Area):
                    Radius = sqrt(Area / PI)
                    Diameter = 2 * sqrt(Area / PI)
                    Circumference = 2 * PI * Radius
            except ValueError:
                try:
                    if int(Circumference):
                        Diameter = Circumference / PI
                        Radius = Diameter / 2
                        Area = PI * Radius ** 2
                except ValueError:
                    pass

    Area1 = Area / PII
    Circumference1 = Circumference / PII

    print('Radius is ', Radius)
    print('Diameter is ', Diameter)
    print('Area is ', Area, '/ ', Area1, 'π')
    print('Circumference is ', Circumference, '/ ', Circumference1, 'π')
    print('----------------------------------')
    print('Rerunning!')
    sleep(2)


while True:
    Run()