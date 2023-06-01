import sys
import os
import pydoc


def get_py_modules():
    py_modules = {}
    # print(sys.stdlib_module_names)
    # Извлекаем все встроенные модули Python из sys.modules и создаем словарь
    # с их описанием на английском и русском
    for name in sorted(sys.stdlib_module_names):
    # for name in sorted(sys.builtin_module_names):
        print(name)
        if name.startswith('_'):
            continue
        py_modules[name] = name.__doc__
    print(py_modules)

get_py_modules()
# print(os.__doc__)