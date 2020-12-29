# Additionner le nombre d'element dans la liste

def total(x):
	init = 0
	for i in x:
		init = init + i
	return init

print(total([5, 5, 8, 2 ,3]))




def count(x):
	init = 0
	for i in x:
		init = init + 1
	return init

print(count([5, 5, 8, 2 ,3]))