from tests.src.enums import Statuses
from tests.src.generators.player_localozation import PlayerLocalization


class BaseGenerator:
    # class BuilderBaseClass:

    def __init__(self):
        self.result = {}

    def update_inner_value(self, key, value):
        if not isinstance(key, list):
            self.result[key] = value
        else:
            temp = self.result
            for item in key[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[key[-1]] = value
        return self


class Player(BaseGenerator):
    def __init__(self):
        # self.result = {
        #     "localize": {
        #         "en": PlayerLocalization("en_US").build(),
        #         "ru": PlayerLocalization("ru_RU").build(),
        #     },
        # }
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="avatar"):
        self.result["avatar"] = avatar
        return self

    # def set_localize(self, generator):
    #     self.result["localize"] = {
    #         "en": generator.build(),
    #     }
    #     return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        return self

    def build(self):
        return self.result
