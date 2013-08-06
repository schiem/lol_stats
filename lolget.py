import urllib
from bs4 import BeautifulSoup


summoner_url  = 'http://gameinfo.na.leagueoflegends.com/en/game-info/champions/'

class Summoner:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def dump_stats(self, f):
        f = open(f, 'r+')
        f.seek(0, 2)
        f.write('\n' + self.name + '\n')
        for i in self.stats:
            f.write(i + " : " + self.stats[i] + '\n')
        f.close()

def get_stats(summoner):
    stats = {}
    page = summoner_url + summoner + "/"
    soup = BeautifulSoup(urllib.urlopen(page))
    stat_list = soup.find_all('span', 'stat-label')
    stat_num = soup.find_all('span', 'stat-value')
    for i in range(len(stat_list)):
        stats[str(stat_list[i].string).strip()] = str(stat_num[i].string).strip()
    return stats

def get_summoner_list_from_file():
    #bizarre as shit way of doing this
    f = open('lol_champs', 'r')
    champs = []
    for line in f:
        champs.append(line.split("champion-grid-")[1].split('"',1)[0].strip())
    return champs

if __name__=="__main__":
    summoners = get_summoner_list_from_file()
    f = open('stats_file.txt', 'w')
    f.close()
    for summoner in summoners:
        Summoner(summoner.title(), get_stats(summoner)).dump_stats('stats_file.txt') 
