my_str = "hello BITM" # -> (0,1,2,3,4,5,6,7,8,9) ->(index position value)
                      # -> (h,e,l,l,o, ,B,I,T,M)
# print(my_str[6])
# print(len(my_str))

# new_str = my_str.replace("???","")
# print(new_str.isdigit())

# - loops (for, while)
# for val in range(0,10):
#     print(val)

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# for val in range(0,10):
#     if val == 5:
#         break
#     print(val)

my_str2 = "hello students!"
new_str = ""

# print(my_str,end=" and ")
# print(my_str2)

# for char in my_str2:
#     new_str += char + "-"

# print(new_str)

def add():
    num1 = int(input("enter number1: ")) #"10"
    num2 = int(input("enter number2: ")) #"5"
    print(num1+num2)

add()