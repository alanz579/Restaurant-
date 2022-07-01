'''
1. welcome message
2. Menu option:
  - 4 options for food
  - 4 options for drinks
  - 2 options for desserts
Keep asking the users until they press 0 to exit the menu
3. By the end, we show them what they have ordered in total orders
4. Ask if they have any coupon (5% and 8%) 
5. Calculate the total price (need to take care for the coupons and taxes)
'''
#welcome
print("Welcome to the Restaurant")

#menu
def menu():
  totalprice = 0
  
  
  burger = 0 
  fries = 0
  pizza = 0
  sandwich = 0
  water = 0
  coke = 0
  smoothie = 0
  milk = 0
  cupcake = 0
  icecream = 0
  running = True
  
  while running:
    print("\nHere is the menu: ")
    options = int(input(" For food press 1\n For Drinks press 2\n For Dessert press 3\n To pay press 4 \n To exit press 0: "))
    
    if options == 1:
      food = input("\nHere are the foods, input the item name: \n $6.69 burger \n $2.50 fries \n $4.20 pizza \n $2.22 sandwich: ") 
      if food.lower() == "burger":
        
        totalprice += 6.69
        burger += 1
      if food.lower() == "fries":
        
        totalprice += 2.50
        fries += 1
      if food.lower() == "pizza":
        
        totalprice += 4.20
        pizza += 1
      if food.lower() == "sandwich":
        
        totalprice += 2.22
        sandwich += 1
        
        
    elif options == 2:
      drink = input("Here are the drinks, input the item name: \n $1 water \n $1.50 coke \n $2 smoothie \n $1.25 milk: ")
      if drink.lower() == "water":
        totalprice += 1
        water += 1
      if drink.lower() == "coke":
        totalprice += 1.50
        coke += 1
      if drink.lower() == "smoothie":
        totalprice += 2
        smoothie += 1
      if drink.lower() == "milk":
        totalprice += 1.25
        milk += 1
    
    elif options == 3:
      dessert = input("\nHere are the desserts, input the item name: \n $3 cupcake \n $2 ice cream: ")
      if dessert.lower() == "cupcake":
        totalprice += 3
        cupcake += 1
      if dessert.lower() == "ice cream":
        totalprice += 2
        icecream += 1
    elif options == 0:
      running = False
      
  # summarize their oders
    elif options == 4:
      if burger != 0:
        print(f"{burger} burgers")
      if fries != 0:
        print(f"{fries} fries")
      if pizza != 0:
        print(f"{pizza} pizzas")
      if sandwich != 0:
        print(f"{sandwich} sandwich")
      if water != 0:
        print(f"{water} water")
      if coke != 0:
        print(f"{coke} coke")
      if smoothie != 0:
        print(f"{smoothie} smoothie")
      if milk != 0:
        print(f"{milk} milk")
      if cupcake != 0:
        print(f"{cupcake} cupcake")
      if icecream != 0:
        print(f"{icecream} ice cream")
        
  # ask the user if they have any coupons
      coupons = input("Do you have any coupons input yes or no: ")
      if coupons.lower() == "yes":
        whichcoupon = int(input("Is your coupon 5 percent or 8 percent: "))
        if whichcoupon == 5:
          print("Okay your coupon has been used")
          totalprice = totalprice - (totalprice * 0.05) 
        elif whichcoupon == 8:
          print("Okay your coupon has been used")
          totalprice = totalprice - (totalprice * 0.08)
      if coupons.lower() == "no":
        riddle = input("What has a head, a tail but no legs?")
        if riddle.lower() == "coin":
          print("Congratulations you have earned 2% off")
          totalprice = totalprice - (totalprice * 0.02)
        
      totalprice = totalprice + (totalprice * 0.0725)
      totalprice = round(totalprice,2)
      print(f"The total price is {totalprice}")
      moneypaid = 0
      
      while moneypaid < totalprice:
        pay = float(input("Please input the price to pay: "))
        if pay == totalprice:
          print("Thank you, Have great day!")
          moneypaid += pay
        else:
          print("The inputted price is not valid, please try again.")
  
menu()
