from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from .stylegan2 import pretrained_networks
from .stylegan2 import align_images, project_images
from PIL import Image
import dnnlib
import dnnlib.tflib as tflib
from pathlib import Path
import numpy as np
import shutil
import os
import glob

def index(request):
        return render(request, 'toonifyApp/index.html')


def cleanDir(path):
    dirpath = Path(__file__).resolve().parent.parent/"toonifyApp/stylegan2"
    path = path+"/*"
    files = glob.glob(str(dirpath/path))
    for f in files:
        os.remove(f)

def api_toonify(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        #TODO TOONIFY HERE
        #ffhq_url = Path(__file__).resolve().parent.parent/"static/libs/stylegan2-ffhq-config-f.pkl"
        blended_url = Path(__file__).resolve().parent.parent/"static/libs/ffhq-cartoon-blended-64.pkl"

        _, _, Gs_blended = pretrained_networks.load_networks(blended_url)
        #_, _, Gs = pretrained_networks.load_networks(ffhq_url)
        outfile = ""
      
        align_images.setup()
        project_images.main()
        latent_dir = Path(__file__).resolve().parent.parent/"toonifyApp/stylegan2/generated"
        latents = latent_dir.glob("*.npy")
        for latent_file in latents:
            latent = np.load(latent_file)
            latent = np.expand_dims(latent,axis=0)
            synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=False), minibatch_size=8)
            images = Gs_blended.components.synthesis.run(latent, randomize_noise=False, **synthesis_kwargs)
            imgToon = Image.fromarray(images.transpose((0,2,3,1))[0], 'RGB').save(latent_file.parent / (f"{latent_file.stem}-toon.jpg"))
            filename = img.name[:-4]
            filename = filename + "_01-toon.jpg"
            source = Path(__file__).resolve().parent.parent/"toonifyApp/stylegan2/generated"/filename
            output = Path(__file__).resolve().parent.parent/"toonifyApp/stylegan2/raw"/filename
            shutil.copy2(source ,Path(__file__).resolve().parent.parent/"static/outfile")
            outfile = "/static/outfile/"+filename
        
        cleanDir("generated")
        cleanDir("aligned")
        cleanDir("raw")

        return HttpResponse(outfile)
    else:
        return HttpResponse("Invalid call")
