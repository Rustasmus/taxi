import random

all_taxi = []
all_customer = []
all_orders = []
car_number_types = ('B', 'I', 'S', 'J', 'N', 'T', 'O', 'Z')
action = ''

while True:
    action = input('''
                    Enter 1 if you taxi driver
                    Enter 2 if you customer
                    Enter 3 if you want exit
                        ''').strip()
    driver_name = ''
    driver_surname = '0'
    car_number = '0'
    driver_licence_number = '0'
    experience = ''
    driver_phone_number = ''
    driver_password = ''

    customer_name = ''
    customer_surname = ''
    customer_phone_number = ''
    customer_email = ''
    customer_password = ''

    if action == '1' and action.isdigit():
        while driver_name.isdigit() or len(driver_name) <= 1:
            driver_name = input('Please input name: ').strip().capitalize()
            if len(driver_name) > 1 and driver_name.isalpha():
                while driver_surname.isdigit() or len(driver_surname) <= 1:
                    driver_surname = input('Please input surname: ').strip().capitalize()
                    if len(driver_surname) > 1 and driver_surname.isalpha():
                        while not (car_number[0] in car_number_types and car_number[-1] in car_number_types) or not car_number[1:-1].strip().isdigit():
                            car_number = input('Please input car number example "B 2222 B": ').upper().strip()
                            if (car_number[0] in car_number_types and car_number[-1] in car_number_types) and car_number[1:-1].strip().isdigit():
                                while not driver_licence_number.startswith('DL') or not driver_licence_number[
                                                                                        2:-1].isdigit():
                                    driver_licence_number = input(
                                        'Please input driver licence number: ').strip().upper()
                                    if driver_licence_number.startswith('DL') and driver_licence_number[2:-1].isdigit():
                                        while not experience == int or not 2 <= experience <= 60:
                                            experience = int(input('Please input experience: ').strip())
                                            if 2 <= experience <= 60:
                                                while not driver_phone_number.startswith(
                                                        '+996') or not driver_phone_number[1:].isdigit() or not len(
                                                        driver_phone_number) == 13:
                                                    driver_phone_number = input('Enter your phone number: ')
                                                    if driver_phone_number.startswith('+996') and driver_phone_number[
                                                                                                  1:].isdigit() and len(
                                                            driver_phone_number) == 13:
                                                        while not 8 < len(driver_password) <= 15:
                                                            driver_password = input('Enter you password: ').strip()
                                                            if 8 < len(driver_password) <= 15:
                                                                all_taxi.append((driver_name,
                                                                                 driver_surname,
                                                                                 car_number,
                                                                                 driver_licence_number,
                                                                                 experience,
                                                                                 driver_phone_number,
                                                                                 driver_password))
                                                            else:
                                                                print('Incorrect password')

                                                    else:
                                                        print('Incorrect phone number')
                                                break
                                            else:
                                                print('Incorrect experience')
                                    else:
                                        print('Incorrect driver licence number')
                            else:
                                print('Incorrect car number')
                    else:
                        print('Incorrect surname')
            else:
                print('Incorrect name')
        print(all_taxi)
    elif action == '2' and action.isdigit():
        if action == '2' and action.isdigit():
            while customer_name.isdigit() or len(customer_name) <= 1:
                customer_name = input('Please enter name: ').strip().capitalize()
                if len(customer_name) > 1 and customer_name.isalpha():
                    while not customer_phone_number.startswith('+996') or not customer_phone_number[1:].isdigit() or not len(customer_phone_number) == 13:
                        customer_phone_number = input('Enter your phone number: ')
                        if customer_phone_number.startswith('+996') and customer_phone_number[1:].isdigit() and len(customer_phone_number) == 13:
                            for i in range(5):
                                send_code = random.randint(1000, 9999)
                                print(f'{customer_phone_number} acepted code: {send_code}')
                                code = input('Enter sms code: ')
                                if code == str(send_code):
                                    all_customer.append((customer_name,
                                                         customer_phone_number,
                                                         customer_password))
                                    print(f'{customer_name} you registered success!')
                                    break
                                else:
                                    counter = 4
                                    print(f'Incorrect code! You have attend {counter - i}')
                        else:
                            print('Incorrect phone number')
                else:
                    print('Incorrect name')
        else:
            print('Incorrect action')
    elif action == '3' and action.isdigit():
        break
    else:
        print('Incorrect action, try again!')
print('you quit')
while True:
    print('Hi, welcome to MegaTaxi! Please authorisation!')
    phone_number = input().strip()
    if phone_number.startswith('+996') and phone_number[1:].isdigit() and len(phone_number) == 13:
        for customer in all_customer:
            if customer[1] == phone_number:
                print(f'Hi, {customer_name[0]} please enter authorisation code')
                send_code = random.randint(1000, 9999)
                print(f'Authorisation code is {send_code}.')
                code = input('Enter authorisation code: ')
                if str(send_code) == code:
                    point_a = input('Enter location A')
                    point_b = input('Enter location B')
                    driver = random.choice(all_taxi)
                    stavka = 39
                    stavka_per_km = 12
                    price = stavka + random.randint(0, 20) * stavka_per_km
                    if point_a == 'Earth' and point_b == 'Mars':
                        print(f'''
                                            location A: {point_a} to location B: {point_b}
                                            Driver, name: Elon Mask, car number: S tesla S, phone number: +996 555 555555555

                                            Price: smile :)

                                            ''')
                    else:

                        print(f'''
                        location A: {point_a} to location B: {point_b}
                        Driver, name: {driver[0]}, car number: {driver[2]}, phone number: {driver[-1]}
                        
                        price: {price}
                        
                        ''')
                    action = input('Press 1 to confirm order')
                    if action.isdigit() and action == '1':
                        all_orders.append((customer[1], point_a, point_b, price))
                        print(f'Your order accepted driver will be {random.randint(1, 10)} minute')
                    else:
                        print('Your order was canceled!')

                else:
                    print('Code didn`t match')
                    break
            else:
                print('Please sing up!')
                break
    else:
        print('Incorrect phone number.')
