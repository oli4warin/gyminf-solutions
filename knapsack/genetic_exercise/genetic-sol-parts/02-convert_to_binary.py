def convert_to_binary(n):
    """
    Konvertiert eine natürliche Zahl in eine Binärzahl:
        Parameter:
            n: Eine natürliche Zahl (Integer)
        Rückgabewert:
            n als Binärzahl (String)
    """
    if n > 1:
        return convert_to_binary(n//2)+str(n%2)
    return str(n%2)
   
