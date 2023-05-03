import json
import os

# Словарь глаголов (verb)
verb = {'3-5':{'name':'Глаголы 3, 4, 5 классов', 'word':{}},
        'fras':{'name':'Фразовые глаголы', 'word':{}},
        'modl':{'name':'Модальные глаголы', 'word':{}},
        'nepr':{'name':'Неправильные глаголы', 'word':{}},
        'prav':{'name':'Правильные глаголы', 'word':{}}
        }
file_list = os.getcwd()
json_files = [file_list+'/app/word_collection1/word_3-5.json',
              file_list+'/app/word_collection1/word_gl_fras.json',
              file_list+'/app/word_collection1/word_gl_modl.json',
              file_list+'/app/word_collection1/word_gl_nepr.json',
              file_list+'/app/word_collection1/word_gl_pr.json']

for i in range(5):
    with open(json_files[i], 'r') as file:
        data = json.load(file)
        if i == 0:
            verb['3-5']['word'].update(data)
        if i == 1:
            verb['fras']['word'].update(data)
        if i == 2:
            verb['modl']['word'].update(data)
        if i == 3:
            verb['nepr']['word'].update(data)
        if i == 4:
            verb['prav']['word'].update(data)

if __name__ == "__main__":
    # print(list(verb.get('correct').keys()))
    print(list(verb.keys()))
    for i in list(verb.keys()):
        print(verb[i]['name'])
        print(len(verb[i]['word']))
    # print(verb['3-5']['word'])
    file_list = os.getcwd()
    print(file_list)