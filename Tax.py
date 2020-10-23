class Tax:
    def __init__(self,tax,order):
        self.tax = tax
        self.order = order

    def sumAllInOrder(self):
        
        subTotal = 0
        for item in self.order:
            subTotal+=item

        return subTotal

    def calTax(self):
        subTotal = self.sumAllInOrder()

        newTax  = subTotal * self.tax

        finalTotal = newTax + subTotal

        return finalTotal

    def printResults(self):
        print("\nSu total antes del tax: " + str(self.sumAllInOrder()) )
        print("\nSu total final es: " + str(self.calTax()) )






