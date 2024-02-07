import random


class Password:

    def __init__(self):
        self.letter = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
                       "z", "x", "c", "v", "b", "n", "m"]
        self.number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.character = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
        self.password_list = []
        self.random_password()
        self.password = "".join(self.password_list)

    def random_password(self):
        self.password_list.clear()
        nr_letter = random.randint(4, 6)
        nr_number = random.randint(2, 4)
        nr_character = random.randint(3, 5)

        for item in range(nr_letter):
            self.password_list.append(random.choice(self.letter))
        for item in range(nr_number):
            self.password_list.append(random.choice(self.number))
        for item in range(nr_character):
            self.password_list.append(random.choice(self.character))

        random.shuffle(self.password_list)

        if len(self.password_list) != 12:
            self.random_password()

