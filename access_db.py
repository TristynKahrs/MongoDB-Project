import pymongo, os, sys, pickle

class Employee():
    def __init__(self, id, firstName, lastName, hireYear):
        self.id = int(id)
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        self.hireYear = int(hireYear)

    def __str__(self):
        return f'{self.id} - {self.firstName} {self.lastName} - {self.hireYear}'

def getDatabase(db, collection):
    #Getting acces to the localhost Mongodb
    local_db_connect = pymongo.MongoClient('mongodb://localhost:27017/')
    db_names = local_db_connect.list_database_names()

    if db in db_names:
        db = local_db_connect[db]

        return db[collection]
    else:
        new_db = local_db_connect[db]
        new_collection = new_db[collection]
        #This Throw Away Info is needed in order to actually create
        #a new database on the localhost of it does not exist.
        throw_away_info = {'New': 'DB'}
        new_collection.insert_one(throw_away_info)
        new_collection.delete_one(throw_away_info)
        getDatabase(db, collection)

def createEmployee(employeeInfo):
    employees = getDatabase('Employee_DB', 'Employees')
    all_employee_ids = []

    try:
        for employee in employees.find():
            all_employee_ids.append(employee["_id"])

        if len(all_employee_ids) == 0:
            new_id = employeeInfo[0]
        else:
            if employeeInfo[0] in all_employee_ids:
                new_id = max(all_employee_ids) + 1
            else:
                new_id = employeeInfo[0]

        new_employee = {'_id': new_id, 'fname': employeeInfo[1], 'lname':employeeInfo[2], 'hireYear':employeeInfo[3]}
        employees.insert_one(new_employee)
    except:
        createEmployee(employeeInfo)

def findEmployee(employeeId):
    employees = getDatabase('Employee_DB', 'Employees')

    for employee in employees.find():
        if employeeId == employee['_id']:
            return Employee(employee['_id'], employee['fname'], employee['lname'], employee['hireYear'])

    return False

def deleteEmployee(employeeId):
    employees = getDatabase('Employee_DB', 'Employees')

    for employee in employees.find():
        if employeeId == employee['_id']:
            employees.delete_one({'_id':employeeId})
            return True

    return False

def updateEmployee(employeeInfo):
    employees =  getDatabase('Employee_DB', 'Employees')

    for employee in employees.find():
        if employeeInfo[0] == employee['_id']:
            myQuery = {'_id': employee['_id']}

            i = 0
            while i < 3:

                if i == 0:
                    key = 'fname'
                elif i == 1:
                    key = 'lname'
                else:
                    key = 'hireYear'
                newQuery = {'$set':{key: employeeInfo[i + 1]}}

                employees.find_one_and_update(myQuery, newQuery)
                i += 1

            return True

    return False

def importAllEmployees(path):
    files = os.listdir(path)
    all_employees = dict()
    for ser_file in files:
        employeeInfo = []
        with open(path + ser_file, 'rb') as file:
            all_employees[int(ser_file.replace('.ser', ''))] = pickle.load(file)

        employeeInfo.append(all_employees[int(ser_file.replace('.ser', ''))].id)
        employeeInfo.append(all_employees[int(ser_file.replace('.ser', ''))].firstName)
        employeeInfo.append(all_employees[int(ser_file.replace('.ser', ''))].lastName)
        employeeInfo.append(all_employees[int(ser_file.replace('.ser', ''))].hireYear)

        print(employeeInfo)
        createEmployee(employeeInfo)

#importAllEmployees('Assignment 1 - data/people/long serialized/')

if __name__ == '__main__':
    print(findEmployee(10000))
