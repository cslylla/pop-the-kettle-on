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

# Name library
name_first = ["cozy", "lazy", "tasty",
              "smooth", "dark", "starry", "melancholic", "warm", "cold", "fuzzy", "jelly", "dozy", "sparkly", "enchanted", "lady", "lord", "turkish", "russian", "exotic", "old"]
name_second = ["bonfire", "hug", "duvet", "kiss", "cuppa", "cake", "sorbet", "girl",
               "boy", "unicorn", "brew", "blend", "tea", "breeze", "rock", "love", "universe"]
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


def select(array):
    random_num = random.randint(0, len(array)-1)
    item_from_array = array[random_num]
    return item_from_array


def create_tea():
    rand_num1 = random.randint(1, 2)
    result.append(select(tea_type))
    i = 1
    while i <= rand_num1:
        result.append(select(fruits))
        i += 1
    rand_num2 = random.randint(1, 2)
    j = 1
    while j <= rand_num2:
        result.append(select(spices))
        j += 1


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
