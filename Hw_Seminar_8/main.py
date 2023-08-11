# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def calculate_directory_size(directory):
    total_size = 0

    for path, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)

    return total_size


def get_directory_info(directory):
    info_dict = {}

    for obj in os.listdir(directory):
        obj_path = os.path.join(directory, obj)

        if os.path.isdir(obj_path):
            info_dict[obj] = get_directory_info(obj_path)
            info_dict[obj]['type'] = 'directory'
            info_dict[obj]['size'] = info_dict[obj]['total_size']
        else:
            info_dict[obj] = {
                'type': 'file',
                'size': os.path.getsize(obj_path)
            }

    info_dict['total_size'] = calculate_directory_size(directory)
    return info_dict


def save_as_json(result_dict):
    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict, json_file, ensure_ascii=False, indent=5, sort_keys=True)


def save_as_csv(result_list):
    with open('result.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['parent', 'obj', 'type', 'size'])
        writer.writerows(result_list)


def save_as_pickle(result_list):
    with open('result.pkl', 'wb') as pickle_file:
        pickle.dump(result_list, pickle_file)


def check_directory(directory):
    result_dict = {directory: get_directory_info(directory)}
    result_list = create_result_list(result_dict[directory])

    save_as_json(result_dict)
    save_as_csv(result_list)
    save_as_pickle(result_list)


def create_result_list(info_dict, parent=None):
    result_list = []

    for obj, info in info_dict.items():
        if parent is not None:
            obj_path = os.path.join(parent, obj)
        else:
            obj_path = obj

        if isinstance(info, dict):
            if info['type'] == 'directory':
                result_list.append([obj_path, '', 'directory', info['total_size']])
                result_list.extend(create_result_list(info, obj_path))
            else:
                result_list.append([parent, obj, 'file', info['size']])

    return result_list


check_directory(r'D:\My education\Python Immersion\Seminar_8')
