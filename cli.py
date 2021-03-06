from os import system
from access_db import *
system('echo off')
def clearScreen():
    system('cls')

def help():
    print("""
You may use the following commands:
    help
    add [id] [first name] [last name] [hire year]
    find [id]
    update [id] [first name] [last name] [hire year]
    delete [id]
    quit / q
    """)

clearScreen()

names = []
looping = True
while looping:
    value = input('>:c ')
    list_input = value.split(' ')
    lower = list_input[0].lower()

    if lower == 'help':
        help()

    elif lower == 'quit' or lower == 'q':
        looping = False

    elif lower in ['add','update']:
        if len(list_input) == 5:
            del list_input[0]
            try:
                list_input[0] = int(list_input[0])
                list_input[3] = int(list_input[3])
                if lower == 'add':
                    createEmployee(list_input)
                    print(f'Employee has been successfully created')
                elif lower == 'update':
                    if updateEmployee(list_input):
                        print(f'Employee {list_input[0]} has been successfully updated')
                    else:
                        print(f'We could not find an Employee with ID: {list_input[0]}')
            except:
                print('Invalid values, ID and Hire Year must be a numeric value')
        else:
            print(f"format:: {lower} [id] [first name] [last name] [hire year]")

    elif lower in ['find', 'delete']:
        if len(list_input) == 2:
            id = list_input[1]
            try:
                id = int(id)
                if lower == 'find':
                    employee = findEmployee(id)
                    if employee:
                        print(employee)
                    else:
                        print("We could not find that employee")
                elif lower == 'delete':
                    if deleteEmployee(id):
                        print(f'Employee {id} has been successfully removed')
                    else:
                        print(f'Employee {id} could not be found')
            except:
                print(f'format:: {lower} [(whole number)]')

    else:
        print('That command is not recognized, use [help] to see available commands')

print('bye :c')
system('echo on')
exit()
