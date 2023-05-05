MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ew = MENU["espresso"]["ingredients"]["water"]
ec = MENU["espresso"]["ingredients"]["coffee"]
em = 0
ecost = MENU["espresso"]["cost"]
lw = MENU["latte"]["ingredients"]["water"]
lc = MENU["latte"]["ingredients"]["coffee"]
lm = MENU["latte"]["ingredients"]["milk"]
lcost =MENU["latte"]["cost"]
cw =MENU["cappuccino"]["ingredients"]["water"]
cc = MENU["cappuccino"]["ingredients"]["coffee"]
cm = MENU["cappuccino"]["ingredients"]["milk"]
ccost =MENU["cappuccino"]["cost"]
rw= resources["water"]
rc= resources["coffee"]
rm = resources["milk"]
def ask_money():
    q = float(input("quarters:"))
    d = float(input("dimes:"))
    n = float(input("nickel:"))
    p = float(input("pennies:"))
    money = q*0.25 + d*0.1 + n*0.05 + p*0.01
    return money
make_drink = True
while make_drink:
    drink = input('what would you like? (espresso/latte/cappuccino):\n')
    if drink == 'espresso':
        if rw >= ew and rc >= ec:
            print("insert coins")
            total = ask_money()
            if total == ecost:
                print("Here is your espresso. Enjoy!")
                rw -= ew
                rm -= em
                rc -= ec
            elif total > ecost:
                refund = total - ecost
                print("Here is your espresso. Enjoy!")
                print(f"Here is {refund} dollars in change.")
                rm -= em
                rc -= ec
                rw -= ew

            elif total < ecost:
                print("Sorry that's not enough money. Money refunded.")
                make_drink = False

        elif rw < ew:
            print("sorry there is not enough water")
            make_drink = False
        elif rc < ec:
            print("sorry there is not enough coffee")
            make_drink = False
    elif drink == 'report':
            print(f"water: {rw} ml\nmilk: {rm} ml\ncoffee: {rc} ml\nmoney = ${ecost}")

