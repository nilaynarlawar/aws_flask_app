import uuid

emp_sal_map = {}



def add_employee_salary(emp_id, salary, currency, pay_type, pay_cycle):
    id = str(uuid.uuid4()).split('-')[0]
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

def exists(emp_id):
    """Returns true if the provided Emp ID exists"""
    for key in emp_sal_map:
        value = emp_sal_map.get(key)
        if value['emp_id'] == emp_id:
            return True

def update_employee_salary(id, emp_id, salary, currency, pay_type, pay_cycle):
    """Update employee """
    if exists(emp_id):
        value = emp_sal_map.get(id)
        value['salary'] = salary
        value['currency'] = currency
        value['pay_type'] = pay_type
        value['pay_cycle'] = pay_cycle
        return True

def delete_employee_salary(emp_id):
    """Delete employee salary """
    if exists(emp_id):
        for key in emp_sal_map:
            value = emp_sal_map.get(key)
            if value['emp_id'] == emp_id:
                del emp_sal_map[key]
                return True

def delete_all_salary_records():
    emp_sal_map.clear()
    return True

