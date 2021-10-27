import random
class lfsr:
    def __init__(self, degree, keyLength, coef, seed):
        self.degree = degree

        self.setKey(keyLength)
        self.setCoefficients(coef)
        self.setSeed(seed)

    def setDegree(self, m):
        self.degree = m

    def getDegree(self):
        return self.degree

    def setKey(self, bits):
        k = ''
        for i in range(bits):
            k = k + str(random.randint(0,1))
        self.key = k

    def getKey(self):
        return self.key

    def setCoefficients(self, num):
        # the coefficients will be inputted as an int and converted to binary
        # for example, for a lfsr with m=4, then 15 is the max number since it
        # would be 1111
        # also, if you enter in something super long itll just use the first m^2
        # you enter in
        self.coef = "{0:b}".format(num).zfill(self.degree)

    def getCoefficients(self):
        return self.coef

    def setSeed(self, seed):
        self.seed = seed[-self.degree:].zfill(self.degree)

    def getSeed(self):
        return self.seed

    def runLfsr(self, runs):
        tmp = self.seed
        print("SEED: " + str(tmp))
        print("COEF: " + str(self.coef))
        print("KEY: " + str(self.key))
        print("RUNS: " + str(runs))
        self.key = self.key * runs
        ciphertext = ''
        print("\nLFSR Values,", "Output,", "Encoded Output")
        for i in range(runs, -1, -1):
            arr = []
            for j in range(self.degree-1, -1, -1):
                if self.coef[j] == '1':
                   arr.append(int(tmp[j]))
            inp = str(sum(arr) % 2)
            out = int(tmp[-1])
            tmp = inp + tmp[:-1]

            ciph = (out + int(self.key[i])) % 2
            ciphertext = ciphertext + str(ciph)
            print(tmp, out, ciph)
        return "\nCIPHERTEXT: " + ciphertext


# if __name__ == '__main__':
#     t = lfsr(degree=5, keyLength=7, coef=5, seed='10110')
#     print(t.runLfsr(runs=10))
