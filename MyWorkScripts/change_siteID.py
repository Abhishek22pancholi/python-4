#Import modułów
import os, sys
import zipfile

#Deklaracja funkci i  parametrów
def change_SiteId(new_SiteId):
#Wygenerwoanie oraz przypisanie do listy elementów zip znajdujących się w folderze
    file_list = [f for f in os.listdir(path='.') if zipfile.is_zipfile(os.path.join('.',f))]
#Pętla po lsicie plików
    for zip_files in file_list:
#Pobranie zip`a oraz otworżenie zipa
        with zipfile.ZipFile(zip_files) as enty_file:
#Wypakowanie pliku z wnętrza zip`a
            enty_file.extract('enty')
#Otawrcie pliku w trybie zapisu
            old_content =[]
            with open('enty', 'r') as f:
                for line in f:
                    if line.startswith('<SiteId>'):
                        line = '<SiteId>' + str(new_SiteId) + '</SiteId>' 
                    old_content.append(line)
#Zamiana lini tekstu na parametr
            with open('enty', 'w') as d: 
#Zapisanie pliku
                new_content = "".join(old_content) 
                d.write(new_content)
#Nadpisanie zipa
        with zipfile.ZipFile(zip_files, 'w') as enty_file:
            enty_file.write('enty')
        os.remove('enty')
#zwrucenie komunikatu o pwodzeniu lub nie
    return "Wykonano"
