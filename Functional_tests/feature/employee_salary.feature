Feature: Employee salary CRUD Operation

    Want to test the Create, Update, Delete, Read functionality

    Scenario Outline: Adding Employee Salary
        Given Employee and Employee Salary table is empty
        And the Employee add API is queried with "<employee_details>"
        When the Employee salary add API is queried with "<employee_salary_details>"
        Then the response status code is 200
        Examples:
            | employee_details                        | employee_salary_details                |
            | bob,bob@gmail.com,California-USA,Google | 1,450000,dollar,saving_account,monthly |

    Scenario Outline: Delete existing Employee salary
        Given Employee and Employee Salary table is empty
        And the Employee add API is queried with "<employee_details>"
        When the Employee salary add API is queried with "<employee_salary_details>"
        And the Employee salary delete API is queried with "<emp_id>"
        Then the response status code for delete is 200
        Examples:
            | employee_details                        | employee_salary_details                | emp_id |
            | bob,bob@gmail.com,California-USA,Google | 1,450000,dollar,saving_account,monthly | 1      |