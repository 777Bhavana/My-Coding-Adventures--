print('temperature convertor')
print(' what to what do you want to convert')
print(' C to K \n K to C \n F to C \n C to F \n F to K \n K to F \n')
print('Enter your Choice in')
choice = int(input())
if (choice == 1):
    print('enter for Celsius')
    C = float(input())
    K = C + 273.15
    print('you answer in Kelvin =' + str(K))
elif (choice == 2):
    print('enter for kelvin')
    K = float(input())
    C = K - 273.15
    print('your answer in Celsius =' + str(C))
elif (choice == 3):
    print('Enter for Fabricate')
    F = float(input())
    C = (F - 32) * 5 / 9
    print('your answer in Celsius =' + str(C))
elif (choice == 4):
    print('enter for Celsius')
    C = float(input())
    F = C * (9 / 5) + 32
    print('your answer in fabricates')
elif (choice == 5):
    print('Enter for Fabricate')
    F = float(input())
    K = (F - 32) * 5 / 9 + 273.15
    print('your answer in kelvin =' + str(K))
elif (choice == 6):
    print('enter for kelvin')
    K = float(input())
    F = (K - 273.15) * 9 / 5 + 32
    print('your answer in fabric =' + str(F))
else:
    print('you have entered the wrong option')
    exit()
