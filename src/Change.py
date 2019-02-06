class Change:
    def __init__(self):
        self.indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P',
                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.value = []

    def calculate(self, n, n_value):
        if int(n_value / n) is 0:
            return self.indexs[n_value % n]

