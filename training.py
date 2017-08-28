#if else loop
name = "Hari"
if name is "Hari":
    print("you are wrong person")
elif name is "Shyam":
    print("You are not allowed here")
elif name is "Ram":
    print("What the heck")
else: print("Oh! where you been")

#list and for loop
fruit = ['Banna', 'Apple', 'Mango', 'Orange', 'Jackfruit']
for f in fruit:
    print(f)
    print(len(f))
print("Break")
for x in range(5,10):
    print(x)
print("break")
#range (start, end, increment)
for x in range(2,15,3):
    print(x)
print("Break")
fan = 5

#while loop
while fan < 10:
    print("hello~!")
    fan += 2
#this is single line comment
'''
    and this is multiline  comment
'''
#break statement
magicNmber = 345
for n in range(51):
    if n is magicNmber:
        print(n," is your magic Number")
        break
    else: print("bad day :(")
    break
print(56," Break ", 6)

#continue statement
number = [11,12,13,14,15,16]
for n in range(10,20):
    if n in number:
        continue
    print(n)