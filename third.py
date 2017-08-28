import secondP  #import secondP file
import random   #random value
import urllib.request

secondP.add()   #calling add() function of secondP file

x = random.randrange(1,50)
print(x)

#sets
item = {'milk', 'cofee', 'noodle', 'cofee', 'cookies', 'laptop'}
print(item) #note that it doesn't print cofee twice

#dictionary
#note dictionary have key:value
classmate = {'first':' Economics', 'second':' OOSD', 'third':' POOPL', 'fourth':' Multimedia','fifth':' Network'}
print(classmate) #print whole thing
print(classmate['first']) #print specific

for k, v in classmate.items():
    print(k+v)

#modules