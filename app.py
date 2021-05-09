from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from Models import Employee, EmployeeSal
import os

app = Flask(__name__)
app.secret_key = "Secret Key"
basedir = os.path.abspath(os.path.dirname(__file__))


# Clean db
@app.route('/employee/deleteAll', methods=['GET', 'POST'])
def delete_all_records():
    Employee.delete_all_records()
    EmployeeSal.delete_all_salary_records()
    # flash("Employee added successfully!!")
    return redirect(url_for('Index'))


# Create a Employee
@app.route('/employee/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    addr = request.form['addr']
    cmpy = request.form['cmpy']
    Employee.add_employee(name, email, addr, cmpy)
    flash("Employee added successfully!!")
    return redirect(url_for('Index'))

# Get All Employee
@app.route('/employees', methods=['GET'])
def get_employees():
    all_employees = Employee.get_all_employees()
    return render_template("index.html", employees=all_employees)

# Get Single Employee
@app.route('/employee/getbyid/<id>', methods=['GET'])
def get_employee(id):
    employee = Employee.exists(id)
    return employee

# Update a Employee
@app.route('/employee/update', methods=['POST'])
def update_employee():
    id = request.form.get('id')
    name = request.form['name']
    email = request.form['email']
    addr = request.form['addr']
    cmpy = request.form['cmpy']

    Employee.update_employee(id, name, email, addr, cmpy)
    flash("Employee Updated Successfully!!")
    return redirect(url_for('Index'))

# Delete Employee
@app.route('/employee/delete/<id>/', methods=['GET', 'POST'])
def delete_employee(id):
    Employee.delete_employee(id)
    if EmployeeSal.exists(id):
        EmployeeSal.delete_employee_salary(id)
    flash("Employee Deleted Successfully!!")
    return redirect(url_for('Index'))
    

# ---------------------------------- Employee Salary REST Code ---------------------------


# Create a Employee Salary
@app.route('/employee/salary/add', methods=['POST'])
def add_emp_salary():
    emp_id = request.form['emp_id']
    salary = request.form['salary']
    currency = request.form['currency']
    pay_type = request.form['pay_type']
    pay_cycle = request.form['pay_cycle']

    if Employee.exists(emp_id):
        EmployeeSal.add_employee_salary(emp_id, salary, currency, pay_type, pay_cycle)
        flash("Employee Salary added successfully!!")
    else:
        flash("Employee Id doesn't exists")
    return redirect(url_for('Index'))

@app.route('/')
def Index():
    all_employees = Employee.get_all_employees()
    print(all_employees)
    all_employees_salaries = EmployeeSal.get_all_employees_salaries()
    return render_template("index.html", employees=all_employees, employees_salary=all_employees_salaries)

# Get All Employee Salaries
@app.route('/employees/salaries', methods=['GET'])
def get_emp_salaries():
    all_emp_salaries = EmployeeSal.get_all_employees_salaries()
    return render_template("index.html", employees_salary=all_emp_salaries)

# Get Single Employee Salary
@app.route('/employee/salary/getbyid/<emp_id>', methods=['GET'])
def get_emp_salary(emp_id):
    employee = EmployeeSal.exists(emp_id)
    return employee

# Update a Employee Salary
@app.route('/employee/salary/update', methods=['POST'])
def update_emp_salary():
    id = request.form.get('id')
    emp_id = request.form['emp_id']
    salary = request.form['salary']
    currency = request.form['currency']
    pay_type = request.form['pay_type']
    pay_cycle = request.form['pay_cycle']
    EmployeeSal.update_employee_salary(id, emp_id, salary, currency, pay_type, pay_cycle)

    flash("Employee Salary Updated Successfully!!")
    return redirect(url_for('Index'))


# Delete Employee Salary
@app.route('/employee/salary/delete/<emp_id>', methods=['GET', 'POST'])
def delete_emp_salary(emp_id):
    EmployeeSal.delete_employee_salary(emp_id)
    flash("Employee Salary Deleted Successfully!!")
    return redirect(url_for('Index'))


# Run Server

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True,use_reloader=True)