import sys
import pydoc


def get_py_modules():
    py_modules = {}
    # print(sys.stdlib_module_names)
    # Извлекаем все встроенные модули Python из sys.modules и создаем словарь
    # с их описанием на английском и русском
    # for name, obj in sys.modules['builtins']:
    #     print(name, obj)
    for i in sys.stdlib_module_names:
        if i.startswith('_'):
            continue
        print(i)
        if i == 'random':
            print(help(i))

get_py_modules()