class divisible():
    def __init__(self, end):
        self.current = 0
        self.end_point = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end_point + 12:
            raise StopIteration()
        self.current += 12
        return self.current - 12
        

n = int(input())
for i in divisible(n):
    print(i)