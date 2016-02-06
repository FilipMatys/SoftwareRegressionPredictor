class Menu:
   # Initialize menu
   def __init__(self, items):
      self.menu_items = items

   # Show menu
   def show(self):
      for item in self.menu_items:
         print(1 + self.menu_items.index(item), ". " + item[0])

   # Run menu
   def run(self):
      self.show()

      while True:
         try:
            choice = int(input()) - 1
         except ValueError:
            print("Please, enter numerical value.")
            continue

         if choice < 0 or choice >= len(self.menu_items):
            print("Please, choose valid option.")
            continue

         self.menu_items[choice][1]()