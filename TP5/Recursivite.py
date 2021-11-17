
def remove_vowels(s):
    """
    >>> remove_vowels("Ceci est un test")
    'Cc st n tst'
    >>> remove_vowels("Bonjour")
    'Bnjr'
    """
    if(len(s)!=1):
        if s[0] in "aeiouy": return ""+remove_vowels(s[1:])
        else:
            return s[0]+remove_vowels(s[1:])
    else:
        if s[0] in "aeiouy": return ""
        else:
            return s[0]
