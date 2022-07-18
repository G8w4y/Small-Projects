# flavours = [
#     {'Name': 'Espresso',
#      'Price': '$1.50',
#      'Water': '50 ml',
#      'Coffee': '18 g'
#      },
#     {'Name': 'Latte',
#      'Price': '$2.50',
#      'Water': '200 ml',
#      'Coffee': '24 g',
#      'Milk': '150 ml'
#      },
#     {'Name': 'Cappuccino',
#      'Price': '$3.00',
#      'Water': '250 ml',
#      'Coffee': '24 g',
#      'Milk': '100 ml'
#      },
#             ]
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coffee = """
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \`
   |             | )  )
   |             |/  /
   |             /  / 
   |            (  /
   \             y'
    `-.._____..-'
"""