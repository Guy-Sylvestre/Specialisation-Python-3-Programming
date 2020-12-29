# initialisation, arrèt et compte de deux en deux

initt = 0
countt = 15
aa = list()
while(initt < 15):
	aa.append(initt)	
	initt += 1
print(aa)



list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
summ = 0
while (tot < len(list1)):
	summ += list1[tot]
	tot += 1
print(summ)




# Write a function called that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.stop_at_four





def stop_at_four(my_list):
    accum_lst=[]
    accum_var=0

    while (accum_var < len(my_list)) and (my_list[accum_var] != 4):
        accum_lst.append(my_list[accum_var])
        accum_var+=1
    return accum_lst

print(stop_at_four([3,6,4,1,3]))




#########################################################################
import random
import turtle


def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(90)
    else:                      # tails
        t.right(90)

    t.forward(50)

wn.exitonclick()