## ToonifyProject

# Guide installation du projet

Prérequis :
  1. Installer [Python 3.7.9](https://www.python.org/downloads/release/python-379/)
  2. Installer [Visual studio 2017 community édition](https://visualstudio.microsoft.com/fr/free-developer-offers/)
  3. Ajouter le chemin à la variable d'environnement PATH (ex: `C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin`)

Procédure :
  1. Ouvrir un terminal de commande
  2. Executer `git clone https://github.com/foxyrs/ToonifyProject.git`
  3. Executer `cd ToonifyProject`
  4. Executer `Scripts\activate.bat`
  5. Executer `python -m pip install -e application\toonifyApp\stylegan2`
  6. Executer `pip install -r requirements.txt`
  7. Si le chemin de l'étape 4 du prérequis est différent, modifier la ligne `compiler_bindir_search_path` du fichier `ToonifyProject\application\toonifyApp\stylegan2\dnnlib\tflib\custom_ops.py`
  8. Installer [cuda 10.0](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal) 
  9. Télécharger la [librairie CuNn 7.4.1 pour Cuda 10.0](https://developer.nvidia.com/rdp/cudnn-archive)
  10. Ajouter les chemins à la variable d'environnement PATH (ex: `C:\Program Files (x86)\cudnn_10_0_v7_4_1_5\cuda\bin`) et (ex: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin`)
  11. Placer les fichiers `ffhq-cartoon-blended-64.pkl` et `stylegan2-ffhq-config-f.pkl` dans le dossier `ToonifyProject\application\static`
  12. Executer `python application/manage.py runserver`
  13. Ouvrir votre navigateur et aller à l'adresse: http://127.0.0.1:8000/toonifyApp/
