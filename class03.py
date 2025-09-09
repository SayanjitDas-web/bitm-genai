#list(Array)

my_list = [1,2,3,4,"five","six", True, False]
#         [0,1,2,3,   4,    5,     6,    7]

my_list2 = list([7,"eight",9,True,"five","six", True, False])

#----- CRUD operation

#read or get one element/value from list
# print(my_list[4])

#1st method
# for i in range(0,len(my_list)):
#     print(my_list[i])

#2nd method
# flag = 0
# while flag < len(my_list):
#     print(my_list[flag])
#     flag = flag + 1

#3rd method
# for val in my_list:
#     print(val)

#add new value
# my_list.append("ten")
# my_list.insert(2,44)

#update a value
# my_list[4] = "eleven"

#delete a value
# my_list.remove("six")
# my_list.pop()

#slicing
# print(my_list[4:])
# print(my_list[::-1])
# my_list.reverse()
# print(my_list)


#dictionary
my_dict = {
    "name":"sayan",
    "email":"test@test.com",
    "age":26,
    "isPresent": True
}

# loop dictionarykey and value
# for [key, val] in my_dict.items():
#     print(key,val)

# read a key
# print(my_dict["name"])

#update a dictionary key
# my_dict["age"] = 25

#create/add a key
# my_dict.update({"roll":"1234abcd56"})
# my_dict["roll"] = "1234abcd56"

#delete a key
# del my_dict["email"]

# print(my_dict)

my_set = {1,5,7,3,2,4,6}

#add value to set
# my_set.add(10)
# my_set.update({9})

#delete
# my_set.remove(7)

# print(my_set)