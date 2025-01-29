from crawler import crawl_until_the_end
from visualization import create_graph

if __name__ == '__main__':
    url = "https://commanderspellbook.com/search/?q=Intruder+Alarm+ci%3ATemur"
    combos = crawl_until_the_end(url)
    print(combos)
    create_graph(combos)

