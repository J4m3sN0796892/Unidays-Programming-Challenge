class PricingRules():                                             # Main Parent Class
    def Total(A_Counter,B_Counter,C_Counter,D_Counter,E_Counter): #Function to Calculate the total
        Total = 0
        B_Even =0
        B_Mod = 0
        Price = {"A":8, "B":12, "C":4, "D":7, "E":5}
        A_Price =0
        A_Price = A_Counter * Price["A"]

        B_Price = 0
        B_Even = B_Counter %2
        B_Mod = B_Counter //2                                      #Applies the logic to the items in the basket (3 for 2 etc)

        B_Price = 20 * B_Mod
        if B_Even == 1:
            B_Price += Price["B"]


        C_Price =0
        MulOf3 = 0
        MulOf3 = C_Counter  %3
        C_Mod = 0
        C_Mod = C_Counter //3
        C_Price += C_Mod * 10
        
        if MulOf3 != 0:
            C_Price += MulOf3 * Price["C"]

        D_Price = 0
        ModD = 0

        ModD = D_Counter //2
        ModD= ModD * Price["D"]
        
        D_Price += ModD
        
        E_Price =0
        MulOf3E = 0
        MulOf3E = E_Counter  %3
        E_Mod = 0
        E_Mod = E_Counter //3
        E_Price += E_Mod * 10
        
        if MulOf3E != 0:
            E_Price += MulOf3E * Price["E"]
        Total += B_Price + A_Price + C_Price + D_Price + E_Price
        return Total
 class UnidaysDiscountChallenge(PricingRules):                    #Child Class , inherits Parent as a set of rules
    
    def __init__(self,Item):
        self.Item = Item
        self.Basket=[]
        
    def AddToBasket(self,Item):                                   #Function which adds items to the basket
        self.Basket.append(Item)
        if Item =="D":
            self.Basket.append(Item)
            
        print(self.Basket)
        A_Counter = 0
        B_Counter = 0
        C_Counter =0
        D_Counter = 0
        E_Counter =0
        
        for product in self.Basket:
            if product == "A":
                A_Counter += 1
            if product == "B":
                B_Counter +=1
            if product =="C":
                                                                    #Loop counts how many of each item in the basket
                C_Counter +=1
            if product =="D":
                D_Counter +=1
            if product =="E":
                E_Counter +=1
        Apply_Discount= PricingRules.Total(A_Counter,B_Counter,C_Counter,D_Counter,E_Counter)

        return Apply_Discount    
            
Shopping = UnidaysDiscountChallenge(PricingRules)
Loop =0
total = 0
Response = input("Welcome to The Letter Shop, Would you like to Start Shopping?\n Y/N\n")
Response = Response.capitalize()
while Response == "Y":
                                                                  # this part is basically the Main() as it is where the classes / functions are called
    if Response == "Y":
        
        Item = input("Please select an item from the following\n A,B,C,D,E\n")
        Item = Item.capitalize()
        if Item in ["A","B","C","D","E"]:
            Return = Shopping.AddToBasket(Item)
            print("Total =",Return)
            Response = input("Would you like to keep shopping?\nY/N\n")
            Response = Response.capitalize()
        else:
            print("Please Enter a Valid item")
                 
    
            Response = input("Would you like to keep shopping?\nY/N\n")
            Response = Response.capitalize()

    if Response == "N":
        if Return < 50:
            Delivery = 7                                          # Add the Delivery fee if there is any.
            
        if Return >= 50 :
            Delivery = 0
        print("Thank You For Shopping at the Letter Shop\n your total bill is :£",Return)
        print("Your Delivery Fee is:£",Delivery)
        input("Press enter to close")
        break     
