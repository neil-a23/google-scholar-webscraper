from habanero import Crossref
from csv import writer
from crossrefsearch import results
import sys
import pandas as pd 

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


information = results['message']['items']
apapsychdois = []

titles = []
dois = []
apadois = []
for i in information:
    if 'title' in i:
        titles.append(i['title'])
    if "10.1037" in i["DOI"]:
        apadois.append(i["DOI"])
    else: 
        dois.append(i["DOI"])

apadf = pd.DataFrame(apadois, columns=["DOI"])
apadf.to_csv("apadois.csv", mode="a+", index=None)
df = pd.DataFrame(list(zip(dois,titles)), columns=["DOI", "title"])
df.to_csv("crossref/crossrefdata.csv", index=None)