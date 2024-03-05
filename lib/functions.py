#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print("Hello, {}!".format(name))

greet("Alice")


def greet_with_default(name="programmer"):
    print("Hello, {}!".format(name))

greet_with_default("James")

greet_with_default()

def add(num1, num2):
    return num1 + num2 

result = add(45, 55)
print(result)

def halve(number):
    return number / 2

result = halve(10)
print(result)
