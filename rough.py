# lst = [1,2,3]

# my_str = "mlops playlist"

# my_int = 155
# # lst.clear()
# # print((lst)) 
# # print(type(my_str))
# # print(type(my_int))
# a = "X"
# b = "Y"
# print(a+b)

from oops_proj import chatbook

# user1 = chatbook()
#function vs method below
# lst = [1,2,3]

# a1 = len(lst)
# print(a1)
# #method
# user1 = chatbook()
# user1.sendmsg()
user1 = chatbook()
print(user1.id)


# using static method to set the id of the class chatbook, using static method directly from class chatbook rather than object, without creating an object of the class. Static methods are used to perform operations that are related to the class but do not require access to instance-specific data. In this case, set_id is a static method that allows you to set the value of the private class variable __user_id without needing an instance of the chatbook class. This is useful for managing class-level data that is shared among all instances of the class.
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)




# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)













# print(user1._chatbook__name)
# getter and setter
# print(user1.get_name())
# user1.set_name("AgentX")
# print(user1.get_name())
