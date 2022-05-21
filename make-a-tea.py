import random
import datetime

# Tea library
coffeinated_tea = ["Black tea", "Green tea", "White tea",
                   "Macha tea", "Oolong tea", "Yerba mate tea"]
decaf_tea = ["Rooibus tea", "Herbal tea", "Fruit tea", "Mint tea"]

# Fruit library
winter_fruits = ["orange", "cranberry", "tanerine", "kiwi"]
spring_fruits = ["strawberry", "wildberry",
                 "blueberry", "ruhbarb", "apricot", "cherry"]
summer_fruits = ["pine apple", "banana", "lemon",
                 "lime", "peach", "melone", "pomegranate"]
autumn_fruits = ["pumpkin", "apple", "pear", "grape", "grapefruit"]

# Spice library
winter_spices = ["anise", "allspice", "nutmeg", "mace",
                 "cardamom", "cloves", "cinnamon", "ginger", "cocoa"]
spring_spices = ["fennel", "basil", "thyme",
                 "chamomile", "peppermint", "jasmine"]
summer_spices = ["lemon grass", "mint", "rose",
                 "tumeric", "lemon zest", "orange zest", "coconut"]
autumn_spices = ["toffee", "honeycomb", "honey",
                 "apple strudel", "ginger bread", "almond"]

# Conditions
current_time = datetime.datetime.now()
time_of_day = current_time.strftime("%p")
month = current_time.strftime("%m")

if time_of_day == "AM":
    tea_type = coffeinated_tea
else:
    tea_type = decaf_tea

if month == "12" or month == "01" or month == "02":
    fruits = winter_fruits
    spices = winter_fruits
elif month == "03" or month == "04" or month == "05":
    fruits = spring_fruits
    spices = spring_spices
elif month == "06" or month == "07" or month == "08":
    fruits = summer_fruits
    spices = summer_spices
elif month == "09" or month == "10" or month == "11":
    fruits = autumn_fruits
    spices = autumn_spices

# Select a tea
random_tea_num = random.randint(0, len(tea_type)-1)
tea = tea_type[random_tea_num]

# Select fruit
random_fruit_num = random.randint(0, len(fruits)-1)
fruit = fruits[random_fruit_num]

# Select spice
random_spice_num = random.randint(0, len(spices)-1)
spice = spices[random_spice_num]

# Print tea
print("Your tea is " + tea + " with " + fruit + " and " + spice)
