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
@app.route('/employee/add', methods=['GET','POST'])
def add_employee():
    """
    name = request.args.get('name')
    email = request.args.get('email')
    addr = request.args.get('addr')
    cmpy = request.args.get('cmpy')
    Employee.add_employee(name, email, addr, cmpy)
    flash("Employee added successfully!!")
    return {"Status" : 200}
    """
    if request.method == 'GET':
        return {"Status": 200}
    if request.method == 'POST':
        print('post')
        return {"Status": 300}


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
    # print(all_employees_salaries)
    return render_template("index.html", employees=all_employees, employees_salary=all_employees_salaries)

# Run Server

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True,use_reloader=True)