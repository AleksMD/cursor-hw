import re

stand = {'M': 1000, 'D': 500,
        'C': 100, 'L': 50,  'X': 10,
         'V': 5, 'I': 1}
#This pattern was taken from the network and little bit modified
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

def roman_numerals_sum(num1: str, num2: str) -> int:
    '''
    Calculates the sum of two roman numerals

    :return: the sum of two roman numerals as Integer
    '''

    if isinstance(num1, str) and isinstance(num2, str):
        return roman_to_int_conv(num1) + roman_to_int_conv(num2)

    else:
        raise TypeError('Both arguments should be in the string format')

#Uncomment following to test the summator:
#roman_sum = roman_numerals_sum('X', 'M')
#print(roman_sum)
