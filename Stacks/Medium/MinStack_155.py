class MinStack:
    '''
        [3, 2, 1]
        [1, 2, 3]
        [1, 2, -1]
        [2, -1, 3]
    '''

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        if len(self.minVals) == 0:
            self.stack.append(val)
            self.minVals.append(val)
        else:
            if val <= self.minVals[-1]:
                self.minVals.append(val)
            self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop(-1)
        if popped == self.minVals[-1]:
            self.minVals.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]

