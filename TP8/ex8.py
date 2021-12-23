# Vos import ici...
from zipfile import ZipFile, is_zipfile

ARCHIVE = 'meteofrance2014.zip'

def extract_temp(date, code):
    """
    retourne la liste des températures pour la date et la station météo passées en arguments 

    Args:
        date: une date au format AAAAMMJJ
        code: code de la station météo

    Returns:
        liste des températures en degrés Celsius
        
    >>> print(extract_temp('20140109', '07005')) # Abbeville le 9 janvier 2014
    [11.2, 11.6, 11.8, 11.0, 9.6, 8.2, 7.9, 6.8]
    >>> print(extract_temp('20140317', '07110')) # Brest le 17 mars
    [7.2, 7.3, 7.2, 7.5, 8.7, 9.8, 8.5, 7.9]
    >>> print(extract_temp('20140623', '07434')) # Limoges le 23 juin 2014
    [20.2, 17.0, 16.1, 16.1, 18.2, 17.6, 16.3, 15.0]
    >>> print(extract_temp('20140815', '07761')) # Ajaccio le 15 aout 2014
    [18.2, 16.7, 17.8, 25.8, 25.5, 24.9, 22.5, 19.4]
    >>> print(extract_temp('20140703', '89642')) # Terre Adélie le 3 juillet 2014
    [-17.7, -19.2, -18.7, -19.6, -20.4, -20.8, -23.3, -23.3]
    >>> print(extract_temp('20140703', '12345')) # Station inconnue
    []
    >>> print(extract_temp('20150703', '89642')) # date non comprise dans l'archive
    []
    """
    
    # votre code ici...
    fichier = "synop."+str(date[0:6])+".csv"

    zip = ZipFile("data/"+ARCHIVE)

    test = fichier in ZipFile.namelist(zip)
    if test == False:
        return []
    
    data = zip.read(fichier).decode('utf8')

    l = data.split()

    temps = []

    for i in range (1,len(l)):
        a = l[i].split(";")
        if a[0] == code and a[1][0:8] == date:
            temp = float(a[7])-273.15
            temps.append(round(temp, 1))
    return temps

def main():
    print(extract_temp('20150703','89642'))
    return
    
if __name__ == '__main__':
    # ... votre code de test ici
    main()