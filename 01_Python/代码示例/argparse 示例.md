### argparse
 argparse example
```python
#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2021-01-10 10:50:27


import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")

    parser.add_argument("num", help="The fibonacci number you wish to calculate.", type=int)
    parser.add_argument('-o', "--output", help="Output result to a file", action="store_true")
    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("The " + str(args.num) + "th fib number is " + str(result))
    elif args.quite:
        print(result)
    else:
        print("fib(" + str(args.num) + ") =" + str(result))

    if args.output:
        f = open("fib.txt", "a")
        f.write(str(result) + "\n")


if __name__ == '__main__':
    main()
```
