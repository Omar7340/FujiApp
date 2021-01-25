import requests
from datetime import date, timedelta

def get_list():
    data = get_manga_by_team()
    mangas = []
    for team in data:
        for manga in team['mangas']:
            mangas.append(manga)
            mangas[-1]['team'] = team['name']
    
    return mangas

# mardi yyyy-mm-dd
def formatDate(givenDate):
    date_iso = date.fromisoformat(givenDate[-10:])
    return date_iso.strftime("%A %d %B %Y")

# start => yyyy-mm-dd
# each request give 3 days
# so if you give 7 as parameter
# this function gives you the 7*3= 21 latest days
def get_latest(nb_days_pack_by_3):
    start = date.today()
    data = []
    for i in range(nb_days_pack_by_3):
        str_start = start.isoformat()
        req = requests.post("https://gs-nation.com/LGsNation/public/GetNextDay", {"date":str_start})
        data = data + req.json()['result']
        start = start - timedelta(days=3)
        req = ""
    
    bibliotheque = []
    for days in data:
        mangas = { "date": formatDate(days[0]), "mangas": days[1]}
        for item in mangas["mangas"]:
            item["mangas"] = item["mangas"][0]
        bibliotheque.append(mangas)

    return bibliotheque

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

    min = 0
    max = int(data['total_chapter'])

    for page in range(min,max+1):
        url = data['patch_scan'] + "{}.jpg".format(page)
        data['pages'].append(url)

    return data

def get_name_by_id(id):
    req = requests.post("https://gs-nation.com/LGsNation/public/getMangaById", {"id":id})
    data = req.json()['succes']['name']

    return data

def get_list_slug_chapters(id):
    req = requests.post("https://gs-nation.com/LGsNation/public/getMangaById", {"id":id})
    data = req.json()['succes']

    chapters = []
    for chapter in data['scans']:
        chapters.append(chapter['chapter'])

    return chapters

def get_count_chapters(id):
    req = requests.post("https://gs-nation.com/LGsNation/public/getMangaById", {"id":id})
    data = req.json()['succes']
    return len(data['scans'])