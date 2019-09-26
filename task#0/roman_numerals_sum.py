import re

stand = {'M': 1000, 'D': 500,
        'C': 100, 'L': 50,  'X': 10,
         'V': 5, 'I': 1}
complex_romans = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
#This pattern was taken from the web and little bit modified
search_pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|VI{0,3}|I{0,4}?)$'

re_pattern = re.compile(search_pattern)

def roman_to_int_conv(num1: str) -> int:
    '''
    :param num1: Shoud be valid roman numeral, as 'str' format ('III', 'VI' etc.)

    :return: A valid integer, as 'int' format (1, 2, 3, 4 etc.)
    '''

    if re.search(search_pattern, num1):#checks validity of roman numeral

        integers = [stand[symb] for symb in num1] #retrieves all integers from input string according to the standard


        if len(integers) == 1: # if case of single roman numerals(e.g. 'I', 'V','X', 'C' etc)
            return integers[0] # it directly returns them

        temp_list = []
        try:
            for item in integers:
                ind = integers.index(item)

                if item < integers[ind+1]:
                    item = integers[ind+1] - item
                    temp_list.append(item)

                elif item == integers[ind+1]:
                    temp_list.append(item)

                else:
                    if item not in temp_list:
                        temp_list.append(item)
        except IndexError:
            pass
    else:
        raise ValueError('Invalid roman numeral')

    return sum(temp_list)

#Uncomment following to test the converter
#x = roman_to_int_conv('MCMXL')
#print(x)

def from_int_to_roman(num: int) -> 'str, roman numeral(X, V, I...)':

    reverse_stand = {v: k for k, v in stand.items()}

    reverse_stand.update({v: k for k, v in complex_romans.items()})

    general = dict(sorted(reverse_stand.items(), key=lambda x: x[0], reverse=True))

    roman = ''

    for key in general.keys():
        if num > key:
            roman += num // key * general[key]
            num = num % key
        elif num == key:
            roman += general[key]
            break
    return roman

def roman_numerals_sum(num1: str, num2: str, roman_view=True) -> int:
    '''
    Calculates the sum of two roman numerals

    :return: the sum of two roman numerals as Integer
    :roman_view=True, if it is False the result will be expressed in int format
    '''

    if isinstance(num1, str) and isinstance(num2, str):
        if roman_view:
            return from_int_to_roman(roman_to_int_conv(num1) + roman_to_int_conv(num2))
        else:
            return roman_to_int_conv(num1) + roman_to_int_conv(num2)
    else:
        raise TypeError('Both arguments should be in the string format')

if __name__ == '__main__':
    assert roman_numerals_sum('M', 'X') == 'MX'
    assert roman_numerals_sum('V', 'V') == 'X'
    