import pytest
from Models import EmployeeSal

def test_add_employee_sal():
    # Arrange
    employee_sal = EmployeeSal
    emp_id = '1'
    salary = '5000'
    currency = 'Dollar'
    pay_type = 'Saving'
    pay_cycle = "Bi-weekly"
    # Act
    employee_sal.add_employee_salary(emp_id, salary, currency, pay_type, pay_cycle)
    actual = employee_sal.get_all_employees_salaries()

    # Assert
    assert len(actual)==1

def test_delete_employee_sal():
    # Arrange
    employee_sal = EmployeeSal
    emp_id = '1'
    salary = '5000'
    currency = 'Dollar'
    pay_type = 'Saving'
    pay_cycle = "Bi-weekly"

    # Act
    employee_sal.add_employee_salary(emp_id, salary, currency, pay_type, pay_cycle)
    employee_sal.delete_all_salary_records()
    actual = employee_sal.get_all_employees_salaries()
    # Assert
    assert len(actual)==0