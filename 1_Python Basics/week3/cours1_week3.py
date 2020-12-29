# -----------------------1---------------------
Hard-coded answers will receive no credit.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
convertiont = rainfall_mi.split()
num_rainy_months = 0
for i in convertiont:
	if (i > "3"):
		num_rainy_months += 1
print(num_rainy_months)



# -----------------------2---------------------
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

convertiont = sentence.split()
sentencesame_letter_count = 0
for i in convertiont:
    sentencesame_letter_count += 1
print(sentencesame_letter_count)

# -----------------------3---------------------
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0
for item in items:
	if ("w" in item):
		acc_num += 1
print(acc_num)


# -----------------------4---------------------
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

convertion = sentence.split()
print(convertion)
num_a_or_e = 0
for i in convertion:
	if ("a" in i or "e" in i):
		num_a_or_e += 1
print(num_a_or_e)


# -----------------------5---------------------
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

compt = 0
for i in s:
	if (i in vowels):
		compt += 1
print(compt)




# -----------------------6---------------------