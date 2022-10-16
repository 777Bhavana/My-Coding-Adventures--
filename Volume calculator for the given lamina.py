import math

print('Enter your lamina')
print('while entering the values of base , radius .height ext.. please do enter in SI units only')
print('Enter 1.cube\n2.cylinder\n3.cuboid\n4.sphere\n5.cone\n6.pyramid\n ')
ch = int(input())
if ch == 1:
    length = float(input('Enter the length of the side of the cube    '))
    volume = math.pow(length, 3)
    print('volume of the cube = ' + str(volume))

elif ch == 2:
    radius = float(input('enter the radius of the cylinder  '))
    height = float(input('enter the height of the cylinder  '))
    pi = 3.14159265
    volume = pi * (radius * 2) * height
    print('volume of your cylinder = ' + str(volume))

elif ch == 3:
    length = float(input('Enter the length     '))
    width = float(input('Enter the width    '))
    height = float(input('Enter the height '))
    volume = length * width * height
    print('volume of the cuboid = ' + str(volume))

elif ch == 4:
    radius = float(input('enter the radius of the sphere  '))
    pi = 3.14159265
    volume = (4 * pi * (radius * 3)) / 3
    print('Volume of the sphere  = ' + str(volume))

elif ch == 5:
    height = float(input('Enter the height '))
    radius = float(input('enter the radius of the cone  '))
    pi = 3.14159265
    volume = (pi * (radius * 2) * height) / 3
    print('Volume of cone = ' + str(volume))

elif ch == 6:
    base = float(input('Enter the base'))
    height = float(input('Enter the height '))
    Volume = (base * height) / 3
    print('the volume of the pyramid ='+str(Volume))
else:
    print('You have entered the wrong option \n the program terminates \n bye!!!!!!!!!!!!!')
    exit(0)
