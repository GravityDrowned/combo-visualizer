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
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True, select_menu=True,
                  filter_menu=True)
    net.barnes_hut()
    if not combos:
        return
    for combo in combos:
        cards = combo.get("cards")
        net.add_nodes(cards, title=cards)
        add_all_edges(net, cards, combo.get("results"))
    net.show_buttons(filter_=['physics'])
    net.toggle_physics(True)
    net.show("cards.html")

cards_mock = ['Xyris, the Writhing Storm', 'Intruder Alarm', 'Lore Broker']
results_mock = ['Infinite draw triggers for all players', 'Infinite looting for all players',
                    'Infinite self-discard triggers for all players', 'Near-infinite creature tokens',
                    'Near-infinite ETB', 'Near-infinite untap of all creatures']

t = {
    "cards": cards_mock,
    "results": results_mock
}

create_graph([t] )