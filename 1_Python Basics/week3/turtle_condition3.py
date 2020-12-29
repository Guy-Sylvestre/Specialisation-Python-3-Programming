words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []
for word in words:
	# pass
	
	if (word[-1:] == "e"):
		print(word + "d")
	else:
		print(word + "ed")
		print(word)