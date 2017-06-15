import random
# Let's start with the area code. No leading zero, so only pick between 1
# and 9. Then the remaining two can be anything between 00 and 99.


def makeFirst():
    first_digit = random.randint(1, 9)
    remaining = random.randint(0, 99)
    return first_digit * 100 + remaining
# Next the middle numbers. They cannot have a 9 so sample 0 to 8. Then
# loop until you get a valid case, throwing out if you happen to sample a
# 000.


def makeSecond():
    middle = 0
    while middle == 0:
        middle1 = random.randint(0, 8)
        middle2 = random.randint(0, 8)
        middle3 = random.randint(0, 8)
        middle = 100 * middle1 + 10 * middle2 + middle3
    return middle
# For the last four numbers, we'll use random.sample to ensure that we
# don't get any repeats.


def makeLast():
    return ''.join(map(str, random.sample(range(10), 4)))
# Finally join the whole thing together and format it like a phone number.


def makePhone():
    first = makeFirst()
    second = makeSecond()
    last = makeLast()
    return '{}{}{}'.format(first, second, last)
# A few tests


def cnp():
    string = ""
    for i in range(13):
        string += str(random.randint(0, 9))
    return string


for i in range(20):
    print cnp()
