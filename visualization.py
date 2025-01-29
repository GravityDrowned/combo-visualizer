from cProfile import label
from pyvis.network import Network
import random

def add_all_edges(net, cards, results):
    r = lambda :random.randint(0, 255)
    color  ='#%02X%02X%02X' % (r(), r(), r())
    for card in cards:
        for other_card in cards:
            if card == other_card:
                continue
            net.add_edge(card, other_card, color=color, title='\n'.join(results))

def create_graph(combos):
    net = Network(height="1000px", width="100%", bgcolor="#222222", font_color="white", notebook=True, select_menu=True,
                  filter_menu=True)
    net.barnes_hut()
    if not combos:
        return
    for combo in combos:
        cards = combo.get("cards")
        images = combo.get("images")
        for i, card in enumerate(cards):
            net.add_node(card, title=card, shape="image", image=images[i], size=20)
        add_all_edges(net, cards, combo.get("results"))

    # set the size in relation to the number of connections
    for node in net.get_nodes():
        neighbors = net.neighbors(node)
        node_id = net.get_node(node)
        node_id['size'] = min(210, 20 + 10 * len(neighbors))

    net.show_buttons(filter_="physics")
    net.toggle_physics(True)
    net.show("cards.html")

cards_mock = ['Xyris, the Writhing Storm', 'Intruder Alarm', 'Lore Broker']
images_mock = ['https://api.scryfall.com/cards/named?format=image&version=normal&exact=Xyris%2C%20the%20Writhing%20Storm&face=front', 'https://api.scryfall.com/cards/named?format=image&version=normal&exact=Intruder%20Alarm&face=front', 'https://api.scryfall.com/cards/named?format=image&version=normal&exact=Lore%20Broker&face=front']
results_mock = ['Infinite draw triggers for all players', 'Infinite looting for all players',
                    'Infinite self-discard triggers for all players', 'Near-infinite creature tokens',
                    'Near-infinite ETB', 'Near-infinite untap of all creatures']

t = {
    "cards": cards_mock,
    "images": images_mock,
    "results": results_mock
}

create_graph([t] )