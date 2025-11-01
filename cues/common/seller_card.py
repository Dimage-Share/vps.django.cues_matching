from dataclasses import dataclass


@dataclass
class SellerCard:
    id: int
    name: str
    rating: int
    is_active: bool

    def __init__(self):
        pass

    def getCard(self):
        pass
