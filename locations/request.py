LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8423 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    },
    {
      "name": "Nashville East",
      "address": "244 Eastway Dr.",
      "id": 3
    }
  ]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found locations if it exists
    requested_locations= None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location= location
    
    return requested_location