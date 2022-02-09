import requests

def max_superhero_intelligence(superheros):
    URL = 'https://superheroapi.com/api/2619421814940190/search/'
    for superhero in superheros:    
        r = requests.get(URL + superhero)
        superheros[superhero] = int(r.json()['results'][0]['powerstats']['intelligence'])
    max_intelligence = max(superheros, key = superheros.get)
    print(f'Самый умный {max_intelligence} с интеллектом: {superheros[max_intelligence]}')

if __name__ == '__main__':
    superheros = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    max_superhero_intelligence(superheros)