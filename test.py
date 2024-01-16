import os
import subprocess
from sys import stderr, stdout

with open('globals/path.txt') as f:
    PATH = f.readline()

with open('globals/autocommit.txt') as f:
    AUTOCOMPLETE = f.readline()
    AUTOCOMPLETE = bool(AUTOCOMPLETE)
    
EXISTING_TASKS = os.listdir(f'../{PATH}/tasks')


def push(task_name):
    print('Начиннаю процесс пуша задачи ', task_name + '...')
    
    print(f'Создаю ветку submits/{task_name}... \t')
    try:
        result = subprocess.run(f'cd ~/{PATH}; git checkout main', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = subprocess.run(f'cd ~/{PATH}; git checkout -b submits/{task_name}', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        print('Перехожу на ветку... \t\t')
        try:
            result = subprocess.run(f'cd ~/{PATH}; git checkout main', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            result = subprocess.run(f'cd ~/{PATH}; git checkout submits/{task_name}', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print('OK')
        except Exception as e:
            print('Error:', e)
    result = subprocess.run(f'cd ~/{PATH}; git status', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
    
    valid_choice = False
    choice = 'undefined'
    while not valid_choice:
            choice = input('Подтвердить изменения? (y/n): ')
            if choice == 'y':
                valid_choice = True
            elif choice == 'n':
                valid_choice = True

    if choice != 'y':
        return 
    
    print('Staging files...', end=' ')
    try:
        result = subprocess.run(f'cd ~/{PATH}; git add -A', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
        print('OK')
    except Exception as e:
        print('Error', e)
        return 
    print('Commiting files...', end=' ')
    if AUTOCOMPLETE:
        try:
            result = subprocess.run(f'cd ~/{PATH}; git commit -m "Solution for task: {task_name}" ', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
            print('OK')
        except Exception as e:
            print('Error:', e) 
    else:
        commit_message = input('Сообщение коммита: ')
        try: 
            result = subprocess.run(f'cd ~/{PATH}; git commit -m "{commit_message}" ', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
            print('OK')
        except Exception as e:
            print('Error: ', e)
    
    print('Pushing commit...', end=' ')
    try: 
        result = subprocess.run(f'cd ~/{PATH}; git checkout submits/{task_name}; git push', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
        print('OK')
    except Exception as e:
        print('Error:', e)



def test(task_name):
    try:
        result = subprocess.run(f'cd ~/{PATH}/build; cmake ..; make test_{task_name}; ./test_{task_name}', shell=True, check=True, stdout=stdout, stderr=stderr, text=True)
        valid_choice = False
        while not valid_choice:
            choice = input('Запушить решение? (y/n): ')
            if choice == 'y':
                push(task_name)
                valid_choice = True
            elif choice == 'n':
                valid_choice = True
    except Exception as e:
        pass
def main():
    for task in EXISTING_TASKS:
        print(task)
    correct_task_name = False
    task_name = 'undefined'
    while not correct_task_name:
        task_name = input('Название задачи: ')
        if task_name not in EXISTING_TASKS:
            print('Такой задачи нет')
        else:
            correct_task_name = True
    test(task_name)

    


if __name__ == "__main__":
    main()
