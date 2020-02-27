import math
import time

PI = math.pi
sqrt = math.sqrt
sleep = time.sleep

print('Welcome to The Circle Calculator! || made by: John Exterkamp')
print('----------------------------------')

while True:
    PA = input('Would you like to use PI or just 3.14 | Type PI or 3.14 --> ')
    if PA == '3.14':
        PI = 3.14
        break

    if PA == 'PI':
        PI = math.pi
        break

while True:
    Area = input('What is the area of the circle if unknown type N ? Type here --> ')
    Radius = input('What is the radius of the circle if unknown type N ? Type here --> ')
    Diameter = input('What is the diameter of the circle if unknown type N ? Type here --> ')
    Circumference = input('What is the circumference of the circle if unknown type N ? Type here --> ')
    node = [Area, Radius, Diameter, Circumference]

    if not 'N' in node:
        print('nothing needs to be solved or you answers are not numbers please try again?!')
    else:
        break
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
                radius = input('I\'m sorry but radius does not seem to be a int or float please re-enter here --> ')
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
                Diameter = input('I\'m sorry but diameter does not seem to be a int or float please re-enter here --> ')
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
                Circumference = input('I\'m sorry but circumference does not seem to be a int or float please re-enter here --> ')
print('----------------------------------')
print('calculating...')
sleep(1)
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
                    Radius = Circumference / 2 * PI
                    Diameter = Circumference / PI
                    Area = PI * Radius ** 2
            except ValueError:
                pass


print('Radius is ', Radius)
print('Diameter is ', Diameter)
print('Area is ', Area)
print('Circumference is ', Circumference)
print('----------------------------------')