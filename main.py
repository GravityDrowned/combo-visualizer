from crawler import crawl_until_the_end, digging_deeper
from visualization import create_graph

if __name__ == '__main__':
    #url = "https://commanderspellbook.com/search/?q=Intruder+Alarm+ci%3ATemur"
    #combos = crawl_until_the_end(url)

    #card_name = "Xyris, the Writhing Storm"
    card_name = "Marwyn, the Nurturer"
    card_name = "Grand Warlord Radha"
    color_name = "Gruul"
    combos = digging_deeper(card_name, color_name)
    print(combos)
    create_graph(combos)

