#!/usr/bin/python3
for i in reversed(range(123)):
    if (i == 96):
        break
    elif i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
