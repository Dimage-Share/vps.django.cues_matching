from seller_card import SellerCard

db = None


def getSellers():
    dt = db.getTable(
        "select id, name, rating, is_active from sellers order by rating")
    ret = [SellerCard]
    for row in dt.rows:
        card = SellerCard()
        card.id = row[0]
        card.name = row[1]
        card.rating = row[2]
        card.is_active = row[3]
        ret.append(card)
    return ret


sellers = getSellers()
ui = []

for seller in sellers:
    ui.append(seller.getCard())

ui.show()
