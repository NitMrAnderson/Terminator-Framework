import subprocess
from prompt_toolkit import prompt
from usr.config import style, promt, info, warn, error
from core.AddonLoader import *
from pathlib import Path
from datetime import datetime

workpath = (Path(__file__).parent.absolute())
now = datetime.now()
dt_string = now.strftime("[%d.%m.%Y %H:%M:%S]")

LoadAddons()

while True:
    args = []
    try:
        input = prompt(promt, style=style)
        command = input.split(' ')
        command = [x for x in command if x]
        args.extend(command)
        try:
            del args[0]
            command = ''.join(command[:1])
            args_str = ' '.join(args)
            input = " " + command + " " + args_str
            if command != "history" and command != "clear" and command != "exit" and command != []:
                try:
                    with open('usr/logs/commands.log', 'a') as logs:
                        logs.write(dt_string + f'{input}\n')
                except FileNotFoundError:
                    warn("Logs wasn't found...")
                    info("Generating logs")
                    logs_path = (str(workpath) + "/usr/logs")
                    os.mkdir(logs_path)
                    with open('usr/logs/commands.log', 'a') as logs:
                        logs.write(dt_string + f'{input}\n')
            if command == "help":
                if args == []:
                    file = open("usr/docs/help.txt", 'r')
                    print(file.read())
                    file.close()
                else:
                    HelpModule(args)
            elif not command:
                print()
            elif command == "exit":
                OnExit()
            elif command == "plugins":
                GetList()
            elif command == "restart" or command == "reload":
                subprocess.run(["python3", "terminator.py"], check=True)
                OnExit()
            elif command == 'history':
                if len(args) == 0:
                    with open('usr/logs/commands.log', 'r') as logs:
                        print(*(command_ for command_ in logs.readlines()))
                elif len(args) == 1 and args[0] == "-c" or args[0] == "--clear":
                    with open('usr/logs/commands.log', 'w') as logs:
                        logs.seek(0)
                else:
                    error("History don't get more that one argument")
            elif command == 'about':
                AboutModule(args)
            elif command == "clear":
                subprocess.run("clear", check=True)
            else:
                # Run plugin if it's exist
                if UseModule(command) != 0:
                    pass
                else:
                    error('Command does not exist.',
                          'Enter "help" to see a list of supported commands')
        except IndexError:
            pass
    except KeyboardInterrupt:
        warn('Enter "exit" to exit')
