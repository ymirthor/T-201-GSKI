for i in range(self.size - 1):
            self.array[self.size - 1 - i] = self.array[self.size - 2 - i]
        self.array[0] = value