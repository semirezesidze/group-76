for i in range(1, 51):
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")









for i in range(0, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(i, "იყოფა 3-ზე")
    elif i % 5 == 0:
        print(i, "იყოფა 5-ზე")
    else:
        print(i, "არ იყოფა არცერთზე")

















num = int(input("შეიყვანე რიცხვი: "))
even = 0
odd = 0

for i in range(0, num + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("ლუწი რიცხვების რაოდენობა:", even)
print("კენტი რიცხვების რაოდენობა:", odd)










numbers = [10, 25, 33, 47, 80, 99]

for n in numbers:
    if n > 50:
        print(n, "მეტი 50-ზე")
    else:
        print(n, "ნაკლები 50-ზე")












total = 0

for i in range(0, 101):
    if i % 2 == 0:
        print(i)
        total += i

print("ლუწი რიცხვების ჯამია:", total)










words = ["apple", "banana", "avocado", "cherry", "apricot"]

for word in words:
    if word.startswith("a"):
        print(word)















for i in range(0, 21):
    if i == 0:
        print(i, "ნულია")
    elif i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")

















numbers = [5, 15, 25, 35, 45, 55]

for n in numbers:
    if n % 5 == 0:
        print(n)












word = input("შეიყვანე სიტყვა: ")

for letter in word:
    print(letter)









total = 0

for i in range(1, 11):
    total += i

print("ჯამი არის:", total)
