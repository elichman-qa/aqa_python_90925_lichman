user_data = input("Введіть слово з 10 унікальними літерами: ")
print("Кількість унікальних символів:", len(list(set(user_data))))
if (len(list(set(user_data)))) > 10:
    print(True)
else:
    print(False)

def search_ch_in_word(ch) :
    while True:
        word = input(f"Введіть слово з літерою {ch}: ")
        if ch in word.lower():
            print("Так! Це вірний варіант!")
            break
        else:
            print(f"Тут немає {ch}, тож введіть ще одне.")

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

list2 = []
def print_str_value(some_list):
    i = 0
    while i < len(some_list):
        if isinstance(some_list[i], str):
            list2.append(some_list[i])
        i += 1
    print(list2)

print("—" * 120, "\n")
nums = [1, 9, 8, 4, 165, 12, 54, 84, 55, 21, 11, 6, 7, 65]

nums2 = []

def sum_pare_value(list_nums) :
    i = 0
    while i < len(list_nums):
        if list_nums[i]%2 == 0:
            nums2.append(list_nums[i])
        i += 1
    print('Сума парних чисел:', sum(nums2))