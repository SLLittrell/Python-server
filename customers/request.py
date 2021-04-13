import sqlite3
import json
from models import Customer


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
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.name
        FROM customer c
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['email'], row['name'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


# Function with a single parameter
def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.name
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))
        

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], data['email'], data['name'])

        return json.dumps(customer.__dict__)


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

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break