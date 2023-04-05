texts = list()

while True:
    try:
        user_input = input()
        texts.append(user_input)
    except EOFError as e:
        print("end of file reach")
        break

texts_len = len(texts)
for index in range(texts_len - 1, -1, -1):
    print(texts[index])