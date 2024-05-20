import os
import shutil

def remove_folder(folder_path):
    # Sprawdzamy, czy folder istnieje
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            # Usuwamy folder wraz z zawartością
            shutil.rmtree(folder_path)
            print(f'Folder "{folder_path}" został pomyślnie usunięty.')
        except Exception as e:
            print(f'Wystąpił błąd podczas usuwania folderu "{folder_path}": {e}')
    else:
        print(f'Folder "{folder_path}" nie istnieje.')