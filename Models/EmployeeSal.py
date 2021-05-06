
emp_sal_map = {}
id = 0

def delete_all_records():
    emp_map.clear()

def add_employee_salary(emp_id, salary, currency, pay_type, pay_cycle):
    id = id + 1
    emp_sal_list = {"id": id,
                    "emp_id": emp_id,
                    "salary": salary,
                    "currency": currency,
                    "pay_type": pay_type,
                    "pay_cycle": pay_cycle}
    emp_sal_map[id] = emp_sal_list
    return True

def get_all_employees_salaries():
    return emp_sal_map.values()

