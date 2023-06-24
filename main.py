import os
import shutil

def get_text_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(current_dir)
    text_files = [file for file in files if file.endswith('.txt')]
    return text_files

def search_text_in_files(text):
    text_files = get_text_files()
    found_files = []

    for file_name in text_files:
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()
            if text in file_content:
                found_files.append(file_name)

    return found_files

def move_files_to_folder(files, folder_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    destination_dir = os.path.join(current_dir, folder_name)

    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    for file_name in files:
        source_path = os.path.join(current_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)
        shutil.move(source_path, destination_path)
        print(f"Файл {file_name} перенесен в папку {folder_name}")

search_text = input("Введите текст для поиска: ")  
found_files = search_text_in_files(search_text)


if found_files:
    destination_folder = input("Введите название папки, в которую нужно перенести файлы: ")
    move_files_to_folder(found_files, destination_folder)
else:
    print("Файлы с искомым текстом не найдены.")
