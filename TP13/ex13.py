# Vos imports ici..
import urllib.request
import parser
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    # Votre classe ici
    def __init__(self):
        super.__init__()
    def handle_starttag(self, tag, attrs):
        print("<< Trouvé balise ouvrante :", tag)
    def handle_endtag(self, tag):
        print(">> Trouvé balise fermante :", tag)
    def handle_data(self, data):
        if data.strip(): print("    Trouvé contenu  :", data)

def scrap_imdb(html_data):
    """
    Extrait la liste de film contenue dans html_data.

    Args:
        html_data: source de la page html

    Returns:
        Liste de films
    """
    # Votre code ici...
    parser = MyHTMLParser()
    u = urllib.request.urlopen('https://www.imdb.com/chart/top?ref_=nv_ch_250_4')
    data = u.read().decode('utf8')
    parser.feed(data)
    return []
    
        
def main(url):
    """
    >>> with open("IMDb.html", mode='r', encoding='utf8') as f: html_data = f.read()
    >>> movies =  scrap_imdb(html_data)
    >>> for m in movies[:5]: print(m)
    Les évadés
    Le parrain
    Le parrain, 2ème partie
    The Dark Knight: Le chevalier noir
    12 hommes en colère
    >>> for m in movies[-5:]: print(m)
    Lagaan
    L'ultime razzia
    Gangs of Wasseypur
    La douceur de vivre
    In the Mood for Love
    """
    # Votre code ici...
    
    # proxy_address = 'http://147.215.1.189:3128/'
    # proxy_handler = urllib.request.ProxyHandler({'http': proxy_address})
    # opener = urllib.request.build_opener(proxy_handler)
    # urllib.request.install_opener(opener)
    
    return None

if __name__ == '__main__':
    main('http://www.imdb.com/chart/top?ref_=nv_ch_250_4')
