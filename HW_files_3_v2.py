import os

CATALOG_NAME = 'HW_files3' # - имя каталога куда пишем
BASE_PATH = os.getcwd()   # - базовый путь
origin_files = os.listdir() # - список исходных файлов
full_path = os.path.join(BASE_PATH, CATALOG_NAME, 'result_file2')
new_file = full_path


def file_worker (origin_files, res_file_path):
    file_name_list = [x for x in origin_files if '.txt' in x]
    dict_ = {}
    for file_name in file_name_list:
        len_list = []
        with open(file_name, encoding='utf-8') as file_obj_r:
            file_len = len(file_obj_r.readlines())
            len_list.append(file_len)
        with open(file_name, encoding='utf-8') as file_obj_rr:
            for item in range(file_len):
                file_content = file_obj_rr.readline().strip()
                len_list.append(file_content)
            dict_[file_name] = len_list
    sorted_keys = sorted(dict_, key=dict_.get)
    sorted_dict = {}
    for w in sorted_keys:
        sorted_dict[w] = dict_[w]
    with open(new_file, 'a', encoding='utf-8') as file_obj_w:
        for key, value in sorted_dict.items():
            str3 = '\n'.join(value[1:])
            file_obj_w.write(f'{key}\n{value[0]}\n{str3}\n')

file_worker(origin_files, new_file)
