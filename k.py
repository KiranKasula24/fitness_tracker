import random

list = [0] * 10000

i = 0

while True:
    print("Welcome to your personal fitness tracker!\n")

    opt = int(input('''Enter
                    (1) if it is your First time
                    (2) to Input data
                    (3) to Exit
                    \n'''))

    if(opt == 1):
        r1 = random.randint(0, 10000)

        list[i] = r1

        flag = 0

        for j in range(0, i):
             if(list[j] == r1):
                flag = 1
                break
             
        if(flag == 1):
             continue

        id = r1

        i = i + 1

        file = open(f"{id}.txt", "w+")
        file.close

        print("Welcome to your personal fitness tracker!\n")

        print(f"Your User-ID is {id}\n")

        print("Please enter the required personal data to help asses your physical health:\n")
    
        h = float(input("Enter your height(feet):\n"))
        w = float(input("Enter your weight(kgs):\n"))

        h = h / 3.281

        bmi = w / (h * h)#int is an option

        file = open(f"{id}.txt", "w+")

        file.write(f"{bmi}")

        file.close()

        print(f"Your BMI is {bmi}\n")

        if(bmi < 18.5):
            print("As per your BMI, you are underweight\n")
            print("You belong to 8.5% of the world\n")
            print("Don't worry, you can correct yourself better by following these excercises and diet\n")

            print('''Exercises:
                    Strength training
                    Yoga
                    Limit cardio''')
        
            print('''Diet:
                    High-calorie, nutrient-dense foods
                    Lean proteins
                    Healthy fats
                    Frequent meals/snacks''')
        elif((bmi >= 18.5) and (bmi <= 25.9)):
            print("As per your BMI, you are normal\n")
            print("You belong to 36% of the world\n")
            print("You're doing great! You can remain healthy by following these excercises and diet\n ")

            print('''Exercises:
                    Balanced routine
                    Yoga
                    Active lifestyle''')
        
            print('''Diet:
                    Balanced plate
                    Moderate healthy fats
                    Hydration
                    Limit sugars''')
        elif((bmi >= 25.9) and (bmi <= 30)):
            print("As per your BMI, you are slightly overweight\n")
            print("You belong to 39% of the world\n")
            print("No worries, you can improve by following these excercises and diet\n ")

            print('''Exercises:
                    Moderate cardio
                    Strength training
                    Low-impact workouts''')
        
            print('''Diet:
                    Calorie deficit
                    High fiber
                    Lean proteins
                    Limit sugars''')
        elif(bmi >= 30):
            print("As per your BMI, you are slightly obese\n")
            print("You belong to 17% of the world\n")
            print("No worries, you can improve by following these excercises and diet\n ")

            print('''Exercises:
                    Walking
                    Progress to cardio
                    Strength training''')
        
            print( '''Diet:
                    Calorie-controlled plan
                    High fiber
                    Meal prep''')
            
        print('''Enter 
                ->BMI goal:
                ->Steps goal:''') 
        
        bmi_g = float(input(""))
        step_g = float(input(""))
    elif(opt == 2):
        print("Welcom back user!\n")
        print("Please enter required details:\n")
    
        print('''Enter 
                ->Steps:
                ->min and max Heart rate:''')
    
        s = int(input(""))
        min_h = int(input(""))
        max_h = int(input(""))

        dist = s * 0.00074
        avg_h = (min_h + max_h) / 2
        cal = s * 0.04

        print("Great going!")
        print(f'''You have travelled: {dist} km
You're avg Heart rate is: {avg_h} bpm
You have also burned: {cal} calories''')
    
        print('''Please Enter your
                ->Weight
                ->Diet and qnty of that dish''')
    
        w = float(input(""))    

        diet = {
    "Idli": 58,
    "Dosa": 168,
    "Chapati": 104,
    "Rice": 206,
    "Dal": 198,
    "Boiled Egg": 78,
    "Fried Egg": 90,
    "Poha": 250,
    "Upma": 220,
    "Pongal": 150,
    "Paratha": 260,
    "Paneer": 265,
    "Chicken Curry": 250,
    "Fish Curry": 180,
    "Roti": 85,
    "Vegetable Pulao": 250,
    "Curd": 60,
    "Buttermilk": 35,
    "Milk": 103,
    "Banana": 89,
    "Apple": 52,
    "Mango": 150,
    "Papaya": 43,
    "Orange": 47,
    "Grapes": 69,
    "Chickpeas boiled": 269,
    "Rajma": 240,
    "Chole": 280,
    "Kadhi": 130,
    "Bhindi Fry": 120,
    "Aloo Sabzi": 150,
    "Palak Paneer": 270,
    "Baingan Bharta": 130,
    "Sambar": 150,
    "Rasam": 60,
    "Thepla": 120,
    "Khakhra": 45,
    "Pav Bhaji": 400,
    "Vada Pav": 290,
    "Misal Pav": 300,
    "Veg Biryani": 290,
    "Chicken Biryani": 360,
    "Kheer": 240,
    "Halwa": 300,
    "Gulab Jamun": 150,
    "Ladoo": 180,
    "Jalebi": 150,
    "Pakora": 75,
    "Samosa": 130,
    "Bread": 66,
    "Butter": 45,
    "Ghee": 45,
    "Oil": 40,
    "Maggi": 360,
    "Pasta": 220,
    "Pizza": 285,
    "Burger veg": 295,
    "Burger chicken": 350,
    "French Fries": 312,
    "Corn Flakes": 120,
    "Oats": 150,
    "Puffed Rice": 54,
    "Khichdi": 200,
    "Sprouts": 100,
    "Noodles": 210,
    "Sev": 500,
    "Namkeen": 550,
    "Paneer Tikka": 320,
    "Tandoori Chicken": 265,
    "Mutton Curry": 340,
    "Egg Curry": 220,
    "Chana Masala": 230,
    "Vegetable Curry": 160,
    "Bhatura": 300,
    "Puri": 101,
    "Kachori": 190,
    "Aloo Tikki": 160,
    "Paneer Butter Masala": 350,
    "Malai Kofta": 380,
    "Rajma Chawal": 400,
    "Chole Bhature": 450,
    "Aloo Paratha": 290,
    "Plain Paratha": 260,
    "Masala Dosa": 387,
    "Rava Dosa": 160,
    "Spring Roll": 120,
    "Hakka Noodles": 280,
    "Manchurian": 300,
    "Bonda": 120,
    "Idiyappam": 80,
    "Neer Dosa": 90,
    "Medu Vada": 97,
    "Coconut Chutney": 55,
    "Tomato Chutney": 35,
    "Peanut Chutney": 80,
    "Chikki": 130,
    "Sabudana Khichdi": 350,
    "Modak": 180,
    "Kesari Bath": 250,
    "Lassi": 180,
    "Sugar": 16,
    "Honey": 21,
    "Tea": 90,
    "Coffee": 85
        }

        d = input("")
        qnty = int(input(""))

        bmi_2 = w / (h * h)

        diet[d] = int(diet[d])

        cal_2 = diet[d] * qnty

        cal_diff = cal - cal_2

        if(cal_diff > 0):
            print("Awesome! You're in a calorie defecit\n")
        else:
            print("You might want to reduce your calorie intake...\n")

        #Goals
        print("You've done a great job on your goals\n")

        print(f"You're BMI has gone from {bmi}->{bmi_2}\n")

        bmi_diff = bmi_2 - bmi_g

        if(bmi > bmi_g):
                if(bmi_2 <= bmi_g):
                        print("And you've also achieved you BMI goal!!\n")
                else:
                        print(f"You're {bmi_diff} away from your goal\n")
        elif(bmi < bmi_g):
                if(bmi_2 >= bmi_g):
                     print("BMI goal achieved!!\n")
                else:
                     print(f"You're {bmi_diff * (-1)} away from your goal\n")
        elif(bmi == bmi_g):
             print("BMI goal achieved!!\n")

        step_diff = step_g - s
        
        if(s >= step_g):
             print("Steps Goal Reached!!\n")
        else:
             print(f"You we're {step_diff} steps away from reaching you're step goal\n")

    elif(opt == 3):
        print("Bye! See you soon...\n")
        break
    else:
        print ("Invalid Input\n")