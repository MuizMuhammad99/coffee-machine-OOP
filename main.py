from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    print("hello")
    coffee = input("What would you like? " + menu.get_items())
    if (coffee == 'report'):
        coffee_maker.report()
        money_machine.report()
    elif (coffee == 'off'):
        exit()
    else:
        drink = menu.find_drink(coffee)
        if (coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    main()
