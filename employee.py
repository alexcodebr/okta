employees = {
    "bdoe@email.com": {
        "first_name": "Bob", 
        "last_name": "Doe",
        "address": {
            "city": "New York",
            "street": "1st Street",
            "house_number": 1
        }
    },
    "mmarkson@email.com": {
        "first_name": "Mark", 
        "last_name": "Markson",
        "address": {
            "city": "San Diego",
            "street": "2nd Street",
            "house_number": 2
        }
    }
}

pp.pprint(employees)

# Keys and values
for emp_email, emp_info in employees.items():
    print(f"EMAIL: {emp_email}")
    
    # For each key that belongs to a dictionary at the given email
    for key in emp_info:
        # Print the corresponding key and value
        print(f"{key} = {emp_info[key]}")
    
    print()