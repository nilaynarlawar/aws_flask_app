import pytest
from Models import Employee

def test_add_employee():
    # Arrange
    employee = Employee
    name = 'bob'
    email = 'bob@gmail.com'
    addr = 'USA'
    cmpy = 'Google'

    # Act
    employee.add_employee(name, email, addr, cmpy)
    actual = employee.get_all_employees()

    # Assert
    assert len(actual)==1

def test_delete_employee():
    # Arrange
    employee = Employee
    name = 'bob'
    email = 'bob@gmail.com'
    addr = 'USA'
    cmpy = 'Google'

    # Act
    employee.add_employee(name, email, addr, cmpy)
    employee.delete_all_records()
    actual = employee.get_all_employees()
    # Assert
    assert len(actual)==0