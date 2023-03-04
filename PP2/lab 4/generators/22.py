class evennumbers():
    def __init__(self, n):
        self.n = n
        self.even = 0
        self.end_point = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.even > self.end_point:
            raise StopIteration()
        x = self.even
        self.even += 2
        return x

n = int(input())
for i in evennumbers(n):
    print(i)
