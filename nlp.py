import nltk
from nltk.tree import Tree
from tabulate import tabulate

articlePath = 'extractedArticles/sn90057049/7672/1967010601/a3.txt'

articleFile = open(articlePath, 'r')
article = articleFile.read()
articleFile.close()

tokens = nltk.word_tokenize(article)
tagged = nltk.pos_tag(tokens)
chunks = nltk.chunk.ne_chunk(tagged)

# ORGANIZATION	Georgia-Pacific Corp., WHO
# PERSON	    Eddy Bonte, President Obama
# LOCATION	    Murray River, Mount Everest
# DATE	        June, 2008-06-29
# TIME       	two fifty a m, 1:30 p.m.
# MONEY	        175 million Canadian Dollars, GBP 10.40
# PERCENT	    twenty pct, 18.75 %
# FACILITY	    Washington Monument, Stonehenge
# GPE	        South East Asia, Midlothian

orgs = []
people = []
locs = []
dates = []
times = []
money = []
percent = []
facilities = []
gpes = []

for i, chunk in enumerate(chunks):
    if hasattr(chunk, 'label'):
        if chunk.label() == 'ORGANIZATION':
            orgs.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'PERSON':
            people.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'LOCATION':
            locs.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'DATE':
            dates.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'TIME':
            times.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'MONEY':
            moeny.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'PERCENT':
            percent.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'FACILITY':
            facilities.append([' '.join(c[0] for c in chunk), i])
        elif chunk.label() == 'GPE':
            gpes.append([' '.join(c[0] for c in chunk), i])

if (orgs):
    print("ORGANIZATIONS")
    print(tabulate(orgs, headers=['Term', 'Word Position']))
if (people):
    print("\nPEOPLE")
    print(tabulate(people, headers=['Term', 'Word Position']))
if (locs):
    print("\nLOCATIONS")
    print(tabulate(locs, headers=['Term', 'Word Position']))
if (dates):
    print("\nDATES")
    print(tabulate(dates, headers=['Term', 'Word Position']))
if (times):
    print("\nTIME")
    print(tabulate(times, headers=['Term', 'Word Position']))
if (money):
    print("\nMONEY")
    print(tabulate(money, headers=['Term', 'Word Position']))
if (percent):
    print("\nPERCENTAGES")
    print(tabulate(percent, headers=['Term', 'Word Position']))
if (facilities):
    print("\nFACILITIES")
    print(tabulate(facilities, headers=['Term', 'Word Position']))
if (gpes):
    print("\nGEO-POLITICAL")
    print(tabulate(gpes, headers=['Term', 'Word Position']))
