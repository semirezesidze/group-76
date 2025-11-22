name = input("შეიყვანე სახელი: ")
print(name.upper())










name = input("შეიყვანე სახელი დიდი ასოებით: ")
print(name.lower())








name = input("შეიყვანე სახელი პატარა ასოებით: ")
print(name.capitalize())










names = ["luka", "dato", "mari", "nana"]

for n in names:
    print(n.upper())













names = ["luka", "dato", "mari", "nana"]

for n in names:
    print(n.upper())














names = ["LUKA", "DATO", "MARI", "NANA"]

for n in names:
    print(n.lower())








names = ["luka", "dato", "mari", "nana"]

for n in names:
    print(n.capitalize())













elements = [1, 2, 3, 4, 5, "hello"]

print(len(elements))









text = "ალექსანდრე"
print(len(text))









nums = [1, 2, 3, 4, 5, 6, 10, 12]

count = 0
for n in nums:
    if n % 2 == 0:
        count += 1

print(count)









start = int(input("start: "))
end = int(input("end: "))
step = int(input("step: "))

for num in range(start, end, step):
    if num % 2 == 0:
        print(num)
