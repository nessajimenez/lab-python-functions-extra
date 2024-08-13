%load_ext autoreload
%autoreload 2 

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    import re 

    unique_list = []
    for x in lst:
        if x in unique_list:
            pass 
        else:
             unique_list.append(x)
    return unique_list


def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    upper_count = 0    
    lower_count = 0
    for x in string:
        if x == " ":
            pass
        elif x .isupper() == True:
            upper_count += 1
        else:
            lower_count += 1
    count = (("Uppercase count:" + str(upper_count)),("Lowercase count:" + str(lower_count)))
    return count


import string

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    cleaned = []
    for element in sentence:
        if element.isalpha() == True:
            cleaned.append(element)
        elif element == " ":
            cleaned.append(element)
    cleaned = ''.join(cleaned)
    return cleaned


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    cleaned = []
    previous = ""
    count = 0
    
    for element in sentence:
        if element == " " and previous != " ":
            cleaned.append(element)
            previous = element
            count += 1
        elif element.isalpha() == True:
            cleaned.append(element)
            previous = element
        else:
            pass
        
    cleaned = ''.join(cleaned)
    return count




def add_f(*args):
    return sum(args)

def sub_f(*args):
    answer = args[0]  
    for x in args[1:]:
        answer -= x
    return answer

def div_f(*args):
    answer = 1
    for x in args:
        answer /= x
    return answer

def mult_f(*args):
    answer = args[0]  
    for x in args[1:]:
        answer /= x
    return answer

def calculate_f(operand, *args):
    if operand == "+":
        return add(*args)
    elif operand == "-":
        return sub(*args)
    elif operand == "/":
        return div(*args)
    elif operand == "*":
        return mult(*args)
    else:
        print(f"Error, unidentified operand: {operand}")
