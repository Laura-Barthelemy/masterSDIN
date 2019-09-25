#coding : utf-8
#Ce programme va scrapper les tweets populaires avec : Kylie Cosmetics ou @kyliecosmetics
#ou #kyliecosmetics sans aucune géolocalisation.
#Scrapping du contenu, de l'ID du tweet, de l'ID de la personne, la géolocal
# de la personne qui a posté le tweet, le nombre de followers de la personne,
#nombre de likes et nombre de RT du post, @cités et #.


import pdb
import tweepy
import pickle
import datetime
import pdb
import csv
import os.path

datafile = "Autoconsommation_donnees.csv"
q='autoconsommation OR #autoconsommation'

#Cette fonction sera utile plus bas, car elle permet de collecter l'information
#dont nous avons besoin dans les tweets, a savoir le texte des hashtags cités
# et les screen_name des personnes mentionnées.

def getItem(items,field):
    txt = []
    for x in items:
            txt.append(x[field])
    return ",".join(txt)


#Les informations ci-dessous sont les clés nécessaire à la collecte de données

consumer_key='uxuXCDKJeaQHzWOrYUE9BcDbX'
consumer_secret='SIEFExWOICNFRGlTOMdh7TTVMPRZPu8gNY1zjr5MRGlUu8myGK'
access_token='3190026442-t6Q03rbmjty23Iawj0JmfxsiAwuSYTKjYBavwXO'
access_token_secret='MQr1NoKhuHBhQccKelrnfNJTtjbKjQXvCTa76UN550clx'


auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret) 
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


#Cette liste permet d'éviter de collecter le même tweet en double. A chaque
#lancement, le programme va vérifier que l'id du tweet n'est pas déjà enregistré.
#Ainsi, nous sommes sûrs de ne pas collecter plusieurs fois le même en scrappant
#tous les jours.

ListID=[]
if os.path.isfile(datafile):
    with open(datafile,'r') as f:
        reader = csv.reader(f, delimiter=';',lineterminator='\n')
        for row in reader:
            tweetid=row[0]
            ListID.append(tweetid)



# Le programme ci-dessous permet de collecter les différentes informations dont
#nous avons besoin sur twitter, à savoir: l'id du tweet, le texte, le nombre de
#Retweets... Ces informations sont ensuite enregistrées dans un fichier csv.

with open(datafile,'a') as output:
    data=csv.writer(output,delimiter=';',lineterminator='\n')
    for tweet in tweepy.Cursor(api.search,q).items():
            idtweet        = tweet.id_str
            TweetTxt       = tweet.text.encode('ascii','ignore').decode('utf8')
            NombreRT       = str(tweet.retweet_count)
            NombreLIKE     = str(tweet.favorite_count)
            Date           = tweet.created_at
            Hashtags       = getItem( tweet.entities['hashtags'],      "text")
            Mentions       = getItem( tweet.entities['user_mentions'], "screen_name" )
            Coordonnees    = str(tweet.coordinates)
            ScreenName     = tweet.user.screen_name.encode('ascii','ignore').decode('utf8')
            Name           = tweet.user.name.encode('ascii','ignore').decode('utf8')
            UserID         = str(tweet.user.id)
            Langue         = tweet.user.lang
            Localisation   = tweet.user.location
            NombreFollo    = str(tweet.user.followers_count)
            NbrAbonnements = str(tweet.user.friends_count)

               
            if idtweet not in ListID:
                try :
                    data.writerow([idtweet,TweetTxt,NombreRT,NombreLIKE,Date,Hashtags,Mentions,Coordonnees,ScreenName,Name,UserID,Langue,Localisation,NombreFollo,NbrAbonnements])
                except :
                    1

