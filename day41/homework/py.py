# append(item) - siss bolos chasvavs elements
# insert(index, item) - chasvams elements
# pop() - washlis bolo elementts
# remove(item) - washlis elements
# len(list) - datvlis elementebs








numbers = [1, 2, 3, 4, 5]
numbers.append(10)  

print(numbers)







names = ["Luka", "Goga", "Saba"]
names.append("Semi")  
print(names)




names = ["Luka", "Goga", "Saba"]
user_name = input("Sheiyvane saxeli" )
names.append(user_name)  
print(names)











names = ["Luka", "Goga", "Saba", "Nana", "Mari"]
names.insert(3, "Semi")  
print(names)





my_list = ["A", "B", "C", "D", "E", "F"]
user_name = input("Sheiyvane Saxeli" )
user_index = int(input("Sheiyvane Indeqsi : "))
my_list.insert(user_index, user_name)
print(my_list)




fruits = ["apple", "banana"]
fruits.insert(1, "orange")  
print(fruits)




names = ["goga", "saba", "luka"]
names.insert(2, "irakli") 
print(names)














foods = ["bread", "milk", "cheese"]
foods.insert(0, "water")  
print(foods)












fruits = ["apple", "banana", "orange"]
fruits.pop(1)  
print(fruits)








names = ["goga", "saba", "luka"]
index_saba = names.index("saba")  
names.pop(index_saba)  
print(names)











colors = ["red", "green", "blue", "yellow", "black", "purple"]
colors.pop(0)  
print(colors)

colors.pop(2) 
print(colors)







