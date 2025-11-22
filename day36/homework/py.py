s = input("შეიყვანე სიტყვა: ")

for ch in s:
    if ch == 'e' or ch == 'E':
        break
    print(ch)




text = input("შეიყვანე წინადადება: ")

if "bad" in text.lower():
    print("დაუშვებელი სიტყვააა")
else:
    print("ყველაფერი კარგადაა")










text = input("შეიყვანე წინადადება: ")

for ch in text:
    if ch == ' ':
        continue
    print(ch)










text = input("შეიყვანე წინადადება: ")

for ch in text:
    if ch.lower() in "aeiou":
        continue
    print(ch)









a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))

start = min(a, b)
end = max(a, b)

for num in range(start, end + 1):
    if num % 15 == 0:
        print(num)
        break













while True:
    txt = input("შეიყვანე ტექსტი: ")

    if txt == "python is best":
        break

    print("you should learn python")

















a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))

start = min(a, b)
end = max(a, b)

count = 0

for num in range(start, end + 1):
    if num % 3 == 0:
        count += 1
        if count == 3:
            print(num)
            break
