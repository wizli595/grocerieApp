import sqlite3

groceries = [
    "apples",
    "bananas",
    "clemintines",
    "dill",
    "eggs",
    "flour",
    "granola",
    "honey",
    "ice cream",
    "juice",
    "ketchup",
    "lemon",
    "margarine",
    "onion",
    "potatoes",
    "rosmary",
    "salt",
    "thyme",
    "vinegar",
    "watermelon",
    "pears",
    "cucumbers",
    "garlic",
    "carrots",
    "pastries",
    "eggplants",
    "milk",
    "coffee",
    "tea",
    "rice",
    "noodles",
    "lentils",
    "sweet potatoes",
    "strawberries",
    "cranberries",
    "mangos",
    "pappers",
    "zuccinis",
    "lime",
    "broth",
    "mushrooms",
    "chicken",
    "beef",
    "pork",
    "fish",
    "cream",
    "paprika",
    "tumeric",
    "cinamon",
    "pumpkin",
    "basil",
    "tomatoes",
    "bread",
    "cake",
    "chocolate",
    "gum",
    "pinapple",
    "oranges",
    "lettuce",
    "cheese",
    "cilantro"
]
# sorting
groceries = sorted(groceries)
# conecting
connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()
# execute queries
cursor.execute(
    "create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
    cursor.execute("insert into groceries (name) values (?)", [groceries[i]])

connection.commit()
connection.close()
