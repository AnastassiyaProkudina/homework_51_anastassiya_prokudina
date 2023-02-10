import random


class Cat:
    @staticmethod
    def cat_actions(cat, action):

        if cat['state'] == "спит":
            if action == "поиграть с котом":
                cat['mood'] -= 5
                cat['state'] = 'бодр'
            elif action == "покормить кота":
                cat['mood'] -= 5
                cat['fullness'] += 7

        else:
            if action == "поиграть с котом":
                if random.randint(1, 4) > 1:
                    cat['fullness'] -= 10
                    cat['mood'] += 15
                else:
                    cat['mood'] = 0
            elif action == "покормить кота":
                if cat['fullness'] <= 90:
                    cat['fullness'] += 15
                    cat['mood'] += 5
                else:
                    cat['mood'] -= 30
            elif action == "уложить спать кота":
                cat['state'] = 'спит'
        return cat
