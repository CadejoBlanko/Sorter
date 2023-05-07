import os
import sys
import shutil
from pathlib import Path



def folder_creation(path_f):

    path_f = Path(path_f)

    Path(f'{str(path_f)}/' + 'images').mkdir(parents=True, exist_ok=True)
    Path(f'{str(path_f)}/' + 'documents').mkdir(parents=True, exist_ok=True)
    Path(f'{str(path_f)}/' + 'audio').mkdir(parents=True, exist_ok=True)
    Path(f'{str(path_f)}/' + 'video').mkdir(parents=True, exist_ok=True)
    Path(f'{str(path_f)}/' + 'archives').mkdir(parents=True, exist_ok=True)

    sorter(path_f, path_f)



def normalize(string_name):

    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e',
        'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i',
        'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu',
        'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D',
        'Е': 'E', 'Є': 'Ie', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'I',
        'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
        'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
        'Ю': 'Iu', 'Я': 'Ia'
    }

    name_object = ''
    
    for char in string_name:

        if char.isalnum():
            if char in translit_dict:
                name_object += translit_dict[char]
            elif char.lower() in translit_dict:
                name_object += translit_dict[char.lower()].capitalize() if char.isupper() else translit_dict[char.lower()]
            else:
                name_object += char
        else:
            name_object += '_'

    return name_object



def translit(ob_traslit):

    for ob in ob_traslit.iterdir():

        if ob.is_dir():
            translit(ob)

        name, format = os.path.splitext(ob.name)
        new_name = os.path.join(ob_traslit, (normalize(name) + format))
        
        if ob.name != new_name:
            os.rename(ob, new_name)



def sorter(folder, path_f):
    
    for el in folder.iterdir():

        if el.is_file() and el.suffix == ".jpeg" or el.suffix == ".png" or el.suffix == ".jpg" or el.suffix == ".svg":
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'images', el.name))

        elif el.is_file() and el.suffix == ".doc" or el.suffix == ".docx" or el.suffix == ".txt" or el.suffix == ".pdf" or el.suffix == ".xlsx" or el.suffix == ".pptx": 
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'documents', el.name))

        elif el.is_file() and el.suffix == ".mp3" or el.suffix == ".ogg" or el.suffix == ".wav" or el.suffix == ".amr":
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'audio', el.name))

        elif el.is_file() and el.suffix == ".avi" or el.suffix == ".mp4" or el.suffix == ".mov" or el.suffix == ".mkv":
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'video', el.name))

        elif el.is_file() and el.suffix == ".zip" or el.suffix == ".gz" or el.suffix == ".tar":
   
            name_archive = (el.name).split(".")
            Path(f'{str(path_f)}/' + 'archives/' + name_archive[0]).mkdir(parents=True, exist_ok=True)
            shutil.unpack_archive(el, f'{str(path_f)}/' + 'archives/' + name_archive[0])

        elif el.is_dir():

            if el.name == 'images' or el.name == 'documents' or el.name == 'audio' or el.name == 'video' or el.name == 'archives':
                pass
            elif len(os.listdir(el)) != 0:
                sorter(el, path_f)
            else:
                os.rmdir(el)  

    translit(folder)



folder_creation(sys.argv[1])