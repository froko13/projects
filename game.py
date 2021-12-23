import random
print("Добро пожаловать в игру в палач!")
Word = int(input("Сколько нужно слов? "))
wordik = input("Введи слова ")
sus = wordik.split()
while len(sus) != Word:
    print("Ты написал много или мало слов попробуй ещё ")
    wordik = input("Введи слова ")
    sus = wordik.split()

secret = random.choice(sus)
palyer = "_" * len(secret)
print(palyer)
while palyer != secret:
    userletter = input("введите букву ")
    for i in range(len(secret)):
        if secret[i] == userletter:
            palyer = palyer[:i] + userletter + palyer[i+1:]
    print(palyer)
if palyer == secret:
    print("LETS GO")

