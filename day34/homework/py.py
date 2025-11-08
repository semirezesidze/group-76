cities = ["თბილისი", "ბათუმი", "რუსთავი", "ზუგდიდი", "გორი", "ფოთი"]

for city in cities:
    if len(city) > 6:
        print(city)



words = ["supercalifragilistic", "hello", "extraordinaryword", "smallword", "longwordwithfifteen"]

for word in words:
    if len(word) % 15 == 0:
        print(word)












numbers = [1, 5, 7, 10, 23, 42, 55, 78]
count = 0

for num in numbers:
    count += 1

print("რიცხვების რაოდენობა:", count)












words = ["apple", "banana", "peach", "grape", "kiwi", "mango"]

for word in words:
    if len(word) == 5:
        print(word)







sentence = input("შეიყვანეთ წინადადება: ")
total_chars = 0
count_a = 0

for char in sentence:
    total_chars += 1
    if char == 'a' or char == 'A':
        count_a += 1

print("სიმბოლოების რაოდენობა:", total_chars)
print("'a' ან 'A' სიმბოლოების რაოდენობა:", count_a)












strings = ["hello", "extraordinary", "world", "PythonProgramming", "AI"]

longest = strings[0]

for s in strings:
    if len(s) > len(longest):
        longest = s

print("ყველაზე გრძელი სტრინგი:", longest)
