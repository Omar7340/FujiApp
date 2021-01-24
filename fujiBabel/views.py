from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from .sources import gsNation

# Create your views here.
title = "Babel"

def get_menu(active=None):
    menu = {
        "index":{
            "name": "Mangas",
            "url": reverse("babel:index")
        },
        "latest":{
            "name": "Nouvelle sorties",
            "url": reverse("babel:latest")
        }}

    if active:
        menu[active]['active'] = True
    return menu


def index(request):
    bibliotheque = gsNation.get_list()

    for mangas in bibliotheque:
        mangas['url'] = reverse("babel:detail", args=[mangas['id']])

    menu = get_menu("index")
    
    return render(request, "index.html", { 'title': title, 'bibliotheque':bibliotheque, 'menu':menu })

def latest(request):
    return HttpResponse("not yet")

def detail(request, id):
    mangas = gsNation.get_manga_by_id(id)
    title = mangas["name"]
    for chapter in mangas['scans']:
        chapter['url'] = reverse("babel:read", args=[id,chapter['chapter']])

    menu = get_menu()
    return render(request, "detail.html", { 'title': title, 'mangas':mangas, 'menu': menu})

def read(request, mangas_id, chapter_id):
    chapter = gsNation.get_chapter(mangas_id, chapter_id)
    chapter['manga_name'] = gsNation.get_name_by_id(mangas_id)
    title = chapter['manga_name']
    chapter['slugs'] = gsNation.get_list_slug_chapters(mangas_id)

    min_chap = int(chapter['slugs'][0])
    max_chap = gsNation.get_count_chapters(mangas_id)
    
    if(chapter_id < max_chap - 1):
        chapter['next'] = reverse("babel:read", args=[mangas_id, chapter_id+1])
    if(chapter_id > min_chap):
        chapter['prev'] = reverse("babel:read", args=[mangas_id, chapter_id-1])
    
    menu = get_menu()
    return render(request, "reader.html", { 'title': title, 'chapter': chapter, 'menu':menu})
