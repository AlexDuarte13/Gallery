from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.decorators import login_required
import os, time, string ,glob
from PIL import Image

THUMBSIZE = 230, 153

PATH = "/home/alex/Pictures/" # Alterar para o directorio das fotos

HTML = PATH + "index.html"

TITLE = "Fotos" # Alterar para o titulo do site

ficheiro = open(HTML,"w")


# Create your views here.
def listar_imagens(request):
    imagens = ['Uma', 'Duas']  # retornar as fotos
    return render(request, 'galeria/listar_imagens.html', {"imagens": imagens})


def converter():
    os.chdir(PATH)
    for imagem in glob.glob("*.jpg"):
        img = Image.open(imagem)
        img.thumbnail(THUMBSIZE)
        if imagem[0:5] != "thumb":
            img.save('thumb.' + str(imagem), "JPEG")


def gerar():
    os.chdir(PATH)
    imgthumb = glob.glob("thumb.*")
    ficheiro.write(
        "<html><head><title>" + TITLE + "</title></head><body><font size=\"4\"><b><center>" + TITLE + "</b></font><br><br>")

    for thumb in imgthumb:
        thumb = '<a href=\"' + str(thumb).strip(
            'thumb.') + '\">' + '<img src=\"' + thumb + '\">' + '</img>' + '</a>' + ' '
        ficheiro.write(thumb)
    ficheiro.write("<br><br><font size=\"2\">Actualizado em " + time.strftime(
        "%d-%m-%Y %H:%M:%S") + "<br>Galeria - Script feito por <a href=\"mailto:alexmgarcia@tux-linux.net\" style=\"text-decoration:none\"><b>Alexandre Garcia</b></a> (c) 2006</font></center></body></html>")
    ficheiro.close()


converter()

gerar()