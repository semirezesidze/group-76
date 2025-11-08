
text = input("შეიყვანე სიტყვა ან ტექსტი: ")


if 'a' in text or 'A' in text:
    print("ტექსტში არის 'a' ან 'A'")
else:
    print("ტექსტში არ არის 'a' და 'A'")


if 'car' not in text:
    print("ტექსტში არ არის სიტყვა 'car'")
else:
    print("ტექსტში არის სიტყვა 'car'")

























text = input("შეიყვანეთ ტექსტი: ")
print("a ან A არის?:", ('a' in text) or ('A' in text))
print("'car' არ არის?:", 'car' not in text)
for ch in text:
    if ch.lower() == 'a':  # მცირე გაუმჯობესება — ორივე 'a' და 'A' სკიპდება
        continue
    print(ch)
s