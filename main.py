import getpass
import socket
import os

us = getpass.getuser()
host = socket.gethostname()
while True:
    startstr = f"{us}@{host}:~$ "
    comma = input(startstr).strip()
    if not comma:
        continue
    comma = os.path.expandvars(comma)
    strr = comma.split()
    command = strr[0]
    arg = strr[1:]
    if command == "exit":
        print("Пока пока")
        break
    elif command == "ls":
        print(f"[Заглушка] Вызвано 'ls'. Аргументы {arg}")
    elif command == "cd":
        print(f"[Заглушка] Вызвано 'cd'. Аргументы {arg}")
    elif command == "clear":
        print(f"Вызвано 'clear'. Аргументы {arg}")
    elif command == "echo":
        print(f"Вызвано 'echo'. Аргументы {arg}")
    elif command == "chmod":
        print(f"Вызвано 'chmod'. Аргументы {arg}")
    else:
        print(f"Вы ввели комманду: {command} Комманда не найдена")
