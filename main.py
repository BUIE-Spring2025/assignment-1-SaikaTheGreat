def int_to_roman(num):
    if type(num) != int:
        return None
    elif num <= 0:
        return None
    elif num >= 4000:
        return None
    roman_dict = {1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L"
              , 40 : "XL", 10 : "X", 9 : "IX", 5 : "V", 4 : "IV", 1 : "I"}
    numeros = ""
    for i, j in roman_dict.items():
        while num >= i:
            numeros += j
            num -= i
    return numeros

    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
