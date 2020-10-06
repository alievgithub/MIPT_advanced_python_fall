with open('1.txt', 'w', encoding = 'utf8') as file:
    file.writelines(['  Hello  \n', '  Father  \n', ' !!!  \n'])

with open('1.txt', 'r', encoding = 'utf8') as file:
    STR = file.readlines()

for str in STR:
    str = str.strip()
    print(str)
