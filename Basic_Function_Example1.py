"""
Topic: Basic function and variants

Notes:
    Demo to show basic function usage
    along with while loops
"""


import sys
from time import sleep

def Add_One_V1(n):
    return n + 1


def Calc_Number(num):
    if num.find('.') != -1:
        zz = float(data)

    elif num.find('.') == -1:
        try:
            zz = int(data)
        except TypeError:
            print('Error! Number not detected.')
    
    return Add_One_V1(zz)


if __name__ == '__main__':

    while True:
        print('Please enter a number\nor press \'q\' to quit')
        data = input('>>> ')
        if data.lower() in ['q','quit','exit']:
            break
        else:
            xyz = Calc_Number(data)
            print('Your new number is: {0}'.format(xyz))

    print('Goodbye!')
    sleep(0.5)
    sys.exit(0)
