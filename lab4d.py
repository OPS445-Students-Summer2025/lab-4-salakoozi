#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50




def first_five(string):
    # Place code here - refer to function specifics in section below
    five = string[0:5]
    return five

def last_seven(string):
    # Place code here - refer to function specifics in section below
    seven = string[-7:]
    return seven

def middle_number(number):
    # Place code here - refer to function specifics in section below
    string = str(number)
    index = string[1:3]
    return index
 
def first_three_last_three(str1,str2):
    # Place code here - refer to function specifics in section below
    f3l3 = str1[:3] + str2[-3:]
    return f3l3

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))