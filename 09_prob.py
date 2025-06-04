'''

* * *        for n = 3
*   *
* * *

'''

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if (i == 1 or i == n):  # for first and last line
        print("*" * n)
    else:                    # for middle lines
        print("*" + " " * (n - 2) + "*")


  