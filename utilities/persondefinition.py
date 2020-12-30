import random


class PersonDefinition:
    def __init__(self, hair_texture, hair_color, eye_color, skin_tone, body_type, gender_age, features):
        self.hair_texture = hair_texture
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.skin_tone = skin_tone
        self.body_type = body_type
        self.gender_age = gender_age
        self.features = features

    @staticmethod
    def get_random_from_list(characteristic):
        return characteristic[random.randint(0, len(characteristic) - 1)]

    def __str__(self):
        return 'Hair Texture.txt: {0}\n' \
               'Hair Color: {1}\n' \
               'Eye Color: {2}\n' \
               'Skin Tone: {3}\n' \
               'Body Type: {4}\n' \
               'Gender/Age: {5}\n' \
               'Features: {6}\n'.format(self.get_random_from_list(self.hair_texture),
                                        self.get_random_from_list(self.hair_color),
                                        self.get_random_from_list(self.eye_color),
                                        self.get_random_from_list(self.skin_tone),
                                        self.get_random_from_list(self.body_type),
                                        self.get_random_from_list(self.gender_age),
                                        self.get_random_from_list(self.features))
