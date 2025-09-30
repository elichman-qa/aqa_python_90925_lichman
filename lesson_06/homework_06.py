user_data = input()
print(len(list(set(user_data))))
if (len(list(set(user_data)))) > 10:
    print(True)
else: print(False)

# if set(user_data)