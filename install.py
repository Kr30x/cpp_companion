import subprocess
from sys import stderr, stdout

print('Начинаю настройку...')
PATH = input('Введи путь до репозитория (пример: ami-238-1-Gleb-Golubev-Kreox): ')
print('Путь сохранен!')
with open('globals/path.txt', 'w+') as f:
    f.writelines(PATH)
valid_choice = False
choice = 'undefined'
while not valid_choice:
    choice = input('Автоматически генерировать сообщения коммитов? (y/n): ')
    if choice == 'y':
        valid_choice = True
    elif choice == 'n':
        valid_choice = True
with open('globals/autocommit.txt', 'w+') as f:
    if choice == 'y':
        f.writelines('True')
    else:
        f.writelines('False')

print('Создаю build папку...', end=' \t\t')

try:
    result = subprocess.run(f'mkdir ~/{PATH}/build', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
    print('OK')
    print('Настройка завершена!')
except Exception as e:
    print('Warning:', e)
    print('Пробую удалить папку...', end=' \t')
    try:
        result = subprocess.run(f'rm -R ~/{PATH}/build', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print('OK')
        print('Создаю build папку заново...', end=' \t')
        try:
            result = subprocess.run(f'mkdir ~/{PATH}/build', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print('OK')
            print('Настройка завершена!')
        except Exception as e:
            print('Error: ', e)
    except Exception as e:
        print('Error: ', e)

# try:
#     print('Инициализирую cmake...', end = ' \t\t')
#     result = subprocess.run(f'cmake ~/{PATH}', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     print('OK')
#     print('Настройка завершена!')
# except Exception as e:
#         print('Error: ', e)
