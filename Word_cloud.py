#utf-8
#Ce programme permet de créer un nuage avec les mots les plus utilisés dans nos
#tweets scrappés.

from wordcloud import WordCloud
import numpy as np
import os
import pickle
import csv
import nltk
from PIL import Image

#Cette fonction permet de définir la forme et les différentes modalités du nuage
#de mot que nous souhaitons former (max de mot, image de forme...)

def create_wordcloud(query):
    mymask = np.array(Image.open("twitter-logo-blue-md.png"))
    wc   = WordCloud(background_color='white',
                     mask=mymask
                     ,max_words=2000)
    
    wc.generate (query)
    wc.to_file(os.path.join("wc_mentions_exclu.png"))

#Les stop words permettent d'enlever les mots inutiles de notre nuage de mots

nltk.download('stopwords')
stop_words = list(nltk.corpus.stopwords.words('english'))
stop_words.extend(["UN_Photo"])
print(stop_words)

# Ce petit programme permet de créer le nuage de mots et de l'enregistrer

montexte=[]
with open("Scrapping/donnees_marche_photov.csv",'r') as f:
        reader = csv.reader(f, delimiter=';',lineterminator='\n')
        for row in reader:
            #txt = row[1]
            #txt = txt.split(" ")
            tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
            txt = tokenizer.tokenize(row[6])
            output = [w for w in txt if not w in stop_words]
            output = " ".join(output)
            #print(output)
            montexte.append(output)
            
montexte = " ".join(montexte)
create_wordcloud(montexte)
    
