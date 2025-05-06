import calories as c
import tracker2 as t
import db as db

db.create_tables()

def login_or_signup():
    
    L_or_S = int(input("Enter 1 to Login or 2 to Sign up\n"))

    if L_or_S == 1:
        old_user = 1
        user_id = t.login()
        if user_id is None:
            print("Login failed. try logging in again.")
            login_or_signup()
        
    elif L_or_S == 2:
        user_id = t.signup()
        old_user = 0
        if user_id is None:
            print("Signup failed. try signing up again or login if new user.")
            login_or_signup()
        else:
             old_user = 0
        
 
    else:
        print("Invalid option. try again.")
        login_or_signup()

    return old_user, user_id

old_user ,user_id= login_or_signup()



if old_user == 0:
    print("Welcome to your personal fitness tracker!\n")
    print("lets start tracking your habits and make them better\n")
    print("Please enter the required data to help understand your physical health:\n")
elif old_user == 1:
    print("Welcome back to your personal fitness tracker!\n")
    print("lets continue tracking your habits and make them even better\n") 



gender = input("enter your gender \n").strip().lower()

def bmi():
    height = int(input("\nenter your height in cm \n"))
    weight = int(input("\nenter your weight in kgs\n"))
    m = height*0.01
    height = m
    BMI= weight/(height*height)

    return BMI, height, weight

BMI,height,weight= bmi()

print(f"Your BMI is {BMI}:\n")

if (BMI>18.5 and BMI<25):
    print("you have a healthy BMI\n")
    def goal():
        goal= int(input("Do you want to 1. gain or 2.lose weight?\n "))
        if goal == 1:
            print("You need to gain weight\n")
        elif goal == 2:
            print("You need to lose weight\n")
        else:
            print("enter valid option and try again\n")
            goal= goal()
        return goal
    goal= goal()
    

elif (BMI<18.5):
    print("you are under weight\n")
    goal= 1
    print("You need to gain weight\n")
elif (BMI>25 and BMI<30 ):
    print("you are overweight\n")
    print("You need to lose weight\n")
    goal= 2
elif (BMI>30):
    print("you are obese\n")
    print("You need to lose weight\n")
    goal= 2
else:
    print("enter valid height and weight\n")

print(" lets start tracking your habits and make them better\n")

sleep = int(input("Enter your sleep hours\n"))
# i need to make something which could help the user track his prevvious sleep hours and then compare it 
if sleep < 6:
    print("You need to sleep more\n")
elif sleep > 8:
    print("You are sleeping too much\n")
else:
    print("You are sleeping well\n")

water = float(input("Enter your water intake in litres\n"))
if water < 2:
    print("You need to drink more wate\nr")
elif water > 4:
    print("You are drinking too much water\n")
else:
    print("You are drinking well\n")

print("now lets count your calories \n")

cal= c.calculate_calories()
print(f"Your calorie intake is {cal} calories\n")


steps = int(input("Enter your steps count in last 24 hours\n"))

CB_STEPS = 0.415 * (height)* weight * 0.57 * steps / 1000
print(f"Your calories burnt by steps is {CB_STEPS} calories\n")

print("Enter your workout type \n")
def workout_type():
    WO_Type = int(input("enter your workout type(number) \n 0.no workout \n 1. cardio_moderate \n 2. cardio_intense \n 3. lifting_light \n 4. lifting_heavy \n 5. hiit \n 6. yoga \n 7. dance\n"))
    return WO_Type


WO_Type = workout_type()
WO_Dur= int(input("Enter your workout duration in minutes \n"))


def CB_WORKOUTperMin(WO_Type, weight):
    

    if WO_Type == 0:
        print("please consider working out")
        return 0.0

    
    elif WO_Type == 1:
        if weight <= 60:
            return 6.0
        elif weight <= 70:
            return 7.0
        else:
            return 8.0

    elif WO_Type == 2:
        if weight <= 60:
            return 10.0
        elif weight <= 70:
            return 11.7
        else:
            return 13.3

    elif WO_Type == 3:
        if  weight<= 60:
            return 3.5
        elif weight <= 70:
            return 4.1
        else:
            return 4.7

    elif WO_Type == 4:
        if weight <= 60:
            return 6.0
        elif weight <= 70:
            return 7.0
        else:
            return 8.0

    elif WO_Type == 5:
        if weight <= 60:
            return 11.0
        elif weight <= 70:
            return 13.0
        else:
            return 15.0

    elif WO_Type == 6:
        if weight <= 60:
            return 2.5
        elif weight <= 70:
            return 2.9
        else:
            return 3.3


    elif WO_Type == 7:
        if weight <= 60:
            return 6.0
        elif weight <= 70:
            return 7.0
        else:
            return 8.0

    else:
        print("enter valid workout type")  
        WO_Type=workout_type()
        CB_WORKOUTperMin(WO_Type, weight)

w = weight
perMin=CB_WORKOUTperMin(WO_Type, weight)
CB_WORKOUT= round(perMin * WO_Dur,2)
print(f"Your calories burnt by workout is {CB_WORKOUT} calories\n")

net_calories = round(cal - CB_STEPS - CB_WORKOUT,2)
print(f"Your net calories are {net_calories} calories\n")

if goal == 1:
    if net_calories < 0:
        print("You need to eat more calories\n")
    else:
        print("You are on the right track\n")
elif goal == 2:
    if net_calories > 0:
        print("You need to eat less calories\n")
    else:
        print("You are on the right track\n") 



db.save_fitness_data(
    user_id, gender, height, weight, BMI, goal, sleep, water,
    cal, steps, CB_STEPS, WO_Type, WO_Dur, CB_WORKOUT, net_calories
)


previous_entries = db.get_last_entries(user_id, 3)

if len(previous_entries) >= 2:
    print("\n--- Previous Entries for Comparison ---")
    for i, entry in enumerate(previous_entries[::-1], 1):
        print(f"\nEntry {i}:")
        print(f"  Weight: {entry[2]} kg")
        print(f"  BMI: {entry[3]:.2f}")
        print(f"  Sleep Hours: {entry[4]}")
        print(f"  Water Intake: {entry[5]} L")
        print(f"  Calorie Intake: {entry[6]}")
        print(f"  Calories Burnt (Steps): {entry[7]}")
        print(f"  Calories Burnt (Workout): {entry[8]}")
        print(f"  Net Calories: {entry[9]}")
else:
    print("Not enough past data to compare.")

if weight < previous_entries[-1][2]:
    print("You have lost weight since your last entry.\n")
elif weight > previous_entries[-1][2]:
    print("You have gained weight since your last entry.\n")
elif weight == previous_entries[-1][2]: 
    print("Your weight has remained the same since your last entry.\n")       

if BMI < previous_entries[-1][3]:
    print("Your BMI has decreased since your last entry.\n")  
elif BMI > previous_entries[-1][3]:
    print("Your BMI has increased since your last entry.\n")  
elif BMI == previous_entries[-1][3]:
    print("Your BMI has remained the same since your last entry.\n")


print("Thank you for using the fitness tracker! , hope to see you again \n")

print("Have a great day ahead!")