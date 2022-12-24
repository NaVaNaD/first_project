# x = 9
# y = 8
# if x>y:
#     print('big')
# else:
#     print ('small')
#
# #2
# x=0
# while x < 5 :
#     print (x)
#     x = x + 1
#
# #3
# numbers = range(1,4)
# for number in numbers :
#     if number == 1:
#         print ('summer')
#     elif number == 2 :
#         print ('winter')
#     elif number == 3 :
#         print ('fall')
# else:
#         print ('spring')


# 5

# age = 44
# first_family_name = 'A'
# shekel_vs_dollars = 3.5
# fly_abroad = True
# appartment_num = 45
#
# print(age, first_family_name, shekel_vs_dollars, fly_abroad,appartment_num)
#
# sum = age + shekel_vs_dollars
# print (sum)


# 6
#
# user_phone = input('please enter you phone number')
# print(f'your phone number is: {user_phone}')
#
#
# def print_hello():
#     print('hello')
#
#
# def calculate():
#     print(5+3.2)
#
#
# def name():
#     name1 = input('what is your name?')
#     print (name1)
#
# def div(x):
#     c= x/2
#     print (c)
#
# div(8)


# 10
#
# for x in range(1,10):
#     for j in range(1,x):
#         print ('x', end=' ')
#     print('\n')


# 11
#
# for x in range(1, 8):
#     for i in range(1, 8):
#         if i == x or i == 8-x:
#             print('x', end=' ')
#         else:
#             print(' ', end=' ')
#     print('\n')

12


def user_num():
    a = input('please enter your number')
    return a


def compute_num():
    b = str(user_num())
    # print(b)
    # print(b[1])
    i = 0
    c = 0
    for i in b:
        c += int(i)
        # while i<len(b):
    #     c += int(b[i])
    #     i += 1
    print(type(b))
    print(type(c))


compute_num()
