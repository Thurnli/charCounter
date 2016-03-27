import urllib.request
from bs4 import BeautifulSoup
import collections
import re
import numpy as np
import matplotlib.pyplot as plt

#url = 'https://en.wikipedia.org/wiki/Belfast'
#url = 'https://it.wikipedia.org/wiki/Belfast'
url = 'https://af.wikipedia.org/wiki/Belfast'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "lxml")
tags = soup.find_all('p')

textFile = open('belfast.txt', 'a', encoding='utf-8')

for p in tags:
    text = p.text + p.next_sibling
    textFile.write(text)
    
textFile.close()

#generate data visualisation

textFile = open('belfast.txt', 'r', encoding='utf-8')
prose = textFile.read().lower()
words = re.findall(r'([a-z])\w+', prose)

labels, values = zip(*sorted(collections.Counter(words).items()))
indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

#print (collections.Counter(words))

textFile.close()