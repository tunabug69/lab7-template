#!/usr/bin/env python3
# Student ID: [rsrrajapaksha]

def function1():
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

# Initialize the global variable
schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)

# Call function1() and check the global variable
function1()
print('print() in main on schoolName:', schoolName)

# Call function2() and check the global variable
function2()
print('print() in main on schoolName:', schoolName)
