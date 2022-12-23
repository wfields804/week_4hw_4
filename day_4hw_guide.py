#Brandt's model for hw 3.. to build on into hw 4. I do not know how to start this code.
#When I run it, nothing happens. 
#Going to try and do day 4 hw in pt.2


def shop():
    """Start grocery list."""
    input( 'Start grocery list here')
    cart = {}
    while True:
        main = input('show/add/etc. . . ')
        if main == 'add':
            add = input('whatchu want?')
            quan = input('how many?')
            cart[add] = quan
            print(f'you bought stuff!  here\'s where you\'re at: {cart}')
        elif main == 'quit':
            print(cart)
            break