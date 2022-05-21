import random
import datetime

# Tea library
coffeinated_tea = ["Black tea", "Green tea", "White tea",
                   "Macha tea", "Oolong tea", "Yerba mate tea"]
decaf_tea = ["Rooibus tea", "Herbal tea", "Fruit tea"]

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
    spices = winter_spices
elif month == "03" or month == "04" or month == "05":
    fruits = spring_fruits
    spices = spring_spices
elif month == "06" or month == "07" or month == "08":
    fruits = summer_fruits
    spices = summer_spices
elif month == "09" or month == "10" or month == "11":
    fruits = autumn_fruits
    spices = autumn_spices

# Selecting ingridients
result = []


def select_ingredients(array):
    random_num = random.randint(0, len(array)-1)
    ingredient = array[random_num]
    result.append(ingredient)
    return result


def create_tea():
    rand_num1 = random.randint(1, 2)
    rand_num2 = random.randint(1, 2)
    select_ingredients(tea_type)
    if rand_num1 == 2:
        select_ingredients(fruits)
        select_ingredients(fruits)
    else:
        select_ingredients(fruits)
    if rand_num2 == 2:
        select_ingredients(spices)
        select_ingredients(spices)
    else:
        select_ingredients(spices)


create_tea()

# Remove duplicates from array
result = list(dict.fromkeys(result))

# Add words to array to complete the sentence
result.insert(0, "Here is your")
result.insert(2, "with")
result.insert(-1, "and")


# Turn array to string
def stringify(array):
    string = " "
    return (string.join(array))


print(stringify(result))
