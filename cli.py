from os import system
# from access_db import *
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
            if lower == 'add':
                # createEmployee(list_input)
                # print(f'Employee {id} has been successfully created')
                pass
            elif lower == 'update':
                pass
                # updateEmployee(list_input)
        else:
            print("format:: add [id] [first name] [last name] [hire year]")

    elif lower in ['find', 'delete']:
        if len(list_input) == 2:
            id = list_input[1]
            try:
                id = int(id)
                if lower == 'find':
                    # employee = findEmployee(id)
                    # if employee == False:
                    #     print("We could not find that employee")
                    # else:
                    #     print(employee)
                    pass
                elif lower == 'delete':
                    # if deleteEmployee(id):
                    #     print(f'Employee {id} has been successfully removed')
                    # else:
                    #     print(f'Employee {id} could not be found')
                    pass
            except:
                print(f'format:: {lower} [(whole number)]')

    else:
        print('That command is not recognized, use [help] to see available commands')

print('bye')
exit()
