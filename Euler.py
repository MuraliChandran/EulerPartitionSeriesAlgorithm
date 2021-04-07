class Counter:
    k = 0
    l = 1

    def counter(self, count):
        if count is 0:
            # natural number
           count = 1
        else:
            # odd number
            count = 0
        return count

    def natural(self):
        Counter.k = Counter.k + 1
        return Counter.k

    def odd(self):
        Counter.l = Counter.l + 2
        return Counter.l


class Euler:
    position= {}
    symbolpos = {}

    result = []
    symbols = []
    keys = []
    values = []
    finalresult = []

    c = Counter()

    def EulerPartition(self, z):
        count = 0
        sum = 1
        acount = 0
        mcount = 0
        Euler.position[1] = "+"
        acount = acount + 1

        for i in range(1, z):
            sum = self.PositionResult(sum, count)
            if(acount < 2 ):
                Euler.position[sum]= "+"
                acount = acount + 1
            else:
                Euler.position[sum] = "-"
                mcount = mcount + 1

            if(mcount == 2):
                acount = 0
                mcount = 0
            count = Euler.c.counter(count)

        return 0

    def PositionResult(self, i, count):
        if count is 0:
            # natural number
            i = i + Euler.c.natural()
            return i
        else:
            # odd number
            i = i + Euler.c.odd()
            return i

    def PartitionResult(self):
        l = 0
        for k in (Euler.position.keys()):

            if(k is l):
                Euler.symbols.append(Euler.position.get(k))
                l = l + 1
            else:
               while l <= k:
                    Euler.symbols.append(0)
                    l = l + 1
               l = l - 1
               if (k == l):
                   Euler.symbols[k] =(Euler.position.get(k))

    def finalResult(self):
        sum = 0
        runonce = True
        Euler.keys.append(0)
        Euler.keys.append(1)
        Euler.keys.append(1)
        Euler.values.append(0)
        i = 1
        k = 1

        while i <  666:
            a = Euler.keys[i]
            b = Euler.keys[i + 1]
            # # need a for loop to move the symbol
            # # now check for symbols

            Euler.values.insert(1,Euler.symbols[k])
            if runonce is True:
                Euler.values.insert(1,Euler.symbols[k + 1])

            for j in range(len(Euler.values)):
                if Euler.values[j] is "+" or "-":
                    # we get the position of the symbols
                    Euler.symbolpos[j] = Euler.values[j]

            for k in Euler.symbolpos.keys():
                if Euler.symbolpos.get(k) == "+":
                    sum = sum + Euler.keys[k]
                if Euler.symbolpos.get(k) == "-":
                    sum = sum - Euler.keys[k]

            i = i + 1
            k = k + 1
            Euler.keys.append(sum)
            sum = 0
            runonce = False

        for i in range(1, len(Euler.keys)):
            Euler.finalresult.append(Euler.keys[i])

        #printing the partition series
        for i in range(1, len(Euler.finalresult)):
            print(i,Euler.finalresult[i])

        return 0


if __name__ == '__main__':
    e = Euler()
    e.EulerPartition(50)
    e.PartitionResult()
    e.finalResult()
