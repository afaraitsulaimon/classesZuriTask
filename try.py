class Budget:
    budget_type = "Home Budgets"

    def __init__(self, name, deposit):
         self.budget_name = name
         self.deposit = deposit


    def amountInBudget(self):
        print("=" * 20)
        print(f"Budget for {self.budget_name} is {self.deposit}")
        theWithAmount = int(input((f"How much do you want to withdraw From {self.budget_name} \n")))


        self.deposit = self.deposit - theWithAmount
        print(f" Your Current Balance for {self.budget_name} after withdraw is {self.deposit}")
        


    
    def transferBalance(self,transfer):
        self.transfer = transfer
        balance = self.deposit + self.transfer
        print(f"Your current balance for {self.budget_name} is : $ %d" % balance)
        

        
                 

budget_food = Budget('Food', int(input("How much do you want to deposit for your Food \n")))
budget_clothing = Budget('Clothing', int(input("How much do you want to deposit for your Clothing \n")))
budget_entertainment = Budget('Entertainment', int(input("How much do you want to deposit for your Entertainment \n")))

budget_food.amountInBudget()

print("=" * 20)

budget_clothing.amountInBudget()

print("=" * 20)

budget_entertainment.amountInBudget()

print("=" * 20)

budget_food.transferBalance(int(input("how much would you like to transfer to Food \n")))

print("=" * 20)

budget_clothing.transferBalance(int(input("how much would you like to transfer to Clothing \n")))

print("=" * 20)

budget_entertainment.transferBalance(int(input("how much would you like to transfer to Entertainment \n")))
