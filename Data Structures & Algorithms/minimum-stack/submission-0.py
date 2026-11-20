class MinStack:
    def __init__(self):
        self.res = []
        self.mins = []

        

    def push(self, val: int) -> None:
        self.res.append(val)
        if not self.mins:
            self.mins.append(val)
        elif val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.res.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return self.mins[-1]
