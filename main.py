year = int(input('Enter  year: '))

if (year % 400 == 0) and (year % 100 == 0):
    print('the is leap year(366 days)')

elif (year % 4 == 0) and (year % 100 == 0):
    print('the year is a leap year(366 days)')
else:
    print(" is not a leap year (365 days)")

    print("************************")

length_1 = int(input('Enter your length: '))
print(length_1)

if length_1 > 170 or length_1 == 170:
   print("tall")

if length_1 < 170 and length_1 > 160:
    print("normal")

if length_1 < 150:
    print("short")


