'''
1.  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 between 2000 and 3200 (both included).The numbers obtained should be printed in a
 comma-separated sequence on a single line.
'''

def all_numbers():
    lst = []
    for i in range(2000,3201):
        n = str(i)
        if i%7 == 0:
            if i%5!=0:
                lst.append(n)
    print(",".join(lst))

'''
2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
'''

def reverse_name():
    first_name = input("Enter first name")
    last_name = input("Enter last name")
    first_name = first_name[::-1]
    last_name = last_name[::-1]
    print(first_name+" "+last_name)

'''
3. Write a Python program to find the volume of a sphere with diameter 12 cm.
'''

def vol_sphere():
    diameter = 12
    radius = diameter/2
    volume = (4/3)*3.14*(radius**3)
    print(volume)


if __name__ == '__main__':
    all_numbers()
    reverse_name()
    vol_sphere()