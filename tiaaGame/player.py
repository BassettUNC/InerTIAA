
from random import randint, uniform


class Player():

    """ Player characteristics """
    fname: str
    lname: str
    age: int
    occupation: str
    date: int
    yearly_salary: int
    expiration_age: int

    """ Cost of in-game items """
    house_zero_price: int = 81700
    house_one_price: int = 450000
    house_two_price: int = 2100000

    car_zero_price: int = 25000
    car_one_price: int = 85000
    car_two_price: int = 250000.0

    clothing_zero_price: int = 10
    clothing_one_price: int = 1000
    clothing_two_price: int = 10000

    """ Investment Options """
    # Store a dictionary of lists. key is id, amounts
    assets = {}
    # Ids: stockLow, stockMid, stockHigh, Roth, ira, 403b, tiaaTra, tiaaRP, tiaaRPP
    annual_ira_input: int = 0
    annual_403b_input: int = 0

    stock_low_price: int = 250
    stock_med_price: int = 73
    stock_high_price: int = 18

    """ Player finances """
    balance: float = 0.0
    # Balance before manditory expenses.
    balance_before_expenses: int = 0

    # 0: cheap, 1: medium, 2: expensive.
    house: int = 0
    # Yearly payment
    house_financed: int = 0
    house_payments_remaining: int = 0

    # 0: cheap, 1: medium, 2: expensive.
    car: int = 0
    # Yearly payment
    car_financed: int = 0
    car_payments_remaining: int = 0

    # 0: cheap, 1: medium, 2: expensive.
    clothing: int = 0
    # Yearly payment
    clothing_financed: int = 0
    clothing_payments_remaining: int = 0

    # Ammount of monthly annuity payout after death.
    monthly_annuity_payment: int = 0

    # Yearly Expenses: list[expense_name: str, expense_amount: int].
    yearly_financed_expenses = []
    yearly_outright_expenses = []

    def createPlayer():
        # Create Name Bank
        first_names: str = ['Zayna', 'Kelvin', 'Elijah', 'Aman', 'Anthony', 'Barack', 'Liam', 'Noah', 'Oliver', 'James', 'William', 'Benjamin', 'Luca', 'Henry', 'Theodore', 'Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Isaac', 'Jayden', 'Dylan', 'Lincoln', 'Jaxon', 'Isaiah', 'Andrew', 'Nolan', 'Cameron', 'Eli', 'Aaron', 'Ryan', 'Angel', 'Roman', 'Axel', 'Brooks', 'Jonathan', 'Robert', 'Hunter', 'Leo', 'Nick']
        last_names: str = ['Baltimore', 'Biffle', 'Canine', 'Chia', 'Wisener', 'Youtz', 'Felch', 'Imler', 'Thobe', 'Smith', 'Johnson', 'Belli', 'Khan', 'Han', 'Li', 'Lin', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Lee', 'Clark', 'Lewis', 'Allen', 'King', 'Hill', 'Flores', 'Baker', 'Carter', 'Roberts', 'Gomez', 'Phillips', 'Parker', 'Morris', 'Morales', 'Cook', 'Rogers', 'Cooper', 'Reed', 'Kelly', 'Kim', 'Cox', 'Chavez', 'Gray', 'Hughes', 'Price']
        # Randomly Create character
        random_int: int = randint(0, 11)
        # Firefighther
        if (random_int < 4):
            Player.occupation = "Firefighter"
            Player.yearly_salary = randint(45000, 54000)
            Player.age = randint(17, 21)

        # Teacher
        elif (random_int < 10):
            Player.occupation = "School Board Superintendent"
            Player.yearly_salary = randint(95000, 115000)
            Player.age = randint(28, 32)

        # Doctor
        else:
            Player.occupation = "Doctor"
            Player.yearly_salary = randint(420000, 505000)
            Player.age = randint(31, 36)

        Player.fname = first_names[randint(0, 45)]
        Player.lname = last_names[randint(0, 45)]
        Player.date = 2022
        Player.expiration_age = randint(70, 85)
        

    def addStock(id: str, shares: int):
        # If id has already been puchased... update amount.
        if id in Player.assets:
            if id == "stockLow" or id == "stockMid" or id == "stockHigh":
                if id == "stockLow":
                    if Player.balance > shares * Player.stock_low_price:
                        Player.assets["stockLow"] = Player.assets["stockLow"] + shares
                        Player.yearly_outright_expenses.append("stock low volatility contribution")
                        Player.yearly_outright_expenses.append(shares * Player.stock_low_price)
                    else: 
                        Player.popupError("not enough money")
                elif id == "stockMid":
                    if Player.balance > shares * Player.stock_med_price:
                        Player.assets["stockMid"] = Player.assets["stockMid"] + shares
                        Player.yearly_outright_expenses.append("stock mid volatility contribution")
                        Player.yearly_outright_expenses.append(shares * Player.stock_med_price)
                    else: 
                        Player.popupError("not enough money")
                elif id == "stockHigh":
                    if Player.balance > shares * Player.stock_high_price:
                        Player.assets["stockHigh"] = Player.assets["stockHigh"] + shares
                        Player.yearly_outright_expenses.append("stock high volatility contribution")
                        Player.yearly_outright_expenses.append(shares * Player.stock_high_price)
                    else: 
                        Player.popupError("not enough money")
            else:
                raise Exception("stock dne")
        elif id == "stockLow" or id == "stockMid" or id == "stockHigh":
                existing_shares = Player.assets.get(id)
                if id == "stockLow":
                    if Player.balance > shares * Player.stock_low_price:
                        Player.assets["stockLow"] = shares
                        Player.yearly_outright_expenses.append("stock low volatility contribution")
                        Player.yearly_outright_expenses.append(shares * Player.stock_low_price)
                    else: 
                        Player.popupError("not enough money")
                elif id == "stockMid":
                    if Player.balance > shares * Player.stock_med_price:
                        Player.assets["stockMid"] = shares
                        Player.yearly_outright_expenses.append("stock mid volatility contribution")
                        Player.yearly_outright_expenses.append(shares * Player.stock_med_price)
                    else: 
                        Player.popupError("not enough money")
                elif id == "stockHigh":
                    if Player.balance > shares * Player.stock_high_price:
                        Player.assets["stockHigh"] = shares
                        Player.yearly_outright_expenses.append("stock high volatility contribution")
                        Player.yearly_outright_expenses.append(shares * Player.stock_high_price)
                    else: 
                        Player.popupError("not enough money")
        else:
            raise Exception("stock dne")

    def addinvestment(id: str, ammount: int):
        # If id has already been puchased... update amount.
        if id in Player.assets:
            if id == "ira":
                if ammount > 6000:
                    Player.popupError("You cannot invest more than 6000 per year in an ira.")
                elif Player.balance > ammount:
                    Player.annual_ira_input += ammount
                    Player.assets["ira"] += ammount
                    Player.balance -= ammount
                    Player.yearly_outright_expenses.append("ira contribution")
                    Player.yearly_outright_expenses.append(ammount)
                else: 
                    Player.popupError("You do not have enough money for this action.")
            elif id == "403b":
                if  ammount > 19500:
                    Player.popupError("You cannot invest mor than 19500 per year in a 403b.")
                else:
                    if ammount < Player.yearly_salary and Player.balance > ammount  * 2:
                        Player.annual_403b_input += ammount * 2
                        Player.assets["403b"] += ammount * 2
                        Player.balance -= ammount
                        Player.yearly_outright_expenses.append("403b contribution")
                        Player.yearly_outright_expenses.append(ammount)
                    elif Player.balance > ammount:
                        Player.annual_403b_input += ammount
                        Player.assets["403b"] += ammount 
                        Player.balance -= ammount
                        Player.yearly_outright_expenses.append("403b contribution")
                        Player.yearly_outright_expenses.append(ammount)
                    else:
                        Player.popupError("You do not have enough money for this action.")

            elif id == "annuity":
                if Player.balance > ammount:
                    Player.assets["annuity"] += ammount
                    Player.balance -= ammount
                    Player.yearly_outright_expenses.append("annuity contribution")
                    Player.yearly_outright_expenses.append(ammount)
                else:
                    Player.popupError("You do not have enough money for this action.")

        # Otherwise add it
        else:
            asset_info: int = [0, 0]
            if id == "ira":
                if ammount > 6000:
                    Player.popupError("You cannot invest more than 6000 per year in an ira.")
                elif Player.balance > ammount:
                    Player.annual_ira_input = ammount
                    Player.assets["ira"] = ammount
                    Player.balance -= ammount
                    Player.yearly_outright_expenses.append("403b contribution")
                    Player.yearly_outright_expenses.append(ammount)
                else: 
                    Player.popupError("You do not have enough money for this action.")
            elif id == "403b":
                if  ammount > 19500:
                    Player.popupError("You cannot invest mor than 19500 per year in a 403b.")
                else:
                    if ammount < Player.yearly_salary and Player.balance > ammount  * 2:
                        Player.annual_403b_input = ammount * 2
                        Player.assets["403b"] = ammount * 2
                        Player.balance -= ammount
                        Player.yearly_outright_expenses.append("403b contribution")
                        Player.yearly_outright_expenses.append(ammount)
                    elif Player.balance > ammount:
                        Player.annual_403b_input = ammount
                        Player.assets["403b"] = ammount 
                        Player.balance -= ammount
                        Player.yearly_outright_expenses.append("403b contribution")
                        Player.yearly_outright_expenses.append(ammount)
                    else:
                        Player.popupError("You do not have enough money for this action.")

            elif id == "annuity":
                if Player.balance > ammount:
                    Player.assets["annuity"] = ammount
                    Player.balance -= ammount
                    Player.yearly_outright_expenses.append("annuity contribution")
                    Player.yearly_outright_expenses.append(ammount)
                else:
                    Player.popupError("You do not have enough money for this action.")
            
    def popupError(description: str):
        print(description)

    # Progress game by 1 year.
    def workProgress():
        # Clear yearly expense registry.
        del Player.yearly_financed_expenses[:]
        del Player.yearly_outright_expenses[:]
        # Clear annual retirement contributions
        Player.annual_ira_input = 0
        Player.annual_403b_input = 0

        # Progress date & Age.
        Player.date += 1
        Player.age += 1

        # check if expiration age is met.
        if Player.age == Player.expiration_age:
            print("you have died")
            quit()
        
        # Provide yearly pay if still working.
        # Define annuity payment vars.
        if "annuity" in Player.assets:
            r = .035
            k = 12
            n = (Player.expiration_age - 65)
            d = Player.assets["annuity"][0] / n
        if Player.age >= 65 and "annuity" in Player.assets:
            if Player.age == 65:
                Player.popupError("You have reached retirement. You will now reieve your annuity payout inplace of your salary.")
                Player.monthly_annuity_payment = (Player.expiration_age - 65) / Player.assets.get("annuity")[0]
            Player.balance += Player.monthly_annuity_payment
            Player.balance_before_expenses = Player.balance
        elif Player.age >= 65:
            if Player.age == 65:
                Player.popupError("You have reached retirement.")
        else:
            Player.balance += Player.yearly_salary
            Player.balance_before_expenses = Player.balance

        # Subtract manditory expenses for financed items & retirement and add to expense registry.
        if Player.car_payments_remaining > 0:
            # Add payment to yearly ledger.
            Player.yearly_financed_expenses.append("car")
            Player.yearly_financed_expenses.append(str(Player.car_financed))
            # Deduct from player balanece.
            Player.balance -= Player.car_financed
            # Note payment made.
            Player.car_payments_remaining -= 1

        if Player.house_payments_remaining > 0:
            # Add payment to yearly ledger.
            Player.yearly_financed_expenses.append("house")
            Player.yearly_financed_expenses.append(str(Player.house_financed))
            # Deduct from player balanece.
            Player.balance -= Player.house_financed
            # Note payment made.
            Player.house_payments_remaining -= 1

        if Player.clothing_payments_remaining > 0:
            # Add payment to yearly ledger.
            Player.yearly_financed_expenses.append("house")
            Player.yearly_financed_expenses.append(str(Player.house_financed))
            # Deduct from player balanece.
            Player.balance -= Player.car_financed
            # Note payment made.
            Player.house_payments_remaining -= 1

        # TODO: implement sell shares. check for shares = 0 and remove from assets.

        keys = Player.assets.keys()
        # Handle stocks.
        if "stockLow" in keys:
            stock_mod: float
            if randint(0, 1) == 0:
                stock_mod = uniform(1.05, 1.07)
            else:
                stock_mod = uniform(.93, .95)
            Player.assets["stockLow"] *= stock_mod
            Player.stock_low_price *= stock_mod
        if "stockMid" in keys:
            stock_mod: float
            if randint(0, 1) == 0:
                stock_mod = uniform(1.07, 1.1)
            else:
                stock_mod = uniform(.90, .93)
            Player.assets["stockMid"] *= stock_mod
            Player.stock_med_price *= stock_mod
        if "stockHigh" in keys:
            stock_mod: float
            if randint(0, 1) == 0:
                stock_mod = uniform(1.1, 1.2)
            else:
                stock_mod = uniform(.8, .9)
            Player.assets["stockHigh"] *= stock_mod
            Player.stock_high_price *= stock_mod

        # Handle basic retirement.
            if "ira" in keys:
                Player.assets["ira"] *= 1.00643403011
            if "403b" in keys:
                Player.assets["ira"] *= 1.00643403011

        
        if Player.balance < 0 :
            Player.popupError("You cannot afford to pay your bills. GAME OVER.")
            quit()


    # Method to handle ingame purchases, both financed and outright.
    def buyItem(item: str, financed: bool):
        if financed:
            if item == "car0" or item == "car1" or item == "car2":
                if(Player.car_payments_remaining != 0):
                    Player.popupError("You must pay off your old car first")
                else:
                    if item == "car0":
                        if(Player.balance < Player.car_zero_price * .1):
                            Player.popupError("Insufficient funds for 10 percent downpayment")
                        else:
                            Player.car = 0
                            Player.car_financed = (Player.car_zero_price *.9) *(.47*(1.47)**60)/((1.47**60)-1) *12
                            Player.balance -= Player.car_zero_price * .1
                            Player.car_payments_remaining = 5
                            Player.popupError("Congradulations, you have financed the C-Class")
                    elif item == "car1":
                        if(Player.balance < Player.car_one_price * .1):
                            Player.popupError("Insufficient funds for 10 percent downpayment")
                        else:
                            Player.car = 1
                            Player.car_financed = (Player.car_one_price *.9) *(.47*(1.47)**60)/((1.47**60)-1) *12
                            Player.balance -= Player.car_one_price * .1
                            Player.car_payments_remaining = 5
                            Player.popupError("Congradulations, you have financed the B-Class")
                    elif item == "car2":
                        if(Player.balance < Player.car_two_price * .1):
                            Player.popupError("Insufficient funds for 10 percent downpayment")
                        else:
                            Player.car = 2
                            Player.car_financed = (Player.car_two_price *.9) *(.47*(1.47)**60)/((1.47**60)-1) *12
                            Player.balance -= Player.car_two_price * .1
                            Player.car_payments_remaining = 5
                            Player.popupError("Congradulations, you have financed the S-Class")
            elif item == "house0" or item == "house1" or item == "house2":
                if(Player.house_payments_remaining != 0):
                    Player.popupError("You must pay off your old house first")
                else:
                    Player.house_payments_remaining = 20
                    if item == "house0":
                        Player.house = 0
                        Player.house_financed = Player.house_zero_price * (.534*(1.534)**240)/((1.543**240)-1) *12
                        Player.popupError("Congradulations, you have financed a trailer")
                    elif item == "house1":
                        Player.house = 1
                        Player.house_financed = Player.house_one_price * (.534*(1.534)**240)/((1.543**240)-1) *12
                        Player.popupError("Congradulations, you have financed a single family home")
                    elif item == "house2":
                        Player.house = 2
                        Player.house_financed = Player.house_two_price * (.534*(1.534)**240)/((1.543**240)-1) *12
                        Player.popupError("Congradulations, you have financed a mansion")
            elif item == "house0" or item == "house1" or item == "house2":
                if(Player.clothing_payments_remaining != 0):
                    Player.popupError("You must pay off your old character first")
                else:
                    Player.clothing_payments_remaining = 5
                    if item == "clothing0":
                        Player.clothing = 0
                        Player.clothing_financed = Player.clothing_zero_price * (.534*(1.534)**5)/((1.543**5)-1) *12
                    elif item == "clothing1":
                        Player.clothing = 1
                        Player.clothing_financed = Player.clothing_one_price * (.534*(1.534)**5)/((1.543**5)-1) *12
                    elif item == "clothing2":
                        Player.clothing = 2
                        Player.clothing_financed = Player.clothing_two_price * (.534*(1.534)**5)/((1.543**5)-1) *12
            else: 
                raise Exception("Item not found. Cannot buy!")
        else:
            # Item is not financed.
            if item == "car0" or item == "car1" or item == "car2":
                if(Player.car_payments_remaining != 0):
                    Player.popupError("You must pay off your old car first")
                else:
                    Player.car_financed = 0
                    Player.yearly_outright_expenses.append("car")
                    if item == "car0":
                        if(Player.balance < Player.car_zero_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.car = 0
                            Player.balance -= Player.car_zero_price
                            Player.yearly_outright_expenses.append(str(Player.car_zero_price))
                            Player.popupError("Congradulations, you have purchased a C-Class")
                    elif item == "car1":
                        if(Player.balance < Player.car_one_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.car = 1
                            Player.balance -= Player.car_one_price
                            Player.yearly_outright_expenses.append(str(Player.car_one_price))
                            Player.popupError("Congradulations, you have purchased a B-Class")
                    elif item == "car2":
                        if(Player.balance < Player.car_two_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.car = 2
                            Player.balance -= Player.car_two_price
                            Player.yearly_outright_expenses.append(str(Player.car_two_price))
                            Player.popupError("Congradulations, you have purchased a S-Class")
            elif item == "house0" or item == "house1" or item == "house2":
                if(Player.house_payments_remaining != 0):
                    Player.popupError("You must pay off your old house first")
                    Player.yearly_outright_expenses.append("house")
                else:
                    Player.housing_financed = 0
                    if item == "house0":
                        if(Player.balance < Player.house_zero_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.house = 0
                            Player.balance -= Player.house_zero_price
                            Player.yearly_outright_expenses.append(str(Player.house_zero_price))
                            Player.popupError("Congradulations, you have purchased a trailer")
                    elif item == "house1":
                        if(Player.balance < Player.house_one_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.balance -= Player.house_one_price
                            Player.house = 1
                            Player.yearly_outright_expenses.append(str(Player.house_one_price))
                            Player.popupError("Congradulations, you have purchased a single family home")
                    elif item == "house2":
                        if(Player.balance < Player.house_two_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.balance -= Player.house_two_price
                            Player.house = 2
                            Player.yearly_outright_expenses.append(str(Player.house_two_price))
                            Player.popupError("Congradulations, you have purchased a mansion")
            elif item == "clothing0" or item == "clothing1" or item == "clothing2":
                if(Player.clothing_payments_remaining != 0):
                    Player.popupError("You must pay off your old character first")
                else:
                    Player.clothing_financed = 0
                    Player.yearly_outright_expenses.append("house")
                    if item == "clothing1":
                        if(Player.balance < Player.clothing_zero_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.clothing = 0
                            Player.balance -= Player.clothing_zero_price
                            Player.yearly_outright_expenses.append(str(Player.clothing_zero_price))
                    elif item == "clothing1":
                        if(Player.balance < Player.clothing_one_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.clothing = 1
                            Player.balance -= Player.clothing_one_price
                            Player.yearly_outright_expenses.append(str(Player.clothing_one_price))
                    elif item == "clothing2":
                        if(Player.balance < Player.clothing_two_price):
                            Player.popupError("Insufficient funds")
                        else:
                            Player.clothing = 2
                            Player.balance -= Player.clothing_two_price
                            Player.yearly_outright_expenses.append(str(Player.clothing_two_price))
            else: 
                raise Exception("Item not found. Cannot buy!")

