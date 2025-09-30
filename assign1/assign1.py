import time
import argparse
import textwrap
import matplotlib.pyplot as plt

# todo
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
                    You input a book as a .txt file from command line when executing it. 
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
parser.add_argument('--asciiplot', action='store_true',  help='displays a histogram of the frequencies in ASCII')
parser.add_argument('--mplplot', action='store_true',  help='displays a histogram of the frequencies with matplotlib')
parser.add_argument('--totc', action='store_true',  help='displays the total number of characters')
parser.add_argument('--totw', action='store_true',  help='displays the total number of words')
parser.add_argument('--totl', action='store_true',  help='displays the total number of lines')
args = parser.parse_args()
fname = args.filename

EachCount = [0] * 26 ## could be np.zeroes(26) if importing numpy, but seems superfluous
letters = 'abcdefghijklmnopqrstuvwxyz' ## string that will be cycled though with the l variable later
lcount = 0 ## contains the total number of each letter which is counted in the cycle later

a = {'a','à','á','â'} ## yay for accented letters!
e = {'e','è','é','ê'}
i = {'i','î','ì','í'}
o = {'o','ô','ò','ó'}
u = {'u','û','ú','ù'}

start = time.time() ## stores the starting time
try:
    with open(fname, 'r', encoding='utf-8') as fhandle: ## without the encoding, the dialogue quotes break everything
        text = fhandle.read().lower() ## reads the file as one single piece, and lowercase
        for l in letters:
            lcount = 0
            if l == 'a': ## there's probably a cleaner way to do this but i can't quite think of it rn
                lcount = sum(1 for ch in text if ch in a) ## adds 1 to lcount for each character instance in the text that corresponds
                                                          ## to one of the characters in the list a (similarly for the other vowels)
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
            EachCount[letters.find(l)] = lcount ## each element in EachCount corresponds to a letter of the alphabet string
                                                ## this line adds the number of instances to the corresponding position in the array
        TotCount = sum(EachCount)   ## sums all the instances, so contains the total no. of characters excluding punctuaction&spaces
        EachFrequence = [x * 100 / TotCount for x in EachCount] ## again there's a correspondence w the alphabet
                                                                ##but now there's the frequency, not the plain number
        EFNice = [f'{x:.2f}%' for x in EachFrequence]   ## default formatting has tons of ugly decimals, this makes it cleaner
        print('The relative frequency of each letter is:')
        for l, value in zip(letters,EFNice):
                print(l.capitalize(), value)

        if args.asciiplot:
            print('\n\n')
            print("Here's an ASCII plot of the relative frequencies:")
            for l, value in zip(letters,EachFrequence):
                print(l.capitalize(), '•'*int(value*10))

    with open(fname, 'r', encoding='utf-8') as fhandle: ## the if doesn't work without specifying the with ... again
        if args.totl:
            TotLines = 0 ## initializing the line count to 0
            for line in fhandle:
                NonEmptyLine = line.strip() ## removes whitespaces, so the following if skips empty lines
                if NonEmptyLine: 
                    TotLines+=1
            print('The total number of lines is: ', TotLines)

    with open(fname, 'r', encoding='utf-8') as fhandle:
        if args.totw:
            TotWords = 0 ## initializing the word count to 0
            for line in fhandle:
                ThisLineWords = len(line.strip().split()) ## split generates an array with each word as an element
                                                          ## so its len is the no of words in the line
                                                          ## not sure if the .strip() is necessary but better safe than sorry
                TotWords += ThisLineWords
            print('The total number of words is: ', TotWords)

    with open(fname, 'r', encoding='utf-8') as fhandle:
        if args.totc:
            print('The total number of characters is: ', TotCount)

    end = time.time() - start ## compares w the starting time    
    print('The elapsed time is: ', f'{end:.2f}', 'seconds')

except FileNotFoundError:
    print('Could not find', fname, '\b.')    
