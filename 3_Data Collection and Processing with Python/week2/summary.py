
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@       WEEK 2        @@@@@@@@@@@@@@@@@@@@@@
lst = ["hi",
    "goodbye",
    "python",
    "106",
    "506",
    91,
    ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5],
    109,
    "chair",
    "pizza",
    "wolverine",
    2017,
    3.92,
    1817,
    "account",
    "readings",
    "papers",
    12,
    "facebook",
    "twitter",
    193.2,
    "snapchat",
    "leaders and the best",
    "social",
    "1986",
    9,
    29,
    "holiday",
    ["women", "olympics", "gold", "rio", 21, "2016", "men"],
    "26trombones"
]
num_lst = list()
for i in lst:
    # function isinstance verify if number is integer or float
    # give two arguments first the number have verify and second parametre alias (int, float)
    if (isinstance (i, (int, float))):
        num_lst.append(i)
    elif type(i) is list():
        for y in i:
            if (isinstance (y, (int, float))):
                num_lst.append(y)
          
print(num_lst)
# -----------------------------------------------------------------------------------------------------------



# 1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = map(lambda x: 2*x, lst)
print(list(greeting_doubled))



# 2. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper = map(lambda x: x.upper(), abbrevs)
print(list(abbrevs_upper))


# --------------------------------------------------------------------------------------------------------------


# 1. Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = filter(lambda x: "w" in x, lst_check)
print(list(filter_testing))


# 2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = filter(lambda x: "o" in x, lst)
print(list(lst2))


# --------------------------------------------------------------------------------------------------------------------------


# 2. The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed
L = [12, 34, 21, 4, 6, 9, 42]
# lst = []
# for x in L:
#     if x > 10:
#         lst.append(x)
# print(lst)

lst2 = [x for x in L if x >= 12]
print(lst2)



# 3. Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension.
tester = {'info': [
    {"name": "Lauren",
        'class standing': 'Junior',
        'major': "Information Science"
        },
    {'name': 'Ayo',
         'class standing': "Bachelor's",
         'major': 'Information Science'
        },
    {'name': 'Kathryn',
         'class standing': 'Senior',
         'major': 'Sociology'
         },
    {'name': 'Nick',
         'class standing': 'Junior',
         'major': 'Computer Science'
         },
    {'name': 'Gladys',
         'class standing': 'Sophomore',
         'major': 'History'
         },
    {'name': 'Adam',
         'major': 'Violin Performance',
         'class standing': 'Senior'
         }
    ]
}

compri  = [x["name"] for x in tester["info"]]

print(compri )


# 1. Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x + y for (x , y) in zip(L1, L2) if x >= 0 and y <= 5]
print(L3)