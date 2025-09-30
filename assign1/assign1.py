import time
import argparse
import textwrap

# todo
# make the frequencies prettier and add each letter
# the program should have an option to display a histogram of the frequences
# [optional] the program should have an option to skip the parts of the text
#  that do not pertain to the book (e.g., preamble and license)
# think of more book stats

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
parser.add_argument('filename', help='name of the file to process')
parser.add_argument('--skips', action='store_true',  help='allows skipping the parts of the text not pertaining to the book')
parser.add_argument('--histo', action='store_true',  help='displays a histogram of the frequencies')
parser.add_argument('--totc', action='store_true',  help='displays the total number of characters')
parser.add_argument('--totw', action='store_true',  help='displays the total number of words')
parser.add_argument('--totl', action='store_true',  help='displays the total number of lines')
args = parser.parse_args()
fname = args.filename

EachCount = [0] * 26 ## Altrimenti, importando numpy, np.zeroes(26)
letters = 'abcdefghijklmnopqrstuvwxyz'
lcount = 0

a = {'a','à','á','â'}
e = {'e','è','é','ê'}
i = {'i','î','ì','í'}
o = {'o','ô','ò','ó'}
u = {'u','û','ú','ù'}

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
        
    with open(fname, 'r', encoding='utf-8') as fhandle:
        if args.totl:
            TotLines = 0
            for line in fhandle:
                NonEmptyLine = line.strip()
                if NonEmptyLine: 
                    TotLines+=1
            print('The total number of lines is: ', TotLines)

    with open(fname, 'r', encoding='utf-8') as fhandle:
        if args.totw:
            TotWords = 0
            for line in fhandle:
                ThisLineWords = len(line.split())
                TotWords += ThisLineWords
            print('The total number of words is: ', TotWords)
    
    print('The elapsed time is: ', f'{end:.2f}', 'seconds')
except FileNotFoundError:
    print('Could not find', fname, '\b.')    
