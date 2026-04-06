

import re


def valid_email(email):
    pattren = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattren, email) and len(email) > 0:
        return True
    return False

def valid_phone(phone):
    pattren = r'^01[0-9]{9}$'
    if re.match(pattren, phone) and len(phone) > 0:
        return True
    return False

def valid_password(password):
    if len(password) >= 8:
        return True
    return False

def valid_name(name):
    if len(name) > 0 and name.isalpha():
        return True
    return False

def valid_date(date):
    pattren = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattren, date) and len(date) > 0:
        return True
    return False

def valid_amount(amount):
    try:
        amount = float(amount)
        if amount > 0:
            return True
        return False
    except Exception as e:
        return False
    
def valid_empty(data):
    if len(data) > 0 :
        return True
    return False