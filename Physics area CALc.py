import math

print('Enter your lamina for which the area has to be found')
print('1.Triangle\n2.Square\n3.Circle\n4.Rectangle\n5.Parallelogram\n6.Rhombus\n7.Trapezoid\n8.Ellipse')
ch = int(input('ENTER the no.  '))

if ch == 1:
    base = float(input('Enter the base of the triangle  '))
    height = float(input('Enter the height  '))
    area = 1 / 2 * base * height
    print('AREA OF THE TRIANGLE = ' + str(area))

elif ch == 2:
    side = float(input('Enter the side of the square '))
    area = side * side
    print('AREA OF THE Square = ' + str(area))

elif ch == 3:
    radius = float(input('Enter the radius of the circle '))
    pie = 3.14159265
    area = pie * math.pow(radius, 2)
    print('AREA OF THE Circle = ' + str(area))

elif ch == 4:
    length = float(input('Enter the length of the rectangle '))
    breadth = float(input('Enter the breadth of the rectangle '))
    area = length * breadth
    print('AREA OF THE Rectangle = ' + str(area))

elif ch == 5:
    base = float(input('Enter the base  '))
    height = float(input('Enter the height  '))
    area = base * height
    print('AREA OF THE parallelogram = ' + str(area))

elif ch == 6:
    dia_1 = float(input('Enter one of lengths the diagonal '))
    dia2 = float(input('Enter the second the diagonal '))
    area = 1 / 2 * dia_1 * dia2
    print('AREA OF THE rhombus = ' + str(area))

else:
    print('WRONG choice\n PROGRAM TERMINATES')
