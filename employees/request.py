EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Betty Davis",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Billy Holiday",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Louis Armstrong",
      "locationId": 2
    },
    {
      "name": "Susan Simmons",
      "locationId": 1,
      "id": 5
    },
    {
      "name": "Nat King Cole",
      "locationId": 1,
      "id": 6
    }
  ]

def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employees if it exists
    requested_employees= None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employees= employee
    
    return requested_employees