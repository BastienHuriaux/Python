def check_password(password):
    """
    Teste la robustesse d'un password
    Args:
        password: chaine de caractères
    Returns:
        True or False
    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """
    # votre code ici...
    Taille, MinMaj, Chiffre = False, False, False
    if len(password) >= 10: Taille = True
    if password.islower()==False and password.isupper()==False and password.isdigit()==False:
        MinMaj = True
    for i in range (0,len(password)-1):
        if password[i].isdigit()==True:
            Chiffre=True
            break
    if Taille==True and MinMaj==True and Chiffre==True:
        return True
    return False

def main():
    # votre code de test ici...
    # 1. appel de la fonction sur un cas particulier
    # 2. affichage de la valeur de retour
    # Par exemple :
    # result = check_password('A1213pokl')
    # print(result)
    check_password('A1213pokl')
    check_password('bAse730onE')
    check_password('asasasasasasasaas')
    check_password('QWERTYqwerty')
    check_password('123456123456')
    check_password('QwErTy911poqqqq')
    pass

if __name__ == '__main__':
    main()