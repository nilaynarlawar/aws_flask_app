Feature: Employee CRUD Operation
    Want to test the Create, Update, Delete, Read functionality

    Scenario Outline: Adding New Employee
        Given Employee and Employee Salary table is empty
        When the Employee add API is queried with "<employee_details>"
        Then the response status code is 200
        Examples:
            |  employee_details                         |
            |  bob,bob@gmail.com,California-USA,Google  |

    Scenario Outline: Delete existing Employee
        Given Employee and Employee Salary table is empty
        When the Employee add API is queried with "<employee_details>"
        And the Employee delete API is queried with "<emp_id>"
        Then the response status code for delete is 200
        Examples:
            | employee_details                        | emp_id |
            | bob,bob@gmail.com,California-USA,Google | 1      |




    
         