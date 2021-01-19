import requests

def get_list():
    data = get_manga_by_team()
    mangas = []
    for team in data:
        for manga in team['mangas']:
            mangas.append(manga)
            mangas[-1]['team'] = team['name']
    
    return mangas

def get_manga_by_team():
    req = requests.get("https://gs-nation.com/LGsNation/public/getMangaByTeam")
    data = req.json()['succes']
    return data

def get_manga_by_id(id):
    req = requests.post("https://gs-nation.com/LGsNation/public/getMangaById", {"id":id})
    data = req.json()['succes']
    return data

def get_chapter(mangas_id, chapter_id):
    req = requests.post("https://gs-nation.com/LGsNation/public/GetScan", {"manga_id" : mangas_id, "chapter": chapter_id})
    data = req.json()['result'][0]

    data['pages'] = []

    min = int(data['MinScan'])
    max = int(data['CountScan'])

    for page in range(min,max):
        url = data['patch_scan'] + "{}.jpg".format(page)
        data['pages'].append(url)

    return data

def get_name_by_id(id):
    req = requests.post("https://gs-nation.com/LGsNation/public/getMangaById", {"id":id})
    data = req.json()['succes']['name']

    return data