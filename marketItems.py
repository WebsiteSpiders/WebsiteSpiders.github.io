from tkinter import *
from market import db
from market.models import Item, User
import uuid

barcode = uuid.uuid1()
barcode = barcode.node

print(barcode)
print(barcode)

root = Tk()
root.geometry("600x600")
root.title("Market Items")

class Widget:
    def __init__(self, root, grid):
        self.root = root
        self.row = grid[0]
        self.column = grid[1]

class labelWidget(Widget):
    def __init__(self, root, text, grid, padx):
        super().__init__(root, grid)
        self.text = text
        self.padx = padx
        
        self.Widget = Label(master=self.root, text=self.text, padx=self.padx)
        self.Widget.grid(row=self.row, column=self.column)
class entryWidget(Widget):
    def __init__(self, root, grid, width):
        super().__init__(root, grid)
        self.width = width
        
        self.Widget = Entry(master=self.root, width=self.width)
        self.Widget.grid(row=self.row, column=self.column)

def close():
    exit()

ItemNameLabel = labelWidget(root, "Item's Name:", [0,0], 40)
ItemPriceLabel = labelWidget(root, "Item's Price:", [1,0], 40)
ItemDescLabel = labelWidget(root, "Item's Description:", [2,0], 40)
ItemBarcodeLabel = labelWidget(root, "Item's Barcode:", [3,0], 40)

ItemNameEntry = entryWidget(root, [0,1], 25)
ItemPriceEntry = entryWidget(root, [1,1], 25)
ItemDescEntry = entryWidget(root, [2,1], 50)
ItemBarcodeEntry = entryWidget(root, [3,1], 20)

submitButton = Button(root, text="Submit", command=lambda: (addItem()), padx=10)
submitButton.grid(row=5, column=1)

def addItem():
    ItemName, VarName = ItemNameEntry.Widget.get(),ItemNameEntry.Widget.get()
    VarName = VarName.replace(" ", "_")
    ItemPrice = ItemPriceEntry.Widget.get()
    ItemDesc = ItemDescEntry.Widget.get()
    ItemBarcode = ItemBarcodeEntry.Widget.get()
    string = str(VarName) + f" = Item(name='{ItemName}', price='{ItemPrice}', description='{ItemDesc}', barcode='{ItemBarcode}')"
    exec(string)
    a = eval(VarName)
    db.session.add(a)
    db.session.commit()

mainloop()
