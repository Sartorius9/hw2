text = list(input("Введите числа без пробелов - "))

for i in range(1, len(text), 2):
    text[i - 1], text[i] = text[i], text[i - 1]
print(text)