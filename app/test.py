import sys
import pydoc


def get_py_modules():
    py_modules = {}

    # Извлекаем все встроенные модули Python из sys.modules и создаем словарь
    # с их описанием на английском и русском
    for name, obj in sys.modules.items():
        if name.startswith("_") or not obj:
            continue
        en_doc = obj.__doc__
        ru_doc = ""
        # if en_doc:
        #     # Извлекаем описание на русском языке, если оно есть
        #     en_doc_lines = en_doc.split("\n")
        #     if (len(en_doc_lines) > 1 and en_doc_lines[1].startswith("    ")):
        #         en_doc = "\n".join([en_doc_lines[0]] + en_doc_lines[2:])
        py_modules[name] = {"description_en": en_doc, "description_ru": ru_doc}

    # Возвращаем словарь со всеми встроенными модулями Python и их описанием
    return py_modules

print(list(get_py_modules().keys()))