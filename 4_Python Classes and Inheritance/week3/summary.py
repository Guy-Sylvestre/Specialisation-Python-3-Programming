# Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0
for i in original_str:
    num_chars += 1
print(num_chars)




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      TEST UNITAIRE       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       GESTIONNAIRE D'ERREUR       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print("got an error")
    print(e)

print("continuing")





try:
    for i in range(5):
        print(1.0 / (3-i))
except Exception as error_inst:
    print("Got an error", error_inst)