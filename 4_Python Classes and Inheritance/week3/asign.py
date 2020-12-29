
#The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the string “Did not get gold”.
try:
    gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
    country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
    country_gold = []

    for x in country:
       if (x in gold.keys()):
           country_gold.append(gold[x])
           print(country_gold)
       else:
           country_gold.append("Did not get gold")
           print(country_gold)
except exception as e:
    print("une erreur ses produites")
    



#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.
try:
    di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
        {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
        {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
        {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}
    ]
    total = 0
    for diction in di:
       if ("Puppies" in  diction):
           total += diction["Puppies"]
    print("Total number of puppies:", total)
    
except Exception as e:
    print("Une error c'est produite")
    print(e)





#The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string “Error” appear in the remainder.
try:
    numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
    remainder = []
    for i in numb:
        if (i == 0):
            remainder.append("Error")
        elif (36 % i):
            remainder.append(36 % i)
        elif (36 % i == 0):
            remainder.append(0)
    print(remainder)

except Exception as e:
    print("Une error c'ets produite")
    print(e)




# Provided is buggy code, insert a try/except so that the code passes.

lst = [2, 4, 10, 42, 12, 0, 4, 7, 21, 4, 83, 8, 5, 6, 8, 234, 5, 6, 523, 42, 34, 0, 234, 1, 435, 465, 56, 7, 3, 43, 23]
lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except ZeroDivisionError:
        pass
print(lst_three)






#Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list attempt the string “Error”.
full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except IndexError:
        attempt.append("Error")
print(attempt)





#The following code tries to append the third element of each list in conts to the new list third_countries. Currently, the code does not work. Add a try/except clause so the code runs without errors, and the string ‘Continent does not have 3 countries’ is appended to countries instead of producing an error.
conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'],
         ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'],
         ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'],
         ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except IndexError:
        third_countries.append("Continent does not have 3 countries")
print(third_countries)





#The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code will run properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey": 4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except KeyError:
        ppl_play[x] = 1





#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes. If the key is not there, initialize it in the dictionary and set the value to zero.

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
      {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
      {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]

total = 0
for diction in di:
    try:
        diction.keys() == "Puppies"
        total = total + diction['Puppies']
    except:
        pass
    if("Puppies" not in diction.keys()):
        diction["Puppies"] = 0

print("Total number of puppies:", total)


















VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, initName):
        self.name = initName
        self.prizeMoney = 0
        self.prizes = []
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
    def __str__(self):
        state = self.name + " ($" + str(self.prizeMoney) + ")"
        return state
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(category, obscuredPhrase, guessed):
        str = input(self.name + "has $"+ str(self.prizeMoney)+ "/n" + ", Category:" + category + "/n" + ", Phrases:" + "/n" + obscuredPhrase + "/n" + ", Guessed:" + guessed + "/n" + "Guess a letter, phrase, or type 'exit' or 'pass':") 
        print(str)
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    prizemoney = 0
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
    
    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else: 
            return False
    
    def getPossibleLetters(self, guessed):
        list = []
        if self.prizemoney >= 250: 
            for l in LETTERS:
                list.append(l)
        else:
            for l in LETTERS:
                if l not in VOWELS:
                    list.append(l)
        return list

    def getMove(self, category, obscuredPhrase, guessed):
        list = self.getPossibleLetters(guessed)
        FlipResult = self.smartCoinFlip()
        if len(list) == 0:
            return 'pass'
        else:
            if FlipResult==True:
                for l in self.SORTED_FREQUENCIES:
                    if l in list:
                        return l
            elif FlipResult==False:
                return random.choice(list)