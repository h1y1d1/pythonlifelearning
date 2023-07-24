import random

songs=["baby","hukum","kushi","naa ready","bro","kavalaiah","aradhya","jailer","pokiri","leo","kalki"]
def shuffle():
    return random.randint(1,len(songs))

def play():
    song=songs[shuffle()-1]
    print(song)
playlist = play()