import calories as c
import tracker as t


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

    else:
        print("Invalid option. try again.")
        login_or_signup()

    return old_user

old_user = login_or_signup()



if old_user == 0:
    print("Welcome to your personal fitness tracker!\n")
    print("lets start tracking your habits and make them better\n")
    print("Please enter the required data to help understand your physical health:\n")
elif old_user == 1:
    print("Welcome back to your personal fitness tracker!\n")
    print("lets continue tracking your habits and make them even better\n")  

gender = input(" enter your gender \n").strip().lower()
height = int(input(" enter your height in cm \n"))
weight = int(input(" enter your weight in kgs65\n"))

BMI= weight/height

print(f"Your BMI is {BMI}\n")

if (BMI>18.5 and BMI<25):
    print("you have a healthy BMI")
elif (BMI<18.5):
    print("you are under weight")
elif (BMI>25 and BMI<30 ):
    print("you are overweight")
elif (BMI>30):
    print("you are obese")
else:
    print("enter valid height and weight")

print(" lets start tracking your habits and make them better\n")

sleep = int(input("Enter your sleep hours"))
# i need to make something which could help the user track his prevvious sleep hours and then compare it 
if sleep < 6:
    print("You need to sleep more")
elif sleep > 8:
    print("You are sleeping too much")
else:
    print("You are sleeping well")

water = int(input("Enter your water intake in litres"))

print("now lets count your calories \n")

cal= c.calculate_calories()
print(f"Your calorie intake is {cal} calories\n")


#steps = int(input("Enter your steps count in last 24 hours"))


