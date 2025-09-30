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