percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

pesps = list()

for i in percent_rain:
    if (i > 90):
    	pesps.append("Bring an umbrella")
        # print("Bring an umbrella")
    elif (i > 80):
    	pesps.append("Good for the flowers?")
        # print("Good for the flowers?")
    elif (i > 50):
    	pesps.append("Watch out for clouds!")
        # print("Watch out for clouds!")
    else:
    	pesps.append("Nice day!")
        # print("Nice day!")
print(pesps)