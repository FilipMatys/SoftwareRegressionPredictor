from Menu import Menu
from plugins.dejagnu.Parser import Parser

def showHello():
   print("Ahojky")

def main():
   print("Starting...");
   cm = Menu([("Ahoj", showHello)])
   cm.run()

# Call the main function
if __name__ == "__main__":
   main();    