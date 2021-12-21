# Write your code here
print("""The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money""")


water = 400
milk = 540
bean = 120
cups = 9
money = 550

while True:
    standard_input = input('Choose to (buy, fill, take, remaining, exit): ')

    if standard_input == 'buy':
        coffee_input = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if coffee_input == '1':
            if water >= 250:
                water = water - 250
                milk = milk - 0
                bean = bean - 16
                cups = cups - 1
                money = money + 4
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough water!')

        elif coffee_input == '2':
            if water >= 350:
                water = water - 350
                milk = milk - 75
                bean = bean - 20
                cups = cups - 1
                money = money + 7
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough water!')

        elif coffee_input == '3':
            if water >= 200:
                water = water - 200
                milk = milk - 100
                bean = bean - 12
                cups = cups - 1
                money = money + 6
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough water!')

        elif coffee_input == 'back':
            continue

    elif standard_input == 'fill':
        water_input = int(input('Write how many ml of water you want to add: '))
        milk_input = int(input('Write how many ml of milk you want to add: '))
        bean_input = int(input('Write how many grams of coffee beans you want to add: '))
        cups_input = int(input('Write how many disposable coffee cups you want to add: '))

        water = water + water_input
        milk = milk + milk_input
        bean = bean + bean_input
        cups = cups + cups_input

    elif standard_input == 'take':
        print(f'I gave you ${money}')
        money = money - money

    elif standard_input == 'remaining':
        print(f"""The coffee machine has:
{water} of water
{milk} of milk
{bean} of coffee beans
{cups} of disposable cups
${money} of money""")

    elif standard_input == 'exit':
        break