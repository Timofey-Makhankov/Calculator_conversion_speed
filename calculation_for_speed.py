# calculation for speed
def cal_Speed_MperS():
    distance = float(input("give distance in meters: "))
    time = float(input("give time in seconds: "))
    speed = distance / time
    print(f"The result: {speed} m/s")

# calculation for distance
def cal_Distance_MperS():
    speed = float(input("give speed in m/s: "))
    time = float(input("give time in seconds: "))
    distance = speed * time
    print(f"The result: {distance} meters")

# calculation for time
def cal_Time_MperS():
    distance = float(input("give distance in meters: "))
    speed = float(input("give speed in m/s: "))
    time = distance / speed
    print(f"The result: {time} seconds")

# conversion from KM/h to M/s
def Conversion_for_MperS():
    speed = float(input("give speed in Km/h: "))
    product = speed / 3.6
    print(f"The result: {product} m/s")

# conversion from M/s to KM/h
def Conversion_for_KMperH():
    speed = float(input("give speed in m/s: "))
    product = speed * 3.6
    print(f"The result: {product} Km/h")

# Instruction for commands
print('''
commands:
Speed -> calculate speed
Time -> calculate time
Distance -> calculate distance
Convert -> M/s to KM/h and vice versa
break -> stop the Program
''')

while(1):

# if any of the calculation is chosen
    command : str = input('> ')
    if command.lower() == 'speed':
        cal_Speed_MperS()
    if command.lower() == 'time':
        cal_Time_MperS()
    if command.lower() == 'distance':
        cal_Distance_MperS()

# if conversion is used
    if command.lower() == 'convert':

# instruction for conversions
        print('''
The Output will be what is chosen

get meters = M
get kilometers = K 
        ''')
        command : str = input('meters or kilometers?: ')

# logic for output in meters or kilometers
        if command.lower() == 'm':
            Conversion_for_MperS()
        else:
            Conversion_for_KMperH()

# to stop the (loop) program
    if command.lower() == 'break':
        break