from typing import Dict, Union, Optional
from computer import *


class ResaleShop:


   # What attributes will it need?
   inventory: list
   itemID: int




   # How will you set up your constructor?
   # Remember: in python, all constructors have the same name (__init__)
   def __init__(self, inventory, itemID):
       self.inventory = inventory
       self.itemID = itemID


       # What methods will you need?
   def buy(self, computer):
       self.itemID += 1 # increment itemID
       self.inventory.append(computer)
       return self.itemID


   def update_price(self, item_id: int, new_price: int):
       if len(self.inventory) > self.item_id-1:
           self.inventory[item_id-1].price = new_price
       else:
           print("Item", item_id, "not found. Cannot update price.")


   def sell(self, item_id: int):
       if len(self.inventory) > item_id-1:
           del self.inventory[item_id-1]
           print("Item", item_id, "sold!")
       else:
           print("Item", item_id, "not found. Please select another item to sell.")


   def print_inventory(self):
       # If the inventory is not empty
       if self.inventory:
           item_id = 1
           # For each item
           for computer in self.inventory:
               # Print its details
               print('Item ID: '+str(item_id))
               print(computer.__str__())
               item_id += 1
       else:
           print("No inventory to display.")


   def refurbish(self,item_id: int, new_os: Optional[str] = None):
       if len(self.inventory) > item_id-1:
           computer = self.inventory[item_id-1] # locate the computer
           if int(computer.year_made) < 2000:
               computer.price = 0 # too old to sell, donation only
           elif int(computer.year_made) < 2012:
               computer.price = 250 # heavily-discounted price on machines 10+ years old
           elif int(computer.year_made) < 2018:
               computer.price = 550 # discounted price on machines 4-to-10 year old machines
           else:
               computer.price = 1000 # recent stuff


           if new_os is not None:
               computer.operating_system = new_os # update details after installing new OS
       else:
           print("Item", item_id, "not found. Please select another item to refurbish.")


def main():
  
   computer = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
   resale = ResaleShop([], 0)


   print("-" * 21)
   print("COMPUTER RESALE STORE")
   print("-" * 21)


   # Add it to the resale store's inventory
   print("Buying", computer.description)
   print("Adding to inventory...")
   computer_id = resale.buy(computer)
   print("Done.\n")


   # Make sure it worked by checking inventory
   print("Checking inventory...")
   resale.print_inventory()
   print("Done.\n")


   # Now, let's refurbish it
   new_OS = "MacOS Monterey"
   print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
   print("Updating inventory...")
   resale.refurbish(computer_id, new_OS)
   print("Done.\n")


   # Make sure it worked by checking inventory
   print("Checking inventory...")
   resale.print_inventory()
   print("Done.\n")
  
   # Now, let's sell it!
   print("Selling Item ID:", computer_id)
   resale.sell(computer_id)
  
   # Make sure it worked by checking inventory
   print("Checking inventory...")
   resale.print_inventory()
   print("Done.\n")


# Calls the main() function when this file is run
if __name__ == "__main__": main()
