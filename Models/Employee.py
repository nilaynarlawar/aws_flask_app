import uuid

emp_map = {}

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

def exists(id):
    """Returns true if the provided Emp ID exists"""
    return (id in emp_map)

def update_employee(id, name, email, addr, cmpy):
    """Update employee """
    if exists(id):
        value = emp_map.get(id)
        value['name'] = name
        value['email'] = email
        value['addr'] = addr
        value['cmpy'] = cmpy
        return True

def delete_employee(id):
    """Delete employee """
    if exists(id):
        del emp_map[id]
        return True

def delete_all_records():
    """Delete records """
    emp_map.clear()
    return True
