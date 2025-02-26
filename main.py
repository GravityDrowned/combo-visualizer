from crawler import crawl_until_the_end, digging_deeper
from visualization import create_graph

if __name__ == '__main__':
    #url = "https://commanderspellbook.com/search/?q=Intruder+Alarm+ci%3ATemur"
    #combos = crawl_until_the_end(url)

# 1 Academy Rector
# 1 Aggravated Assault
# 1 Archdruid's Charm
# 1 Ashaya, Soul of the Wild
# 1 Atalan Jackal
# 1 Birthing Pod
# 1 Brash Taunter
# 1 Chord of Calling
# 1 Congregation at Dawn
# 1 Crop Rotation
# 1 Eladamri's Call
# 1 Eldritch Evolution
# 1 Enlightened Tutor
# 1 Entish Restoration
# 1 Erinis, Gloom Stalker
# 1 Fanatical Devotion
# 1 Gaea's Blessing
# 1 Gaea's Bounty
# 1 Goblin Clearcutter
# 1 Idyllic Tutor
# 1 Orcish Lumberjack
# 1 Scute Swarm
# 1 Sylvan Tutor
# 1 Tanuki Transplanter
# 1 Valleymaker
# 1 Worldly Tutor
# 1 Rocco, Cabaretti Caterer


    #card_name = "Xyris, the Writhing Storm"
    card_name = "Marwyn, the Nurturer"
    card_name = "Abdel Adrian, Gorion's Ward"
    card_name = "Scute Swarm"
    color_name = "Naya"
    combos = digging_deeper(card_name, color_name)
    print(combos)
    create_graph(combos)
