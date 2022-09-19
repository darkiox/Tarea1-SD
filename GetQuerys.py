from time import time
from unicodedata import name
import requests
from bs4 import BeautifulSoup

def Get_Query(data, id):
    keysw = ""
    keywords = data['keywords'].split(",")
    for kw in keywords:
        keysw += '\''+kw+'\','
    keysw = keysw[:-1]
    query = f'INSERT INTO urls (id,title,description,keywords,url) VALUES ({id}, \'{data["title"]}\', \'{data["description"]}\', ARRAY[{keysw}],\'{data["url"]}\');'
    with open('Querys.txt', 'a', encoding="utf-8") as f:
        f.write(query + '\n')
        id +=1

# Funcion obtenida desde el ayudante Joaquín Fernandez 
def getDataFromUrl(url):
    collected_data = {'url': url, 'title': None, 'description': None, 'keywords': None}
    try:
        r = requests.get(url, timeout=1)
    except Exception:
        return None

    if r.status_code == 200:
        
        # Se puede usar BeautifulSoap u otra librería que parsee la metadata de los docuementos HTML.
        source = requests.get(url).text
        soup = BeautifulSoup(source, features='html.parser')

        # Se otienes las etiquetas meta
        meta = soup.find("meta")
            
        # Obtenemos el título
        title = soup.find('title')
        #title = title['content'] if title else None
        
        # Obtenemos la descripción
        description = soup.find("meta", {'name': "description"})

        #description = description['content'] if description else None

        # Obtenemos la keywords y las limpiamos
        keywords = soup.find("meta", {'name': "keywords"})
        #keywords = keywords['content'] if keywords else None

        try:
            if keywords is None:
                return None
            else:
                description = description['content'] if description else None
                keywords = keywords['content'] if keywords else None
                
                keywords = keywords.replace(" ", "") if keywords else None
                keywords = keywords.replace(".", "") if keywords else None
                #keywords = keywords.split(",") if keywords else None  
                    
        except Exception:
            return None
        title = title.get_text().replace("\n","") if title else None
        title = title.replace("\r","") if title else None
        title = title.replace("\t","") if title else None
        collected_data['title'] = title
        collected_data['description'] = description
        collected_data['keywords'] = keywords 
        if collected_data['keywords'] is None:
            return None
        return collected_data
          
    return None

f = open("user-ct-test-collection-01.txt")
lines = f.readlines()
count = 0
for line in lines[1:]:
    line = line.split("\t")
    url = line[4][:-1]
    if "http" in url:
        data = getDataFromUrl(url)
        if data is not None:
            Get_Query(data,count)
            count += 1