import random

keywords = ('red', 'black', 'blue', 'magenta', 'lime', 'gold', 'ruby', 'warm', 'emerald', 'clean', 'noxious', 'mute',
            'absent', 'agonizing', 'frail', 'disgusted', 'innocent', 'puzzled', 'flowery', 'shiny', 'concerned', 'billowy',
            'wonderful', 'empty', 'tacky', 'ancient', 'physical', 'resolute', 'depressed', 'elfin', 'rural', 'urban',
            'filthy', 'dead', 'snobbish', 'scared', 'unusual', 'good', 'bad', 'pocket', 'achiever', 'window', 'banana',
            'fight', 'collar', 'card', 'sofa', 'mountain', 'bedroom', 'girl', 'juice', 'pain', 'town', 'jail', 'activity',
            'profit', 'belief', 'vein', 'meat', 'river', 'stem', 'toes', 'trouble', 'waste', 'bend', 'promise',
            'recognize', 'dance', 'brick', 'stone', 'sand', 'orange', 'gray', 'green', 'cyan', 'turquoise', 'silver',
            'sapphire', 'opal', 'cool', 'wise', 'victorious', 'lethal', 'oval', 'lush', 'kindhearted', 'milky', 'rotten',
            'premium', 'ratty', 'dull', 'jolly', 'screeching', 'wandering', 'natural', 'even', 'odd', 'joyous', 'true',
            'false', 'sharp', 'aware', 'striped', 'closed', 'breezy', 'warlike', 'astonishing', 'fine', 'married',
            'berserk', 'train', 'comparison', 'robin', 'breakfast', 'sand', 'request', 'noise', 'house', 'donkey',
            'wax', 'throne', 'comfort', 'kick', 'cushion', 'summer', 'winter', 'spring', 'fall', 'territory', 'mice',
            'passenger', 'cracker', 'shoes', 'education', 'crown', 'travel', 'hypnotize', 'contest', 'charge', 'tired',
            'lonely', 'curious', 'yellow', 'white', 'purple', 'chartreuse', 'scarlet', 'diamond', 'amethyst', 'platinum',
            'neutral', 'political', 'spiky', 'educated', 'soft', 'entertaining', 'hysterical', 'important', 'broad',
            'terrible', 'mushy', 'glittery', 'sore', 'imaginary', 'annoying', 'ethereal', 'icky', 'observant', 'quaint',
            'deserted', 'strange', 'smooth', 'rainy', 'sunny', 'dramatic', 'chemical', 'ugly', 'chilly', 'glorious',
            'pushy', 'wooden', 'drum', 'leg', 'key', 'amusement', 'scissors', 'heart', 'chair', 'fish', 'wave', 'expert',
            'rock', 'ring', 'note', 'sheet', 'story', 'earthquake', 'behavior', 'cloud', 'turkey', 'bear', 'circle',
            'fear', 'voyage', 'fang', 'smell', 'deal', 'download', 'humiliate', 'reflect', 'island', 'forest', 'desert')

response = (f'Draw something based off this random keyword: **{random.choice(keywords)}**', )
