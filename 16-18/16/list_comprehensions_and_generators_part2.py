from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

response = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")
words = response.text.lower().split()
print(words[:10])
cnt = Counter(words)
print(cnt.most_common(15))
words = [re.sub(r'\W+', r'', word) for word in words]

stopwords = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt")
stop_words = stopwords.text.lower().split()

print('the' in words)
words = [word for word in words if word.strip() and word not in stop_words]
cnt = Counter(words)
print(cnt.most_common(15))
print('the' in words)