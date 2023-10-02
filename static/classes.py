CLASSES = [
    "mine",
    "trade",
    "hunt",
    "craft",
    "farm",
    "breed",
    "cook",
    "know"
]

SUITS_CLASSES = {
    "diamonds" : ["mine", "trade"],
    "clubs" : ["hunt", "craft"],
    "cups" : ["farm", "breed"],
    "spades" : ["cook", "know"]
}

CLASSES_EDGES = [
    ('mine', 'trade'),
    ('trade', 'craft'),
    ('craft', 'hunt'),
    ('hunt', 'know'),
    ('know', 'cook'),
    ('cook', 'breed'),
    ('breed', 'farm'),
    ('farm', 'mine')
]