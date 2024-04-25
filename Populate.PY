import random

data = open('Populate.SQL', 'w')
names, countries, cities = [], [], []
regions = ["Africa", "Asia", "Middle East", "Europe", "Others"]


def load_data():
    file = open('data.csv', 'r', encoding='utf-8')
    for line in file:
        if "'" in line:
            continue
        try:
            line_data = line.split(',')
            names.append(line_data[0])
            countries.append(line_data[1])
            cities.append(line_data[2])
        except:
            continue
    file.close()


load_data()


def populate_passengers():
    size = len(names)
    j = 0
    # Construct Insert Statements
    for i in range(5000):
        ran = random.randint(0, 10)
        name = names[i % size]
        gender = "M" if ran % 2 == 0 else "F"
        country = countries[i % size]
        city = cities[i % size]
        region = random.choice(regions)
        age = random.randint(18, 50)

        row = f"INSERT INTO PassengerDim VALUES ({j}, {i}, '{name}', '{gender}', '{country}', {age}, '{region}', " \
              f"'{city}', '1575', 'email');\n"
        try:
            data.write(row)
            j += 1
        except:
            continue


def populate_class():
    classes = ["basic Economy", "Economy", "Prem Economy", "Business", "First", "VIP"]
    i = 0
    for purchased_class in classes:
        for flown_class in classes:
            if purchased_class == flown_class:
                class_change = "No Class Change"
            elif classes.index(purchased_class) > classes.index(flown_class):
                class_change = "Downgrade"
            else:
                class_change = "Upgrade"
            i += 1
            row = f"INSERT INTO ClassDim VALUES ({i}, {i}, '{purchased_class}', '{flown_class}'," \
                  f" '{purchased_class} - {flown_class}', '{class_change}');\n "
            data.write(row)


def populate_promotion():
    classes = ["discount", "bonus miles", "upgrade", "services", "food", "drink"]
    for i in range (500):
        type_ = random.choice(classes)
        amount = random.randint(0, 100)

        row = f"INSERT INTO PromotionDim VALUES ({i}, {i}, '{type_}', sysdate," \
              f" sysdate, 'terms', {amount});\n "
        data.write(row)


def populate_date():
    seasons = ["Summer", "Winter", "Spring", "Autumn"]
    for i in range(3650):
        year = 2015 + i // 365
        month = (i % 12) + 1
        day = (i % 30) + 1
        if month == 2 and day > 28:
            continue
        quarter = month % 4
        season = seasons[quarter]
        row = f"INSERT INTO DateDim VALUES ({i}, to_date('{month}-{day}-{year}', 'MM-DD-YYYY'), {day}, 0," \
              f" 0, 0, {month}, {quarter}, {year}, {month}, {quarter}, {year},0, '{season}');\n"
        data.write(row)


def populate_flight():
    for i in range(1000):
        duration = abs(random.gauss(3, 2))
        distance = abs(random.gauss(100, 50))
        row = f"INSERT INTO FlightDim VALUES ({i}, {duration}, {distance}," \
              f" 0, 0, 0, 0);\n"
        data.write(row)


def populate_profile():
    tiers = {"Basic": "Under 100,000 miles"
             , "Mid Tier": "100,000-499.999 miles",
             "High Tier": "500,000-999,999 miles",
             "Worrier Tier": "1000,000-2,000,000 miles",
             "Legend Tier": "Above 2,000,000 miles"}
    airports = ['ATL', "BOS", "SBN", "ABC", "BCD",
                "EFG", "KIN", "NPN", "MMM", "AAA"]
    i = 0
    for tier in tiers.keys():
        for membership in ["Non-Member", "Club Member"]:
            for airport in airports:
                i += 1
                row = f"INSERT INTO PassengerProfileDim VALUES ({i}, '{tier}', '{airport}'," \
                    f" '{membership}', '{tiers[tier]}');\n"
                data.write(row)


def populate_booking():
    for i in range(10000):
        row = f"INSERT INTO BookingDim VALUES ({i}, '{i}', {random.randint(1, 100)}," \
              f" {random.randint(1, 15)}, {random.randint(1, 100000)});\n"
        data.write(row)


def populate_interaction():
    i = 0
    for j in ['Inquiry', 'Feedback', 'Complaint']:
        for severity in range(5):
            for when in ('After', 'Before', 'Within', 'Others'):
                i += 1
                row = f"INSERT INTO Interaction VALUES ({i}, {i}, {severity}," \
                      f" '{j}', '{when}', 0);\n"
                data.write(row)


def populate_time():
    i = 0
    for hour in range(24):
        for minute in range (60):
            i += 1
            row = f"INSERT INTO TimeOfDayDim VALUES ({i}, {i}, {hour}," \
                f" {minute});\n"
            data.write(row)


def populate_channel():
    i = 0
    channels = {'Website': ['Online', 'Indirect', 'Others', '24/7']
                , 'Mobile App': ['Online', 'Indirect', 'Others', '24/7']
                , 'Agent': ['third party', 'Indirect', 'phone', 'partial']
                , 'Call Center': ['offline', 'direct', 'phone', 'partial']
                , 'site': ['offline', 'direct', 'other', 'partial']
                , 'Others': ['others', 'others', 'Others', 'others']}
    for channel in channels.keys():
        i += 1
        values = channels[channel]
        row = f"INSERT INTO ChannelDim VALUES ({i}, {i}, '{channel}'," \
              f" '{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}');\n"
        data.write(row)


def populate_airport():
    j = 1
    for i in range(990):
        city = cities[i]
        country = countries[i]
        region = random.choice(regions)
        lat = random.randint(1, 360)
        lon = random.randint(1, 360)
        row = f"INSERT INTO AirportDim VALUES ({j}, {i}, '{city[0]}{country[0]}{region[0]}', '{city} Airport'," \
              f" '{city}', 'state {i % 15}', '{country}', '{region}', '{country[0:3]} Zone', {lat}, {lon});\n "
        try:
            data.write(row)
            j += 1
        except:
            continue


def populate_aircraft():
    types = ["Commercial Jet Airliners", "Regional Airliners", "Business Jets", "Cargo Aircraft"]
    manufacturers = [
                    "Airbus",
                    "Boeing",
                    "Bombardier",
                    "Embraer",
                    "McDonnell Douglas",
                    "Tupolev",
                    "Ilyushin",
                    "Antonov",
                    "Fokker",
                    "British Aerospace"
                    ]
    models = [
        "A300",
        "A310",
        "A318",
        "A320",
        "A330",
        "A340",
        "A350",
        "A380"
            ]
    for i in range(500):
        type_ = random.choice(types)
        manufacturer = random.choice(manufacturers)
        model = random.choice(models)
        capacity = random.randint(15, 500)
        fuel_capacity = random.randint(100, 500)
        wing_span = random.gauss(12, 3)
        length = random.gauss(5, 1)

        row = f"INSERT INTO AircraftDim VALUES ({i}, {i}, '{type_}', '{manufacturer}'," \
              f" '{model}', {capacity}, {fuel_capacity}, {wing_span}, {length});\n "
        data.write(row)


def populate_employee():
    j = 1
    roles = ["Captain", 'Co Captain', 'Flight Attendant', 'Data Engineer',
             'ML Engineer', 'Flight Agent', 'Receptionist', 'Office Girl',
             'Coffee Girl']
    for i in range(5000):
        name = names[i % 990]
        city = cities[i % 990]
        country = countries[i % 990]
        region = random.choice(regions)
        gender = random.choice(("M", "F"))
        age = random.randint(18, 50)
        role = random.choice(roles)
        row = f"INSERT INTO EmployeeDim VALUES ({j}, {i}, '{name}', '{gender}', '{country}', '{city}', {age}, " \
              f"'{region}', 'email', '00100', sysdate, '{role}');\n"
        try:
            data.write(row)
            j += 1
        except:
            continue


def populate_flight_activity():
    for i in range(100000):
        booked_seats = random.randint(10, 400)
        passenger_count = booked_seats - random.randint(5, 25)
        empty_seats = booked_seats - passenger_count
        empty_seats = empty_seats if empty_seats >= 0 else 0
        fuel_consumption = random.randint(100, 250)
        crew_count = random.randint(10, 40)
        src_ap = random.randint(1, 924)
        dst_ap = random.randint(1, 924)
        arr_date = random.randint(0, 3649)
        arr_date2 = random.randint(0, 3649)
        dep_date = random.randint(0, 3649)
        dep_date2 = random.randint(0, 3649)
        flight = random.randint(0, 999)
        aircraft = random.randint(0, 499)
        captain = random.randint(1, 4667)
        co_captain = random.randint(1, 4667)
        row = f"INSERT INTO FlightActivity VALUES ({booked_seats}, {passenger_count}, {empty_seats}, " \
              f"{fuel_consumption}, {crew_count}, {src_ap}, {dst_ap}, {arr_date}, {arr_date2}, " \
              f" {dep_date}, {dep_date2}, {flight}, {aircraft}, {captain}, {co_captain});\n"
        data.write(row)


def populate_flight_reservations():
    for i in range(250000):
        fare = random.gauss(500, 1000)
        fare = abs(fare)
        res = i
        rev = abs(random.gauss(100, 50))
        g_tax = random.randint(10, 30)
        a_tax = random.randint(10, 30)
        s_fees = random.randint(10, 20)
        o_fees = random.randint(10, 20)
        b_fees = random.randint(10, 20)
        discount = int(fare * random.random())
        u_fees = abs(random.gauss(40, 20))
        dep_date = random.randint(0, 3649)
        passenger = random.randint(0, 4666)
        channel = random.randint(1, 6)
        class_ = random.randint(1, 36)
        fare_base = random.randint(1, 5)
        src_ap = random.randint(1, 924)
        dst_ap = random.randint(1, 924)
        profile = random.randint(1, 100)
        dep_time = random.randint(1, 1440)
        row = f"INSERT INTO Reservations VALUES ({fare}, {res}, {rev}, {g_tax}, " \
              f"{a_tax}, {s_fees}, {o_fees}, {b_fees}, {discount}, {u_fees}, " \
              f" {dep_date}, {passenger}, {channel}, {class_}, {fare_base}, {src_ap}, {dst_ap}, {profile}, {dep_time});\n"
        data.write(row)


def populate_frequent_flyers():
    for i in range(150000):
        redeemed = random.gauss(100, 500)
        earned = random.gauss(100, 500)
        cancelled = random.randint(0, 1)
        over_ns = abs(random.gauss(8, 12))
        res = i
        passenger = random.randint(0, 4666)
        status = random.randint(1, 3)
        fare_base = random.randint(1, 5)
        class_ = random.randint(1, 36)
        promotion = random.randint(0, 499)
        res_date = random.randint(0, 3649)
        src_ap = random.randint(1, 924)
        dst_ap = random.randint(1, 924)
        profile = random.randint(1, 100)
        booking = random.randint(0, 9999)
        channel = random.randint(1, 6)
        flight = random.randint(0, 999)

        row = f"INSERT INTO FrequentFlyers VALUES ({redeemed}, {earned}, {cancelled}, " \
              f"{over_ns}, {res}, {passenger}, {status}, {fare_base}, {class_}, " \
              f" {promotion}, {res_date}, {src_ap}, {dst_ap}, {profile}, {booking}, " \
              f"{channel}, {flight});\n"
        data.write(row)


def populate_customer_care():
    for i in range(15000):
        res_del = random.gauss(10, 30)
        if random.randint(1, 100) == 15:
            res_del += 100 * random.randint(1, 15)
        resol_del = random.gauss(10, 30)
        if random.randint(1, 100) == 15:
            resol_del += 100 * random.randint(1, 15)
        duration = random.gauss(1, 15)
        profile = random.randint(1, 100)
        flight = random.randint(0, 999)
        passenger = random.randint(0, 4666)
        sub_date = random.randint(0, 3649)
        res_date = random.randint(0, 3649)
        resol_date = random.randint(0, 3649)
        channel = random.randint(1, 6)
        employee = random.randint(1, 4667)
        interaction = random.randint(1, 60)
        sub_time = random.randint(1, 1440)
        res_time = random.randint(1, 1440)
        sol_time = random.randint(1, 1440)

        row = f"INSERT INTO CustomerCare VALUES ({res_del}, {resol_del}, {duration}, " \
              f"{profile}, {flight}, {passenger}, {sub_date}, {res_date}, {resol_date}, " \
              f" {channel}, {employee}, {interaction}, {sub_time}, {res_time}, {sol_time});\n"
        data.write(row)


# populate_passengers()
# populate_class()
# populate_promotion()
# populate_date()
# populate_flight()
# populate_profile()
# populate_booking()
# populate_interaction()
# populate_time()
# populate_channel()
# populate_airport()
# populate_aircraft()
# populate_employee()
# populate_flight_activity()
# populate_flight_reservations()
# populate_frequent_flyers()
populate_customer_care()
