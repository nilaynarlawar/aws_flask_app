import uuid

emp_map = {}
emp_count = 0

def delete_all_records():
    emp_map.clear()

def add_employee(name, email, addr, cmpy):
    emp_id = str(uuid.uuid4()).split('-')[0]
    emp_list = {"id": emp_id,
                "name": name,
                "email": email,
                "addr":  addr,
                "cmpy": cmpy}
    emp_map[emp_id] = emp_list
    return True

def get_all_employees():
    return emp_map.values()