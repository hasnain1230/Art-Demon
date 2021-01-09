import random

words = ('tired', 'lazy', 'fast', 'slow', 'happy', 'sad', 'angry', 'big', 'small', 'friend', 'wet', 'dry', 'scared',
         'flight', 'quiet', 'loud', 'weak', 'alone', 'dessert', 'breakfast', 'sweet', 'loved', 'celebration', 'space',
         'mystery', 'confusion', 'prism', 'dream', 'fake', 'escape', 'tangle', 'gloomy', 'hope', 'curious', 'glare', 'impossible',
         'wool', 'erase', 'mix', 'sing', 'trinket', 'distance', 'machine', 'shiny', 'shadow', 'business', 'present',
         'travel', 'important', 'old', 'invisible', 'average', 'comfortable', 'bird', 'lost', 'found', 'wind', 'hand',
         'camouflage', 'animal', 'explore', 'city', 'stain', 'door', 'memory', 'tree', 'routine', 'bridge', 'box', 'portrait',
         'metal', 'pair', 'together', 'imagine', 'decision', 'suspicious', 'advice', 'feeling', 'harmony', 'warning', 'abnormal',
         'activate', 'sight', 'haunt', 'ambiguous', 'different', 'spin', 'plain', 'plant', 'patience', 'rebellion', 'imperial',
         'contradiction', 'foreign', 'hostile', 'digital', 'ribbon', 'replacement', 'origin', 'sharp', 'ring',
         'hostage', 'expression', 'hypnosis', 'corrupt', 'pride', 'siege', 'work', 'exact', 'jump', 'restore', 'shelter', 'basket',
         'aftermath', 'humanity', 'product', 'biscuit', 'thread', 'connection', 'constellation', 'closed', 'broken',
         'hardship', 'workshop', 'mind', 'deeper', 'critic', 'hike', 'float', 'away', 'resolution', 'shell', 'complain', 'lover',
         'expand', 'threshold', 'monarch', 'virtue', 'glimpse', 'form', 'apology', 'reptile', 'layers', 'blessed', 'map',
         'answer', 'sheet', 'arm', 'relief', 'hiss', 'insult', 'complete', 'increase', 'moldy', 'crackle', 'glossy', 'shoe',
         'test', 'defect', 'steel', 'order', 'chaos', 'smooth', 'empty', 'forgive', 'bright', 'determined', 'peace', 'frantic',
         'nebulous', 'elastic', 'grab', 'lettuce', 'decay', 'stale', 'car', 'condition', 'sudden', 'clear', 'prepare',
         'solve', 'miss', 'journal', 'strive', 'doll', 'mailbox', 'quaint', 'grim', 'shape', 'slippery', 'phone', 'fork', 'bite',
         'because', 'soap', 'vengeful', 'respect', 'please', 'legend', 'ancient')

response = f'Draw something based off this word: **{random.choice(words)}.**'

all_possible_prompts = []

for word in words:
    all_possible_prompts.append(f'Draw something based off this word: **{word}.**')

all_possible_prompts = tuple(all_possible_prompts)




