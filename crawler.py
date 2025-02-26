import requests
from bs4 import BeautifulSoup
import urllib.parse


def flatten(xss):
    return [x for xs in xss for x in xs]

def crawl_everything_for_a_card_name(card_name, color_name):
    card_name_url = urllib.parse.quote_plus(card_name)
    url ='https://commanderspellbook.com/search/?q='+card_name_url+'+ci%3A'+color_name+'+legal%3Acommander'
    print(url)
    combos = crawl_until_the_end(url)
    return combos

def crawl_until_the_end(url):
    current_page = 1
    combos = []
    combos_found = True

    while combos_found:
        url_next = url + '&page=' + str(current_page )
        response = requests.get(url_next)

        soup = BeautifulSoup(response.content, 'html.parser')
        s = soup.find_all('h3', class_="heading-title", string='No Combos Found')
        if s:
            combos_found=False
        combos.append(crawl(response))
        current_page += 1
    return flatten(combos)

def crawl(response):
    if response.status_code == 200:
        combos = []
        soup = BeautifulSoup(response.content, 'html.parser')
        combo_results = soup.find_all('a', class_='comboResults_comboResult__VcfMx')
        for combo in combo_results:
            cards_html = combo.find_all('div', class_="card-name")
            images_html = combo.find_all('div', class_='cardTooltip_cardTooltip__3eItj')
            results_html = combo.find_all('div', class_="result")

            cards = []
            images = []
            results = []

            for i, card in enumerate(cards_html):
                cards.append(card.text.strip())
            for i, image in enumerate(images_html):
                src = image.find('img')['src']
                images.append(src)
            for i, result in enumerate(results_html):
                results.append(result.text.strip())

            combo = {
                "cards": cards,
                "images": images,
                "results": results
            }
            print(combo)

            combos.append(combo)
        return combos
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def digging_deeper(card_name, color_name):

    combos = crawl_everything_for_a_card_name(card_name, color_name)

    combo_pieces = []
    for combo in combos:
        cards = combo.get("cards")
        combo_pieces.append(cards)
    combo_pieces = set(flatten(combo_pieces))
    if card_name in combo_pieces:
        combo_pieces.remove(card_name)
    print(combo_pieces)

    combos_plus_one = []
    combos_plus_one.append(combos)

    for combo_piece in combo_pieces:
        c = crawl_everything_for_a_card_name(combo_piece, color_name)
        combos_plus_one.append(c)

    combos_plus_one = flatten(combos_plus_one)
    print(combos_plus_one)
    return combos_plus_one

