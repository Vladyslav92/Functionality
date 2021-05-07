import os
import shutil


def unpack_archives(paths):
    for arch in os.listdir(os.path.join(paths, 'archives')):
        archiv = 'archives'
        try:
            os.mkdir(f'{os.path.join(paths, archiv)}/{os.path.splitext(arch)[0]}')
            shutil.unpack_archive(os.path.join(os.path.join(paths, 'archives'), arch),
                                  os.path.join(os.path.join(paths, 'archives'), os.path.splitext(arch)[0]))
        except (FileExistsError, shutil.ReadError):
            continue


def normalize(name):
    trans = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
             'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
             'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
             'ъ': 'y', 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya', '`': '_', '~': '_', '!': '_',
             '@': '_', '#': '_', '$': '_', '%': '_', '^': '_', '&': '_', '*': '_', '(': '_', ')': '_',
             '-': '_', '=': '_', '+': '_', '{': '_', '}': '_', '[': '_', ']': '_', ';': '_', ':': '_', '|': '_',
             '"': '_', '/': '_', '?': '_', '>': '_', '<': '_', ',': '_',

             'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z',
             'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
             'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
             'Ъ': 'Y', 'Ы': 'Y', 'Ь': "'", 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
             }
    for i, j in trans.items():
        name = name.replace(i, j)
    return name


def del_empty_normalize_dirs(root_path, cur_path):
    for filename in os.listdir(cur_path):
        if os.path.isfile(os.path.join(cur_path, filename)):
            shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
        elif os.path.isdir(os.path.join(cur_path, filename)):
            del_empty_normalize_dirs(root_path, os.path.join(cur_path, filename))
    if cur_path != root_path:
        os.rmdir(cur_path)
    normalize_files(root_path)


def normalize_files(path):
    for file in os.listdir(path):
        shutil.move(os.path.join(path, file), os.path.join(path, normalize(file)))
    sort_unpack_files(path)


def sort_unpack_files(root_path):
    base = [('jpg', 'jpeg', 'png', 'svg'), ('avi', 'mp4', 'mov', 'mkv'), ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
            ('mp3', 'ogg', 'wav', 'amr'), ('zip', 'gz', 'tar')]
    for file in os.listdir(root_path):
        if file.endswith(base[0]):
            try:
                os.mkdir(f'{root_path}/photo')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'photo'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'photo'))
        elif file.endswith(base[1]):
            try:
                os.mkdir(f'{root_path}/video')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'video'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'video'))
        elif file.endswith(base[2]):
            try:
                os.mkdir(f'{root_path}/documents')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'documents'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'documents'))
        elif file.endswith(base[3]):
            try:
                os.mkdir(f'{root_path}/music')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'music'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'music'))
        elif file.endswith(base[4]):
            try:
                os.mkdir(f'{root_path}/archives')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'archives'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'archives'))
    unpack_archives(root_path)


def main():
    path = r'C:/Users/Владыка/Desktop/Разобрать'
    flag = r'C:/Users/Владыка/Desktop/Разобрать'
    return del_empty_normalize_dirs(path, flag)


if __name__ == '__main__':
    main()
