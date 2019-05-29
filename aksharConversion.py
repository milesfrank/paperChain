import time
import binascii

def convert(starting, ending, number):
    total = 0
    for i in range(0,len(number)):
        digit = number[i]
        j = len(number)-i
        total+=digit*starting**(j-1)
    final = convertFrom10(ending, total)
    return final


def convertFrom10(ending, number): # converts 'number' to base 'ending'
    final = []
    counter = 1
    while True:
        if number==0:
            break
        digit = (number % (ending**counter))/ending**(counter-1)
        final.append(int(digit))
        number-=int(digit*(ending**(counter-1)))
        counter+=1
    return final[::-1]


def convertToHex(number):
    characters = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    array = convertFrom10(16, number)
    array = [str(characters[elem]) for elem in array]
    return ''.join(array)


def convertFromHex(text):
    characters = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    dictionary = {}
    number = 0
    for i in range(0,len(characters)):
        dictionary[str(characters[i])]=i
    for j in range(0,len(text)):
        number += dictionary[text[j]]*16**(len(text)-j-1)
    return number

def hexToText(text):
    return str(binascii.unhexlify(text))[2:-1]

def textToHex(text):
    return str(binascii.hexlify(str.encode(text)))[2:-1].upper()

# Functions below are the entire pipeline
def NumberToText(num):
    return hexToText(convertToHex(num))

def TextToNumber(text):
    return convertFromHex(textToHex(text))


# # Example Usage
# number = TextToNumber("Hi my name is Ian")
# print(number)

# # Example Usage 2
# text = NumberToText(number)
# print(text)

# # Text prints the same thing!