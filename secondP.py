#function
def add():
    print("hey! this is function.")
def usd_to_neplai(rs):
    amount = rs * 101
    return amount
def giving_back(num):
    amo = num * 3
    return amo
setValue = giving_back(34)
print("all this is test ",setValue," value")
add()
print(usd_to_neplai(20))

# default value for parameter
'''
    if no vale is pass to the parameter then vale set to the value assign 
    to the default parameter
'''
def get_gender(sex ="unknown"):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print(sex)
get_gender('m')
get_gender('f')
get_gender()

#keyword argunment
def do_cool_thing(name='Alex',action='play',item='Football', age=''):
    print(name,action,item,age)
do_cool_thing()
do_cool_thing('Mamta','love','Laxman',23)
'''if specific value to be pass in parameter then keyword of the item should be used
    of that function...
'''
#here only item is sent
do_cool_thing(item='Basketball')

#flexible number of argument
#note * must be append in front of  parameter of function
def give_more(*value):
    total = 0
    for a in value:
        total += a
    print(total)
give_more(23)
give_more(23,12,23)
give_more(23,1,2,3,4,5,5,6,7,8,9)

#unpacking arguments
#using * passes all the argument called unpaking argument
def calculate_health_rate(age, apple, smoke):
    calculate = (100-age)+(apple*2)-(smoke*3)
    print(calculate)
someone_health = [22,12,0]
calculate_health_rate(someone_health[0], someone_health[1], someone_health[2])
calculate_health_rate(*someone_health)
