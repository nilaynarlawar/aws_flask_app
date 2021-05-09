import pytest
import requests

from pytest_bdd import scenarios, when, then, given

CALLING_CODE_API = "http://127.0.0.1:5000/"

scenarios('../feature/employee_salary.feature',
          example_converters=dict(employee_details=str, employee_salary_details=str, emp_id=str))


@given('Employee and Employee Salary table is empty')
def empty_table():
    response = requests.post(CALLING_CODE_API + '/employee/deleteAll')
    assert response.status_code == 200


@given('the Employee add API is queried with "<employee_details>"')
def create_employee_response(employee_details):
    data_list = [x.strip() for x in employee_details.split(',')]
    get_empres = requests.get(CALLING_CODE_API + '/employee/getbyid/1')
    if get_empres.content.decode('utf-8').encode('unicode_escape').decode() == '{}\\n':
        data = {'name': data_list[0],
                'email': data_list[1],
                'addr': data_list[2],
                'cmpy': data_list[3]}
        response = requests.post(CALLING_CODE_API + '/employee/add', data=data)
        return response
    return get_empres


@pytest.fixture
@when('the Employee salary add API is queried with "<employee_salary_details>"')
def create_employee_salary_response(employee_salary_details):
    data_list = [x.strip() for x in employee_salary_details.split(',')]
    get_empres = requests.get(CALLING_CODE_API + '/employee/salary/getbyid/1')
    if get_empres.content.decode('utf-8').encode('unicode_escape').decode() == '{}\\n':
        data = {'emp_id': data_list[0],
                'salary': data_list[1],
                'currency': data_list[2],
                'pay_type': data_list[3],
                'pay_cycle': data_list[4]}
        response = requests.post(CALLING_CODE_API + '/employee/salary/add', data=data)
        return response
    return get_empres

@pytest.fixture
@when('the Employee salary delete API is queried with "<emp_id>"')
def delete_employee_salary_response(emp_id):
    get_empres = requests.get(CALLING_CODE_API + '/employee/salary/getbyid/' + emp_id)
    if get_empres.content.decode('utf-8').encode('unicode_escape').decode() == '{}\\n':
        get_empres = requests.post(CALLING_CODE_API + '/employee/salary/delete/' + emp_id)
        return get_empres
    return get_empres


@then('the response status code is 200')
def response_code(create_employee_salary_response):
    assert create_employee_salary_response.status_code == 200


@then('the response status code for delete is 200')
def response_code(delete_employee_salary_response):
    assert delete_employee_salary_response.status_code == 200
