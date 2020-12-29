# -------------------------------1------------------------------
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding")
print(sports)

# -------------------------------2------------------------------
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

trav_dest.pop(-2)
print(trav_dest)

# -------------------------------3------------------------------
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']


trav_dest.append("Guadalajara")
print(trav_dest)

# -------------------------------4------------------------------
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']

winners.sort()
print(winners)

# -------------------------------5------------------------------
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

winners.reverse()
z_winners = winners
print(z_winners)

# -------------------------------6------------------------------
str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for i in str1:
	for y in i:
		chars += [y] 
	# pass
print(chars)

# -------------------------------7------------------------------
ael = "python!"

app = []
for i in ael:
	app += [i]
print(app)

# -------------------------------8------------------------------
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

past_wrds = []
for wrd in wrds:
	past_wrds +=[ wrd + "ed"]
print(past_wrds)

# -------------------------------9------------------------------
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

convertion = scores.split()

a_scores = 0
for score in convertion:
	if (score >= "90"):
		a_scores += 1
print(a_scores)

# -------------------------------10------------------------------
p_phrase = "was it a car or a cat I saw"

r_phrase  = p_phrase[::-1]
print(r_phrase )


# -------------------------------11------------------------------
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for temp in inventory:
    temp = temp.split(',')
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(temp[1],temp[0],temp[2])
    print(str1)

# -------------------------------12------------------------------
# -------------------------------13------------------------------