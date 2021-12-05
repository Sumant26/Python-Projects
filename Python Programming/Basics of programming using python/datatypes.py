#int, float, string, double, boolean, 

# PRIMITIVE DATATYPES
# Number = int, float, double
# Strings
# Booleans

integer = 5    # int
decimal = 5.5  # float
negative = -15 # int
negativeDecimal = -15.5

# Strings 
# A string is a sequence of one or more characters
# a-z, A-Z, 0-9, `~!@#$%^&*()_+-={}[]"':;<>,.?/|\ 
# enclosed in either '' or ""
string = "9"
name = "Sumant"
surname = 'Tulshibagwale'
address = "1206/26 B, ShivajiNagar pune 4"
char = 'b'

# Booleans
# True/False
# used to assert or check
isAdult = False
isRaining = True

# null is not there in Python
# None 

none = None

# check type of variable
type(name)     # str
type(negative) # int
type(decimal)  # float 
type(isRaining)# bool
type(none)     # None

# Collection Types
# list
# is a collection of elements seperated by commas
# enclosed by []
# every element has an INDEX (which is position - 1)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["sumant", "ambareesh", "shreya", "manjiri", "aniruddha"]
didPractice = [True, False, False, False, True, True]
mixed = [1, "hi", False, [1, 2, 3]]
mixed[3][2] # 3

# dict = dictionary
# a collection of key(label): value pair
# separated by commas
person = {
    "name": "Sumant",
    "age": 10,
    "contact": "0123456789",
    "isMarried": False,
    "marks": [89, 90, 78, 67, 56, 45],
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}

person["name"] # Sumant
person["address"]["state"] # Maharashtra