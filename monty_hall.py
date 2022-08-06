import random


class Game:

    def __init__(self, insist: bool,  choice: int = 1):
        self.insist = insist

        self.win_value = random.randint(1, 3)

        self.choice = choice

        self.win = self.__play()

    @classmethod
    def host_options_door(cls, win_value, choice_value):
        doors = {1, 2, 3}
        options = doors - {win_value, choice_value}

        return options.pop()

    def __play(self):

        if self.choice not in range(1, 4):
            raise ValueError("Choice must be in 1, 2 or 3")

        opened = self.host_options_door(self.win_value, self.choice)

        if not self.insist:
            new_choice = {1, 2, 3} - {self.choice, opened}
            self.choice = new_choice.pop()

        return self.choice == self.win_value


def print_win_rate(total: int, insist: bool):
    win = 0
    for _ in range(total):
        if Game(insist).win:
            win += 1
    print(f"Win rate if{' not' if not insist else ''} insist = {win * 100 / total}%")


if __name__ == "__main__":
    print_win_rate(1000, True)

    print_win_rate(1000, False)