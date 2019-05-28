class RC4:
    state = []
    x, y = 0, 0

    def __init__(self, key):
        self.key = bytearray(key, 'ascii')
        self.keysize = len(self.key)

    def encode(self, source):
        self.prepare()
        source = bytearray(source, 'ascii')

        return [i ^ self.prga() for i in source]

    def prepare(self):
        self.x, self.y = 0, 0
        self.state[:] = range(256)

        j = 0
        for i in range(256):
            j = (j + self.state[i] + self.key[i % self.keysize]) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]

    def prga(self):
        self.x = (self.x + 1) % 256
        self.y = (self.y + self.state[self.x]) % 256

        self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]

        return self.state[(self.state[self.x] + self.state[self.y]) % 256]
