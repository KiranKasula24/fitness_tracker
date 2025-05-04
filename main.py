gender = input("enter your gender").strip().lower(
    
)
height = int(input("enter your height")).strip()
weight = int(input("enter your weight")).strip()

BMI= weight/height

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

