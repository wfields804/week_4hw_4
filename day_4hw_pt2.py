#Excersise #1


basket = {}
class Cart():
    """A simple grocery list."""


    def __init__(self, milk, eggs, butter):
        
        while True:
            y = input("PLease choose: Add/Show/Delete or quit ")
            if y.lower() == 'add':
                product = input("What you want? ")
                items = input("How many? ")
                basket[product] = items
            elif y.lower() == 'delete':
                y = input("What to remove? ")
                del basket[y]
                print(f'okay {y} was removed')
            elif y.lower == 'show':
                print(f'here is your grocery list{basket}')
            elif y.lower() == 'quit':
                print("come back soon")
            break
            
        else:
            print("try again")

        self.milk = milk
        self.eggs = eggs
        self.butter = butter
        self.new_items = 0
    

    def grocery_list(self):
    
        first_items = str(self.milk) + "" + self.eggs + " " + self.butter
        return first_items.title()

    def show_items(self):

        print("This list has " + str(self.new_items) + " new items added. ")


    def update_list(self, items):
    
        self.new_items = items


my_current_list = Cart(10)
print(my_current_list.grocery_list()) 
my_current_list.new_items = 3
my_current_list.show_items()
my_current_list.update_list(0)
my_current_list.show_items()


#I think this is correct. I used the book as a refernce and guide. 
#I believe it has ways to add to list. Show list, but I could not figure out how to delete anything other than manaually deleting it from code. 
#It also shows list, but every changed needs to be changed manually. I wanted it to be auto matic from inputs, but I dont believe thats the assignment. 
#I cant get my "show" to work.
#I also cannot quit the loop


#I changed something now I cant figure out why code doesnt run :((( F***