from faker import Faker

fake = Faker().factories


class PlayerLocalization:
    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name(),
        }

    def build(self):
        return self.result
