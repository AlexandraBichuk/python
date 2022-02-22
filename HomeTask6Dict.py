text = ("привет здравствуй привет как дела пока")
dict = {}
for key in text.split():
    if not dict.get(key) == None:
        dict[key] += 1
    else:
        dict[key] = 1
for key, value in dict.items():
    print(f'{key}: {value}')



