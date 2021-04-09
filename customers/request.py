CUSTOMERS = [
    {
      "email": "stacey.littrell@gmail.com",
      "name": "Stace L",
      "id": 1
    },
    {
      "email": "1232@yoho.com",
      "name": "Hannah Hall",
      "id": 2
    },
    {
      "email": "favdog@bark.com",
      "name": "Sally  Street",
      "id": 3
    },
    {
      "email": "barkbark@dog.com",
      "name": "Mike Morgan",
      "id": 4
    },
    {
      "email": "Jump@bark.com",
      "name": "Jenna  JumpingJack",
      "id": 5
    },
    {
      "email": "mark@bark.com",
      "name": "Markey Mark",
      "id": 6
    }
  ]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customers if it exists
    requested_customer= None

    # Iterate the customers list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer= customer
    
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
  
    new_id = max_id + 1
  
    customer["id"] = new_id
  
    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)