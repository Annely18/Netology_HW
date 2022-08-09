import requests

# Задача №1
# Кто самый умный супергерой?
def get_smartest(heroes_list):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    data = requests.get(url)
    compared_hero_dict = {}
    for hero in data.json():
        for compared_hero in heroes_list:
            if hero['name'] == compared_hero:
                intelligence = hero['powerstats']['intelligence']
                compared_hero_dict[compared_hero] = intelligence
    return max(compared_hero_dict, key=compared_hero_dict.get)


heroes = ['Hulk', 'Captain America', 'Thanos']
print(get_smartest(heroes))

