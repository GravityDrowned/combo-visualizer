# https://commanderspellbook.com/search/?q=Xyris+ci%3ATemur
import requests
from bs4 import BeautifulSoup

def flatten(xss):
    return [x for xs in xss for x in xs]

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
            images_html2 =  combo.find_all('img')
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

url = "https://commanderspellbook.com/search/?q=Xyris+ci%3ATemur"

crawl_until_the_end(url)