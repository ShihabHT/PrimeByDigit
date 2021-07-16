from math import sqrt
from termcolor import colored
import time

maxLength = 7

while True:
    digitLength = int(input("Enter the length of the prime number you want to find\n"))
    if maxLength >= digitLength > 0:
        break
    else:
        print("The maximum length can be no longer than ", maxLength, "and at least 1")
        continue

createNumber = '1'

for x in range(1, digitLength):
    # print(createNumber)
    # print(type(createNumber))
    createNumber = createNumber + "0"

checkNumber = int(createNumber) + 1

# print(check_number)
# print(type(check_number))
# start_from = 3

count = 0
if digitLength == 1:
    print("Of", digitLength, "digit, right?\n" + "Ok, here you go.... \n")
    for this in range(1, 10):
        if this > 1:
            for startFrom in range(2, this):
                if this % startFrom == 0:
                    print(this, "is not prime")
                    break
            else:
                print(colored(str(this) + " is prime", 'red', on_color=None, attrs=['bold', 'reverse']))
                count += 1
    print()
    print(colored("There are "+str(count) + " prime numbers of " + str(digitLength) + " digit",
                  'green', attrs=['bold', 'reverse']))
    exit()


print("Of", digitLength, "digits, right?\n"+"Ok, here you go.... \n")


def whether_prime(check_number):
    for start_from in range(3, int(sqrt(check_number)) + 1, 2):
        if check_number % start_from == 0:
            return 0
    else:
        return 1


t0 = time.time()


while len(str(checkNumber)) <= digitLength:
    if str(checkNumber)[-1] != '5':
        result = whether_prime(checkNumber)
        if result == 0:
            # pass
            print(checkNumber, "is not prime")
        elif result == 1:
            print(colored(str(checkNumber) + " is prime", 'red', on_color=None, attrs=['bold', 'reverse']))
            count += 1

        checkNumber += 2
    else:
        checkNumber += 2

print()
print(colored("There are "+str(count) + " prime numbers of " + str(digitLength) + " digits",
              'green', attrs=['bold', 'reverse']))
t1 = time.time()
print("time.time in seconds", t1-t0)
