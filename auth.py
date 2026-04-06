from db import read_data, write_data
from validation import valid_email, valid_phone, valid_password, valid_name
data = read_data()

def login():
    print("\n------------------------Login------------------------")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    for user in data['users']:
        if user['email'] == email and user['password'] == password:
            print("\n\nLogin successful!")
            return user
    
    print("\n\nInvalid email or password.")
    return None


def register():
    print("\n------------------------Register------------------------")

    first_name = input("First name: ").strip()

    if not valid_name(first_name):
        print("\n\nInvalid first name")
        return
    
    last_name = input("Last name: ").strip()

    if not valid_name(last_name):
        print("\n\nInvalid last name")
        return
    
    email = input("Email: ").strip()

    if not valid_email(email):
        print("\n\nInvalid email")
        return

    for u in data["users"]:
        if u["email"] == email:
            print("\n\nEmail already exists")
            return

    password = input("Password: ").strip()
    if not valid_password(password):
        print("\n\nPassword must be at least 8 characters")
        return
    
    confirm_password = input("Confirm password: ").strip()

    if password != confirm_password:
        print("\n\nPassword does not match")
        return

    phone = input("Phone: ").strip()
    if not valid_phone(phone):
        print("\n\nInvalid phone number")
        return

    user = {
        "id": len(data["users"]) + 1,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "isActive": True
    }

    data["users"].append(user)
    write_data(data)
    print("\n\nRegistration Done!!!!")