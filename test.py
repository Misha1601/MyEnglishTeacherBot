import builtins

def get_py_builtins():
    py_builtins = {}
    for name in dir(builtins):
        obj = getattr(builtins, name)

        # Исключаем методы и атрибуты, начинающиеся с "dunders"
        # и методы, заканчивающиеся на "_"
        if name.startswith("__") or name.endswith("_"):
            continue

        # Для каждого типа данных Python создаем словарь
        # с его описанием и списком его методов с описаниями
        if isinstance(obj, type):
            doc = obj.__doc__
            methods = {}
            for method_name in dir(obj):
                if method_name.startswith("__") or method_name.endswith("_"):
                    continue
                method_obj = getattr(obj, method_name)
                methods[method_name] = method_obj.__doc__
            py_builtins[name] = {"description": doc, "methods": methods}

    # Возвращаем JSON с встроенными типами данных Python, их описанием и методами с описаниями
    return py_builtins

print(get_py_builtins())
print(len(get_py_builtins()))
# x = get_py_builtins().keys()
# print(x)
print(get_py_builtins()['zip'])