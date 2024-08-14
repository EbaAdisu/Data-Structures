class BinaryIndexedTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.biarr = [0] * (self.N + 1)
        self.initialize(arr)

    def get_range_sum(self, ind):
        range_sum = 0
        ind += 1
        while ind > 0:
            range_sum += self.biarr[ind]
            ind -= ind & (-ind)
        return range_sum

    def update_range(self, ind, val):
        ind += 1
        while ind < len(self.biarr):
            self.biarr[ind] += val
            ind += ind & (-ind)

    def initialize(self, arr):
        for ind in range(self.N):
            self.update_range(ind, arr[ind])

    def get_sum(self, left, right):
        return self.get_range_sum(right) - self.get_range_sum(left - 1)
