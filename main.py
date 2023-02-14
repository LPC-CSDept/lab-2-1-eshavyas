def main():
   ##################################################
   # Comlete your code here
   ##################################################
   # This program gets an item's original price and
   # calculates its sale price, with 20% discount.

   # Get the item's orginal price.
   original_price =float (input("Enter the item original price: "))
   drate = int (input("Enter the item original price: "))

   # Calculate the amount of the discount.
#    discount = "original_price" *2
   discount = original_price * drate / 100

   # Calculate the sale price. 
   sale_price= original_price - discount

   #Display the sale price. 
   print ('The original price is', original_price)
   print ('The sale price is', sale_price)

   #pass

if __name__ == '__main_':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
  main()
