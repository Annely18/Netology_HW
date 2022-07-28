import os

CATALOG_NAME = 'HW_files3' # - имя каталога куда пишем
BASE_PATH = os.getcwd()   # - базовый путь
origin_files = os.listdir() # - список исходных файлов
full_path = os.path.join(BASE_PATH, CATALOG_NAME, 'result_file')


def file_reader(file_names):
    file_name_list = [x for x in file_names if '.txt' in x]
    dict_ = {}
    for file_name in file_name_list:
        values = []
        with open(file_name, encoding='utf-8') as file_obj:
            file_len = len(file_obj.readlines())
            values.append(file_len)
        with open(file_name, encoding='utf-8') as file_obj:
            for item in range(file_len):
                file_content = file_obj.readline().strip()
                values.append(file_content)
            dict_[file_name] = values
    sorted_dict = {}
    sorted_keys = sorted(dict_, key=dict_.get)
    for w in sorted_keys:
        sorted_dict[w] = dict_[w]
    return sorted_dict


print(file_reader(origin_files))


# КОД ДЛЯ ЗАПИСИ В ФАЙЛ

def file_writer(new_file, dict_):
    with open(new_file, 'a', encoding='utf-8') as file_obj:
        for key, value in dict_.items():
            str3 = '\n'.join(value[1:])
            file_obj.write(f'{key}\n{value[0]}\n{str3}\n')


file_writer(full_path, file_reader(origin_files))
