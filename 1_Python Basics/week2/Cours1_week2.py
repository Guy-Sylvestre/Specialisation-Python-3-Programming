# -----------------------------1-------------------------
my_str = "MICHIGAN"
for i in my_str:
    print(i)


# -----------------------------2-------------------------
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for i in several_things:
    print(i)
for y in several_things:
    print(type(y))


# -----------------------------3-------------------------
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for i in str_list:
    print(len(i))


# -----------------------------4-------------------------
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for i in original_str:
	num_chars = num_chars + 1
print(num_chars)


# -----------------------------5-------------------------
addition_str = "2+5+10+20"

sum_val = addition_str.split("+")
cunt = 0
for i in sum_val:
	cunt += int(i)
print(cunt)



# -----------------------------6-------------------------
sum_val = week_temps_f.split(",")
cunt = 0
sum2 = 0
for i in sum_val:
	cunt += float(i)
	sum2 += 1
avg_temp = cunt / sum2
print(avg_temp)


# -----------------------------7-------------------------
nums = list(range(0, 68))
print(nums)


# -----------------------------8-------------------------
# -----------------------------9-------------------------
# -----------------------------10-------------------------
import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()
t1.shape("square")
t1.up

for i in ("yellow", 4, 5, 7, "red", 7):
    t1.forward(75)
    t1.speed(10)
    t1.stamp()
    t1.forward(-75)
    t1.speed(1)
    t1.right(45)
    t1.speed(5)