class ProductOfNumbers:

    def __init__(self):
        self.product_list=[1]
        self.size=0

    def add(self, num: int) -> None:
        if num==0:
            self.product_list=[1]
            self.size=0
        else:
            self.product_list.append(num*self.product_list[-1])
            self.size+=1

    def getProduct(self, k: int) -> int:
        if k>self.size:
            return 0
        else:
            return int(self.product_list[-1]//self.product_list[self.size-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)