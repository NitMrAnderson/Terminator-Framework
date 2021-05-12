import os
import sys
import pathlib
import glob
import configparser
import toml
import importlib.util

workpath = (pathlib.Path(__file__).parent.absolute())
config = configparser.ConfigParser()
path = str(workpath) + "/bin"
onload = True


def get_all_values(d):
    if isinstance(d, dict):
        for v in d.values():
            yield from get_all_values(v)
    elif isinstance(d, list):
        for v in d:
            yield from get_all_values(v)
    else:
        yield d

def LoadAddons(path=path, onload=onload):
    #Search all .addon files
    dot_addon_paths = []
    command_list = []
    addon_import_paths = []
    for x in os.walk(path):
        for y in glob.glob(os.path.join(x[0], '*.addon')):
            dot_addon_paths.append(y)
    # Create lists
    for x in dot_addon_paths:
        file = open(x, 'r')
        toml_string = file.read()
        parsed_toml = toml.loads(toml_string)
        command_list.append(parsed_toml["command"])
        addon_import_paths.append(os.path.dirname(x) + "/" + parsed_toml["main_file"])
        file.close()
    # Load a addons
    modules = []
    i = 0
    for path in addon_import_paths:
        try:
            spec = importlib.util.spec_from_file_location(command_list[i], path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if onload == True:
                module.OnLoad()
            else:
                pass
            modules.append(module)
            i += 1
        except AttributeError:
            print("Err! Module " + '"' + command_list[i] + '"' + " doesn't work correctly!")
            i += 1
    dictionary = dict(zip(command_list, modules))
    return dictionary

dictionary = LoadAddons(onload=False)

def GetList(dictionary = dictionary):
    command_list = dictionary.keys()
    for command in command_list:
        print(command)

def AboutModule(args, dictionary = dictionary):
    commands_in_dict = dictionary.keys()
    if len(args) == 1:
        command = "".join(args)
        if command in commands_in_dict:
            for commands_in_dict, module in dictionary.items():
                if command in commands_in_dict and commands_in_dict == command:
                    module.Info()
    else:
        print("This command actually don't need9 more then 1 argument")

def HelpModule(args, dictionary = dictionary):
    commands_in_dict = dictionary.keys()
    if len(args) == 1:
        command = "".join(args)
        if command in commands_in_dict:
            for commands_in_dict, module in dictionary.items():
                if command in commands_in_dict and commands_in_dict == command:
                    module.Help()
    else:
        print("This command need 1 argument")
        print('Argument may be "terminator" or plugin name')

def UseModule(command, dictionary=dictionary):
    commands_in_dict = dictionary.keys()
    if command in commands_in_dict:
        for commands_in_dict, module in dictionary.items():
            if command in commands_in_dict and commands_in_dict == command:
                module.OnCall()
    else:
        return 0

def OnExit(dictionary=dictionary):
    for commands_in_dict, module in dictionary.items():
        module.OnExit()
    sys.exit()
