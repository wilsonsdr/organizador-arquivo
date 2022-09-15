# import de algumas bibliotecas necessárias
import os
import glob
import shutil

# adicione o nome da extensão que deseja, conforme o exemplo abaixo
extensoes = {
    "jpg": "jpg",
    "png": "png",
    "ico": "ico",
    "pdf": "pdf",
    "docx": "docx",
    "rar": "rar",
}

# pasta de origem dos arquivos a serem organizados
origem = r"/home/wilsonsdr/downloads"

# pasta de destino para onde os arquivos serão enviados, as pastas precisam estar criadas
dest1 = r"/home/wilsonsdr/documents/arquivos" 
dest2 = r"/home/wilsonsdr/pictures/imagens"
dest3 =  r"/home/wilsonsdr/documents/pdf" 

for extensoes in extensoes.items():
    # retorna as extensões adicionadas
    arquivos = glob.glob(os.path.join(origem, f"*.{extensoes}"))

    # variavel para o caminho de origem
    caminho = os.listdir(origem)

for arquivo in caminho:

    if (arquivo.endswith("rar") or arquivo.endswith("docx")):
                               # origem, arquivo,  pasta de destino 
        shutil.move(os.path.join(origem, arquivo), dest1)

    if (arquivo.endswith("jpg") or arquivo.endswith("png") or arquivo.endswith("ico") or arquivo.endswith("svg")):
        shutil.move(os.path.join(origem, arquivo), dest2)
    
    if (arquivo.endswith("pdf")):
        shutil.move(os.path.join(origem, arquivo), dest3)
