import json

print('Beginning setup...')
PATH = input('Введи путь до репозитория (пример: ~/ami-238-1-Gleb-Golubev-Kreox): ')
print('Путь сохранен!')
with open('globals/path.txt', 'w+') as f:
    f.writelines(PATH)

