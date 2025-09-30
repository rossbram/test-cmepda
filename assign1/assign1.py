import time
import argparse
import textwrap

parser = argparse.ArgumentParser(
                    prog='VeryCoolLetterCounter',
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description=textwrap.dedent('''\
                    ! This is a Very Cool Letter Counter !
                    .₊ ⊹ ˖ .. ݁₊ ⊹ ˖ . . ݁₊ ⊹ ˖ . . ݁₊ ⊹ ˖  ݁₊.
                    This is the program I made for Assignment 1 of the UniPi CMEPDA course.
                    You can input a book as a .txt file from command line when executing it. 
                    The program can do some cool stuff with it, such as:
                    - Computing the relative frequence of each letter of the alphabet 
                      (without distinguishing between lower and upper case, accents included!) [default]
                    - Displaying a histogram of such frequencies
                    - Skipping the parts of the text not pertaining to the book, such as the
                      preamble or the license
                    - Printing out some interesting stats, such as the total number of
                      characters, total number of words, total number of lines.
                    .₊ ⊹ ˖ .. ݁₊ ⊹ ˖ . . ݁₊ ⊹ ˖ . . ݁₊ ⊹ ˖  ݁₊.
                    '''),
                    epilog='Text at the bottom of help')
parser.add_argument('--skips', help='allows skipping the parts of the text not pertaining to the book')
parser.add_argument('--histo', help='displays a histogram of the frequencies')
parser.add_argument('--totc', help='displays the total number of characters')
parser.add_argument('--totw', help='displays the total number of words')
parser.add_argument('--totl', help='displays the total number of lines')
args = parser.parse_args()


EachCount = [0] * 26 ## Altrimenti, importando numpy, np.zeroes(26)
letters = 'abcdefghijklmnopqrstuvwxyz'
lcount = 0
a = {'a','à','á','â'}
e = {'e','è','é','ê'}
i = {'i','î','ì','í'}
o = {'o','ô','ò','ó'}
u = {'u','û','ú','ù'}

fname = input('Enter your file name: ')
start = time.time()
try:
    with open(fname, 'r', encoding='utf-8') as fhandle:
        text = fhandle.read().lower()
        for l in letters:
            lcount = 0
            if l == 'a':
                lcount = sum(1 for ch in text if ch in a)
            elif l == 'e':
                lcount = sum(1 for ch in text if ch in e)
            elif l == 'i':
                lcount = sum(1 for ch in text if ch in i)
            elif l == 'o':
                lcount = sum(1 for ch in text if ch in o)
            elif l == 'u':
                lcount = sum(1 for ch in text if ch in u)
            else:
                lcount = sum(1 for ch in text if ch == l)
            EachCount[letters.find(l)] = lcount
    TotCount = sum(EachCount)
    EachFrequence = [x * 100 / TotCount for x in EachCount]
    EFNice = [f'{x:.2f}%' for x in EachFrequence]
    end = time.time() - start
    print(*EFNice, sep=', ')
    print('The total number of letters is: ', TotCount)
    print('The elapsed time is: ', f'{end:.2f}', 'seconds')
except FileNotFoundError:
    print('Could not find', fname, '\b.')
