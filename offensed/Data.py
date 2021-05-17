import pygame
pygame.init()
from Word import *

#afficher les phrases des joueurs
x1 = 100
x2 = 650
y1 = 100
y2 = 100
x1bis = 115
x2bis = 665
total1 = 0
total2 = 0


#compteur tour
countPlayer = 1


#création mots
tu = Word("tu",None,"pronom")
je = Word("je", None, "pronom")
ta_maman_est_tellement = Word("ta maman est tellement", "family", None)
ton_frere_est_tellement = Word("ton frère est tellement", "family", None)
t_es_tellement = Word("t'es tellement", None, "sujets")
t_es_yeux_sont = Word("tes yeux sont", None, "style")
ton_chien_est = Word("ton chien est", "pet", None)
ton_chat_est = Word("ton chat est", "pet", None)
ton_chihuahua_est = Word("ton chat est", "pet", None)
t_es_au_chomage = Word("t'es au chômage", "work", None)
ton_maillot_est = Word("ton maillot est", "style", None)
ton_jogging_est = Word("ton jogging est", "style", None)
tes_baskets_sont = Word("tes baskets sont", "style", None)
ton_oncle_me_fait_tellement = Word("ton oncle me fait tellement", "family", None)
ton_boulot_de = Word("Ton boulot de", "work", None)
je_voudrai_lui_faire_des_bisous = Word("je voudrai lui faire des bisous", None, "verbes")
tu_merites_mieux = Word("tu mérites mieux", None, "verbes")
on = Word("on", None, "sujets")
reussiras = Word("réussiras", None, "verbes")
est = Word("est", None, "verbes")
ai = Word("ai", None, "verbes")
voudrai = Word("voudrai", None, "verbes")
tombe = Word("tombé", None, "verbes")
es = Word("es", None, "verbes")
suis = Word("suis", None, "verbes")
rire = Word("rire", None, "verbes")
resplendissent = Word("resplendissent", None, "verbes")
faire = Word("faire", None, "verbes")
signer = Word("signer", None, "verbes")
etre = Word("être", None, "verbes")
vanne = Word("vanne", None, "verbes")
connais = Word("connais", None, "verbes")
saches = Word("saches", None, "verbes")
depuis = Word("depuis", None, "adverbes")
mais = Word("mais", None, "negations")
le = Word("le", None, "articles")
la = Word("la", None, "articles")
les = Word("les", None, "articles")
des = Word("des", None, "articles")
une = Word("une", None, "articles")
un = Word("un", None, "articles")
de = Word("de", None, "articles")
du = Word("du", None, "articles")
aux = Word("aux", None, "articles")
au = Word("au", None, "articles")
basket = Word("basket", "passion", None)
foot = Word("foot", "passion", None)




#tes yeux sont tellement beau qu'ils resplendissent dans la nuit 
#Ta maman est tellement gentille que je voudrai lui faire des bisous 
#T'es si bon en foot que t'aurai dû signer en pro 
#Gros tout le monde te vanne avec ta nouvelle coupe mais je suis sur que ta mère doit être grave fier de toi
#Tout a l'heure je suis tombé sur ton compte insta sache que t'es grâve drôle 
#On te vanne avec ton chihuahua mais sache que je le trouve grave mignon 
#je te connais depuis l'enfance et je voudrai que tu saches que je t'ai touours aimé 
#mon reuf t'es au chômage et sans diplome mais je suis sur que tu reussiras dans la vie
#Ton oncle me fait tellement rire que je voudrai que ce soit un membre de ma famille
#ton boulot de caissier est bien mais tu merites beaucoup mieux

#GENRE DES MOTS

pronomsDetermSujet = [tu, je, ta_maman_est_tellement, t_es_tellement, on]
verbes = [reussiras, est, ai, je_voudrai_lui_faire_des_bisous, tombe, es, suis, resplendissent, faire, signer, etre, vanne, connais, saches, rire, tu_merites_mieux]
adverbesNegations = [depuis, mais]
articles = [le, la, les, des, une, un, du, de, aux, au]


genre = [pronomsDetermSujet, verbes, adverbesNegations, articles]

#catégories DE MOTS
pet = [ton_chien_est, ton_chat_est, ton_chihuahua_est]
work = [t_es_au_chomage, ton_boulot_de]
style = [ton_jogging_est, tes_baskets_sont, ton_maillot_est, t_es_yeux_sont]
passion = [foot, basket]
family = [ta_maman_est_tellement, ton_frere_est_tellement, ton_oncle_me_fait_tellement]


#phrase joueur
phrasej1 = []
phrasej2 = []
