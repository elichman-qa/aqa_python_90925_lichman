user_data = input("Введіть слово з 10 унікальними літерами: ")
print("Кількість унікальних символів:", len(list(set(user_data))))
if (len(list(set(user_data)))) > 10:
    print(True)
else: print(False)

while True:
    ch = 'h'
    word = input(f"Введіть слово з літерою {ch}: ")
    if ch in word.lower():
        print("Так! Це вірний варіант!")
        break
    else:
        print(f"Тут немає {ch}, тож введіть ще одне.")


list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

list2 = []
i = 0
while i < len(list1):
    if isinstance(list1[i], str):
        list2.append(list1[i])
    i += 1
print(list2)
