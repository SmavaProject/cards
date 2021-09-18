from cards import Cards
import random


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
                             'Foo', 'Gym', 'Hut', 'Egg']
        self.columns = ['A', 'B', 'C', 'D']
        self.locations = []
        self.cards = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                # print(f'{column}{num}')
                self.locations.append(f'{column}{num}')

    # we need to convert list of locations and available locations to SET to subtract one from another and keep unique values
    # converting available_locations back to LIST to be able to use raandom() on it
    def set_locations(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Cards(word, random_location)
                self.cards.append(card)
                print(f'{card}{random_location}')

    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')
        return row

    def create_grid(self):
        header = ' |  ' + '  |  '.join(self.columns) + ' |  '
        print(header)
        for row in range (1, self.size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)


if __name__ == '__main__':
    game = Game()
    game.set_locations()
    game.create_grid()
