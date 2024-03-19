import math

firstName = "Rachel"  # add your first name
lastName = "Heintjes"  # add your last name
print("Name: " + firstName + " " + lastName)
print("CPS 3320 - Project 1")


# Define main function
def main():
    print("Welcome to my Graduate School Project")
    print("Menu")
    print("C1 - Pace University, NYC Campus")
    print("C2 - New Jersey Institute of Technology")
    print("C3 - Rowan University")
    print("Q - Quit")
    done = False
    while not done:
        choice = input("Choice: ")
        if choice == "Q":
            print("Quit!")
            done = True
        elif choice == "C1":
            college_1()
            done = True  # Prevent further choices after college_1() is executed
        elif choice == "C2":
            college_2()
            done = True  # Prevent further choices after college_2() is executed
        elif choice == "C3":
            college_3()
            done = True  # Prevent further choices after college_2() is executed
        else:
            print("Invalid Choice")

def college_1():
    res_meal_cost = 600  # Cost of the residential meal plan for College 1
    com_meal_cost = 300  # Cost of the commuter meal plan for College 1

    print("Welcome to Pace University Graduate School")
    print("Ranked in the top 9% of private US colleges that provide the best return on tuition investment, Pace University transforms the lives of its diverse students—academically, professionally, and socioeconomically. We are at the forefront of creating opportunity and that mission is expressed in our motto: Opportunitas.")

    while True:
        college_type = input("Is the college public or private? (PUBLIC/PRIVATE): ").upper()
        if college_type == "PUBLIC":
            print("Invalid choice. Only private colleges supported.")
            continue
        elif college_type == "PRIVATE":

            print("You are pursuing a M.S. in Computer Science.")
            print("You must complete 30 credits in order to earn your desired graduate degree!")

            # Calculate total cost for the fall semester
            print("\nFall Semester:")
            fall_credits = int(input("How many credits are you taking in the Fall? "))
            tuition_cost_fall = tuition(fall_credits)

            building, room, room_cost = on_campus_housing()
            if building == "Commuter":
                meal_plan_choice = input("Do you want a meal plan? (YES/NO): ").upper()
                com_meal_plan = meal_plan_choice == "YES"
                meal_cost = 300
            else:
                meal_cost =600

            # Print summary for the fall semester
            print("\nSummary for Fall Semester:")
            print("Fall Credits:", fall_credits)
            print("Status:", "Full-time" if fall_credits > 6 else "Part-time")  # Print status based on credits
            print("Tuition Cost for Fall Semester: $" + str(tuition_cost_fall))
            print("Housing Cost for Fall Semester (Building:", building, ", Room:", room, "): $" + str(room_cost))
            print("Meal Cost for Fall Semester: $" + str(meal_cost))
            print("Total Cost for Fall Semester: $" + str(tuition_cost_fall + room_cost + meal_cost))

            # Calculate total cost for the spring semester
            print("\nSpring Semester:")
            spring_credits = int(input("How many credits are you taking in the Spring? "))
            tuition_cost_spring = tuition(spring_credits)

            building, room, room_cost = on_campus_housing()
            if building == "Commuter":
                meal_plan_choice = input("Do you want a meal plan? (YES/NO): ").upper()
                com_meal_plan = meal_plan_choice == "YES"
                meal_cost = 300
            else:
                meal_cost =600

            total_cost_spring = tuition_cost_spring + room_cost + meal_cost

            # Print summary for the spring semester
            print("\nSummary for Spring Semester:")
            print("Spring Credits:", spring_credits)
            print("Status:", "Full-time" if spring_credits > 6 else "Part-time")  # Print status based on credits
            print("Tuition Cost for Spring Semester: $" + str(tuition_cost_spring))
            print("Housing Cost for Spring Semester (Building:", building, ", Room:", room, "): $" + str(room_cost))
            print("Meal Cost for Spring Semester: $" + str(meal_cost))
            print("Total Cost for Spring Semester: $" + str(total_cost_spring))

            # Calculate and print the total cost for the school year
            total_cost_year = tuition_cost_fall + room_cost + meal_cost + total_cost_spring
            print("\nTotal Cost for the School Year: $" + str(total_cost_year))

            tuition_per_credit = 1500

            total_credits_year = fall_credits + spring_credits

            # Calculate the number of years it will take to graduate
            total_credits_needed = 30  # Total credits needed to graduate
            years_to_graduate = total_credits_needed / total_credits_year

            print("Number of Years to Graduate: " + str(years_to_graduate))

            estimated_degree_cost = total_cost_year * years_to_graduate
            print("Estimated Degree Cost: $" + str(estimated_degree_cost))

            return

        else:
            print("Invalid college type.")


# Define Tuition Function
def tuition(credits):
    tuition_per_credit = 1490

    if credits <= 6:
        print("You are a part-time student.")
    else:
        print("You are a full-time student.")

    return credits * tuition_per_credit


def on_campus_housing():
    print("Are you a commuter or will you be staying on-campus?")
    housing_choice = input("Enter your choice (COMMUTER/ON-CAMPUS): ").upper()

    if housing_choice == "ON-CAMPUS":
        print("Here are your On-Campus housing options:")
        print("1. 182 Broadway")
        print("2. 55 John Street")
        print("3. 33 Beekman")
        choice = input("Enter which building you want to live in (1/2/3): ")

        if choice == "1":
            print("You have chosen 182 Broadway.")
            room_choice = input("Which room would you like to live in? (DOUBLE/TRIPLE/QUAD): ").upper()
            if room_choice == "DOUBLE":
                room_cost = 10100
                print("Cost of Double room: $10100 per semester")
            elif room_choice == "TRIPLE":
                room_cost = 9900
                print("Cost of Triple room: $9900 per semester")
            elif room_choice == "QUAD":
                room_cost = 9350
                print("Cost of Quad room: $9350 per semester")
            else:
                print("Invalid room choice.")
            return "182 Broadway", room_choice, room_cost
        elif choice == "2":
            print("You have chosen 55 John Street.")
            room_choice = input("Which room would you like to live in? (DOUBLE/TRIPLE/LOFTED TRIPLE): ").upper()
            if room_choice == "DOUBLE":
                room_cost = 10100
                print("Cost of Double room: $10100 per semester")
            elif room_choice == "TRIPLE":
                room_cost = 9900
                print("Cost of Triple room: $9900 per semester")
            elif room_choice == "LOFTED TRIPLE":
                room_cost = 9900
                print("Cost of Lofted Triple room: $9900 per semester")
            else:
                print("Invalid room choice.")
            return "55 John Street", room_choice, room_cost
        elif choice == "3":
            print("You have chosen 33 Beekman.")
            room_choice = input("Which room would you like to live in? (DOUBLE/LOFTED DOUBLE/TRIPLE/QUAD/SINGLE/LOFTED DOUBLE AS SINGLE): ").upper()
            if room_choice == "DOUBLE":
                room_cost = 10100
                print("Cost of Double room: $10100 per semester")
            elif room_choice == "LOFTED DOUBLE":
                room_cost = 10100
                print("Cost of Lofted Double room: $10100 per semester")
            elif room_choice == "TRIPLE":
                room_cost = 9900
                print("Cost of Triple room: $9900 per semester")
            elif room_choice == "QUAD":
                room_cost = 9350
                print("Cost of Quad room: $9350 per semester")
            elif room_choice == "SINGLE":
                room_cost = 11500
                print("Cost of Single room: $11500 per semester")
            elif room_choice == "LOFTED DOUBLE AS SINGLE":
                room_cost = 11500
                print("Cost of Lofted Double room as Single: $11500 per semester")
            else:
                print("Invalid room choice.")
            return "33 Beekman", room_choice, room_cost
        else:
            print("Invalid building choice.")
    elif housing_choice == "COMMUTER":
        print("You have chosen to live off-campus.")
        print("Assuming you live with your parents and commute from home, your cost of housing is $0.")
        return "Commuter", None, 0
    else:
        print("Invalid choice.")

# Define Meals Function
def meals(housing_choice, res_meal_cost, com_meal_cost, include_com_meal_plan=False):
    if housing_choice == "ON-CAMPUS":
        print("The standard plan for residential graduate students at Pace University includes $545 declining dining dollars, $55 Flex.")
        print("Meal Plan Cost: $" + str(res_meal_cost))  # Cost of the residential meal plan for College 1
        return res_meal_cost
    elif housing_choice == "COMMUTER":
        print("You have chosen to live off-campus.")
        print("Assuming you live with your parents and commute from home, your cost of housing is $0.")
        if include_com_meal_plan:
            print("The standard plan for all commuter students at Pace University features: $250 declining dining dollars, $50 Flex.")
            print("The meal plan cost for commuters is: $" + str(com_meal_cost))  # Cost of the commuter meal plan for College 1
            return com_meal_cost
        else:
            print("You are not required to have a meal plan.")
            return 0  # Cost for commuter students without a meal plan is $0
    else:
        print("Invalid housing choice.")


def college_2():
    print("Welcome to New Jersey Institute of Technology!")
    print("New Jersey Institute of Technology (NJIT) is a public research university in Newark, New Jersey, with a graduate-degree-granting satellite campus in Jersey City. Founded in 1881 with the support of local industrialists and inventors especially Edward Weston, NJIT opened as Newark Technical School (NTS) in 1885 with 88 students.")

    while True:
        college_type = input("Is the college public or private? (PRIVATE/PUBLIC): ").upper()
        if college_type == "PRIVATE":
            print("Invalid choice. This is a public college!")
            continue
        elif college_type == "PUBLIC":
            break
        else:
            print("Invalid choice. Please choose either PUBLIC or PRIVATE.")
            continue
    print("You are pursuing an M.S. in Computer Science.")
    print("You must complete 30 credits in order to earn your desired graduate degree!")


    fall_credits = int(input("How many credits are you taking in the fall? "))
    nj_resident = input("Do you live in New Jersey? (yes/no) ").lower()

    fall_tuition = tuition2(fall_credits, nj_resident)

    # Assign in_state_tuition_per_credit here
    in_state_tuition_per_credit = fall_tuition

    spring_credits = int(input("How many credits are you taking in the spring? "))
    nj_resident = input("Do you live in New Jersey? (yes/no) ").lower()
    spring_tuition = tuition2(spring_credits, nj_resident)

    # Call the housing function to get housing details
    housing_choice, room_choice, room_cost = housing2()

    # Call the meals function to get meal details
    meal_plan, meal_cost = meals2()

    # Calculate total cost for fall semester
    if meal_cost is None:
        meal_cost = 0  # Set meal_cost to 0 if meal_plan is None

    total_cost_fall_semester = fall_tuition + room_cost + meal_cost

    # Print summary for fall semester
    print("\nSummary for Fall Semester:")
    print("---------------------------")
    print("Fall Credits:", fall_credits)
    print("Status:", "Full-time" if fall_credits > 6 else "Part-time")  # Print status based on credits
    print("Tuition:")
    print("- Tuition cost: $", fall_tuition)
    print("\nHousing:")
    print("- Housing choice:", housing_choice)
    print("- Room choice:", room_choice)
    print("- Room cost: $", room_cost)
    print("\nMeals:")
    if meal_cost is not None:
        print("- Meal plan:", meal_plan)
        print("- Meal cost: $", meal_cost)
    else:
        print("- No meal plan chosen.")
    print("\nTotal Cost for Fall Semester: $", total_cost_fall_semester)


    # Call the housing function to get housing details for spring semester
    spring_housing_choice, spring_room_choice, spring_room_cost = housing2()

    # Call the meals function to get meal details for spring semester
    spring_meal_plan, spring_meal_cost = meals2()

    if spring_room_cost is not None and spring_meal_cost is not None:
        total_cost_spring_semester = spring_tuition + spring_room_cost + spring_meal_cost

    else:
        total_cost_spring_semester = 0  # or handle it according to your program's logic
        print("Error: Unable to calculate total cost for spring semester. Missing room cost or meal cost.")

    # Print summary for spring semester
    print("\nSummary for Spring Semester:")
    print("-----------------------------")
    print("Spring Credits:", spring_credits)
    print("Status:", "Full-time" if spring_credits > 6 else "Part-time")  # Print status based on credits
    print("Tuition:")
    print("- Tuition cost: $", spring_tuition)
    print("\nHousing:")
    print("- Housing choice:", spring_housing_choice)
    print("- Room choice:", spring_room_choice)
    print("- Room cost: $", spring_room_cost)
    print("\nMeals:")
    print("- Meal plan:", spring_meal_plan)
    print("- Meal cost: $", spring_meal_cost)
    print("\nTotal Cost for Spring Semester: $", total_cost_spring_semester)

    total_cost_year = total_cost_fall_semester + total_cost_spring_semester
    print("Academic Year Total: $", str(total_cost_year))

    total_credits_needed = 30

    total_credits_year = fall_credits + spring_credits

    years_to_graduate = total_credits_needed / total_credits_year

    print("Number of Years to Graduate: " + str(years_to_graduate))

    estimated_degree_cost = total_cost_year * years_to_graduate
    print("Estimated Degree Cost: $" + str(estimated_degree_cost))



def tuition2(credits, resident):

        if credits <= 6:
            print("You are a part-time student.")
        else:
            print("You are a full-time student.")

        if resident == "yes":
            if credits == 1:
                tuition = 1226
            elif credits == 1.5:
                tuition = 1839
            elif credits == 2:
                tuition = 2452
            elif credits == 3:
                tuition = 3678
            elif credits == 4:
                tuition = 4904
            elif credits == 5:
                tuition = 6130
            elif credits == 6:
                tuition = 7356
            elif credits == 7:
                tuition = 8582
            elif credits == 8:
                tuition = 9808
            elif credits == 9:
                tuition = 11034
            elif credits == 10:
                tuition = 12260
            elif credits == 11:
                tuition = 134986
            elif 12 <= credits <= 19:
                tuition = 11267
        else:
            if credits == 1:
                tuition = 1760
            elif credits == 1.5:
                tuition = 2640
            elif credits == 2:
                tuition = 3520
            elif credits == 3:
                tuition = 5280
            elif credits == 4:
                tuition = 7040
            elif credits == 5:
                tuition = 8800
            elif credits == 6:
                tuition = 10560
            elif credits == 7:
                tuition = 12320
            elif credits == 8:
                tuition = 14080
            elif credits == 9:
                tuition = 15840
            elif credits == 10:
                tuition = 17600
            elif credits == 11:
                tuition = 19360
            elif 12 <= credits <= 19:
                tuition = 16659

        print("Your tuition is: ", tuition)
        return tuition

def housing2():
    room_cost = 0

    print("Are you a commuter or will you be staying on-campus?")
    housing_choice = input("Enter your choice (COMMUTER/ON-CAMPUS): ").upper()

    if housing_choice == "COMMUTER":
        print("You chose to commute.")
        print("Assuming you live with your parents, and are commuting from home, your cost is $0")
        return None, None, 0

    if housing_choice == "ON-CAMPUS":
        print("Here are your On-Campus housing options:")
        print("1. Cypress Hall")
        print("2. Martinson Residence Hall- (HONORS)")
        print("3. Laurel Hall")
        print("4. Redwood Hall")
        print("5. Oak Hall")
        print("6. Greek Village")
        print("7. Maple Hall")
        choice = input("Enter which building you want to live in (1/2/3/4/5/6/7): ")
        if choice == "1":
            print("You have chosen Cypress Hall.")
            room_choice = input("Which room would you like to live in? (DOUBLE/DOUBLE PRIVATE BATH/SINGLE SHARED BATH/SINGLE PRIVATE BATH): ").upper()
            if room_choice == "DOUBLE":
                room_cost = 4830
                print("Cost of Double room: $4830 per semester")
            elif room_choice == "DOUBLE PRIVATE BATH":
                room_cost = 4950
                print("Cost of Double room with a private bathroom: $4950 per semester")
            elif room_choice == "SINGLE ROOM SHARED BATH":
                room_cost = 5650
                print("Cost of Single room with a shared bathroom: $5650 per semester")
            elif room_choice == "SINGLE ROOM PRIVATE BATH":
                room_cost = 6010
                print("Cost of Single room with a private bathroom: $6010 per semester")
            else:
                print("Invalid room choice.")
            return "Cypress Hall", room_choice, room_cost

        elif choice == "2":
            print("You have chosen Martinson Residence Hall (HONORS).")
            room_choice = input("Which room would you like to live in? (DOUBLE/DOUBLE PRIVATE BATH/SINGLE SHARED BATH/SINGLE PRIVATE BATH): ").upper()
            if room_choice == "DOUBLE":
                room_cost = 4960
                print("Cost of Double room: $4960 per semester")
            elif room_choice == "DOUBLE PRIVATE BATH":
                room_cost = 5090
                print("Cost of Double room with a private bathroom: $5090 per semester")
            elif room_choice == "SINGLE ROOM SHARED BATH":
                room_cost = 5800
                print("Cost of Single room with a shared bathroom: $5800 per semester")
            elif room_choice == "SINGLE ROOM PRIVATE BATH":
                room_cost = 6140
                print("Cost of Single room with a private bathroom: $6140 per semester")
            else:
                print("Invalid room choice.")
            return "Martinson Residence Hall (HONORS)", room_choice, room_cost

        elif choice == "3":
            print("You have chosen Laurel Hall.")
            room_choice = input("Which room would you like to live in? (DOUBLE/DOUBLE PRIVATE BATH/C SINGLE SHARED BATH/SINGLE SHARED BATH/SINGLE PRIVATE BATH): ").upper()
            if room_choice == "DOUBLE":
                room_cost = 4830
                print("Cost of Double room: $4830 per semester")
            elif room_choice == "DOUBLE PRIVATE BATH":
                room_cost = 4950
                print("Cost of Double room with a private bathroom: $4950 per semester")
            elif room_choice == "C SINGLE ROOM SHARED BATH":
                room_cost = 5540
                print("Cost of Single room with a shared bathroom: $5540 per semester")
            elif room_choice == "SINGLE ROOM SHARED BATH":
                room_cost = 5650
                print("Cost of Single room with a shared bathroom: $5650 per semester")
            elif room_choice == "SINGLE ROOM PRIVATE BATH":
                room_cost = 6010
                print("Cost of Single room with a private bathroom: $6010 per semester")
            else:
                print("Invalid room choice.")
            return "Martinson Residence Hall (HONORS)", room_choice, room_cost

        elif choice == "4":
            print("You have chosen Redwood Hall.")
            room_choice = input("Which room would you like to live in? (SINGLE/DOUBLE): ").upper()
            if room_choice == "SINGLE":
                room_cost = 5310
                print("Cost of Single room: $5310 per semester")
            elif room_choice == "DOUBLE":
                room_cost = 4950
                print("Cost of Double room: $5310 per semester")
            else:
                print("Invalid room choice.")
            return "Redwood Hall", room_choice, room_cost

        elif choice == "5":
            print("You have chosen Oak Hall.")
            room_choice = input("Which room would you like to live in? (SINGLE/DOUBLE): ").upper()
            if room_choice == "SINGLE":
                room_cost = 5650
                print("Cost of Single room: $5650 per semester")
            elif room_choice == "DOUBLE":
                room_cost = 4830
                print("Cost of Double room: $4830 per semester")
            else:
                print("Invalid room choice.")
            return "Oak Hall", room_choice, room_cost

        elif choice == "6":
            print("You have chosen Greek Village.")
            room_choice = input("Which room would you like to live in? (RENTED UNITS DOUBLE/OWNED UNITS DOUBLE): ").upper()
            if room_choice == "RENTED UNITS DOUBLE":
                room_cost = 4960
                print("Cost of Rented units double room: $4960 per semester")
            elif room_choice == "OWNED UNITS DOUBLE":
                room_cost = 4830
                print("Cost of Double room: $4830 per semester")
            else:
                print("Invalid room choice.")
            return "Greek Village", room_choice, room_cost

        elif choice == "7":
            print("You have chosen Maple Hall.")
            room_choice = input("Which room would you like to live in? (STUDIO APT PRIVATE/ 1BR 1BA APT DOUBLE/ 2BR 2BA APT DOUBLE/ 4BR 2BA APT PRIVATE): ").upper()
            if room_choice == "STUDIO APT PRIVATE":
                room_cost = 8660
                print("Cost of Studio apartment, private: $8660 per semester")
            elif room_choice == "1BR 1BA APT DOUBLE":
                room_cost = 6740
                print("Cost of 1 bedroom and 1 bathroom apartment double: $6740 per semester")
            elif room_choice == "2BR 2BA APT DOUBLE":
                room_cost = 5930
                print("Cost of 2 bedroom and 2 bathroom apartment double: $5930 per semester")
            elif room_choice == "4BR 2BA APT PRIVATE":
                room_cost = 7190
                print("Cost of 4 bedroom and 2 bathroom apartment, private: $7190 per semester")
            else:
                print("Invalid room choice.")
            return "Maple Hall", room_choice, room_cost
        else:
            print("Invalid building choice.")

    else:
        print("Invalid choice.")


def meals2():
    print("Will you be living on-campus?")
    on_campus = input("Enter your choice (YES/NO): ").upper()

    if on_campus == "YES":
        print("Here are your meal plan options for on-campus residents:")
        print("1. A Plan: Continuous Unlimited Dining, 10 Guest entries; and $0 Tech Bucks.")
        print("2. B Plan: Continuous Unlimited Dining, 10 Guest entries; and $100 Tech Bucks.")
        print("3. C Plan: Continuous Unlimited Dining, 10 Guest entries; and and $200 Tech Bucks.")
        print("4. D Plan: Continuous Unlimited Dining, 10 Guest entries; and and $400 Tech Bucks.")
        print("5. E Plan: Continuous Unlimited Dining, 10 Guest entries; and $600 Tech Bucks.")
        print("6. F Plan: 80 Anytime Meals Per Semester, 10 guest entries; and $400 Tech Bucks.")
        print("7. G Plan: $1,414 Tech Bucks.")
        print("8. H Plan: 80 Anytime Meals Per Semester, 10 guest entries; and $0 Tech Bucks.")
        plan_choice = input("Enter the number corresponding to your desired meal plan (1/2/3/4/5/6/7/8): ")

        meal_cost = 0  # Placeholder for meal cost
        if plan_choice == "1":
            meal_plan = "A Plan"
            meal_cost = 2223
        elif plan_choice == "2":
            meal_plan = "B Plan"
            meal_cost = 2323
        elif plan_choice == "3":
            meal_plan = "C Plan"
            meal_cost = 2423
        elif plan_choice == "4":
            meal_plan = "D Plan"
            meal_cost = 2623
        elif plan_choice == "5":
            meal_plan = "E Plan"
            meal_cost = 2823
        elif plan_choice == "6":
            meal_plan = "F Plan"
            meal_cost = 1517
        elif plan_choice == "7":
            meal_plan = "G Plan"
            meal_cost = 1414
        elif plan_choice == "8":
            meal_plan = "H Plan"
            meal_cost = 1117
        else:
            print("Invalid choice.")
            return None, None  # Return None, None for invalid choice

        return meal_plan, meal_cost

    elif on_campus == "NO":
        print("Do you want a meal plan?")
        com_meal_plan = input("Enter your choice (YES/NO): ").upper()

        if com_meal_plan == "YES":
            print("Here are your meal plan options for off-campus residents:")
            print("1. A Plan: Continuous Unlimited Dining, 10 Guest entries; and $0 Tech Bucks.")
            print("2. B Plan: Continuous Unlimited Dining, 10 Guest entries; and $100 Tech Bucks.")
            print("3. C Plan: Continuous Unlimited Dining, 10 Guest entries; and and $200 Tech Bucks.")
            print("4. D Plan: Continuous Unlimited Dining, 10 Guest entries; and and $400 Tech Bucks.")
            print("5. E Plan: Continuous Unlimited Dining, 10 Guest entries; and $600 Tech Bucks.")
            print("6. F Plan: 80 Anytime Meals Per Semester, 10 guest entries; and $400 Tech Bucks.")
            print("7. G Plan: $1,414 Tech Bucks.")
            print("8. H Plan: 80 Anytime Meals Per Semester, 10 guest entries; and $0 Tech Bucks.")
            print("9. J Plan: 5 meals per week, Breakfast and/or Lunch entry.")
            plan_choice = input("Enter the number corresponding to your desired meal plan (1/2/3/4/5/6/7/8/9): ")

            meal_cost = 0  # Placeholder for meal cost
            if plan_choice == "1":
                meal_plan = "A Plan"
                meal_cost = 2223
            elif plan_choice == "2":
                meal_plan = "B Plan"
                meal_cost = 2323
            elif plan_choice == "3":
                meal_plan = "C Plan"
                meal_cost = 2423
            elif plan_choice == "4":
                meal_plan = "D Plan"
                meal_cost = 2623
            elif plan_choice == "5":
                meal_plan = "E Plan"
                meal_cost = 2823
            elif plan_choice == "6":
                meal_plan = "F Plan"
                meal_cost = 1517
            elif plan_choice == "7":
                meal_plan = "G Plan"
                meal_cost = 1414
            elif plan_choice == "8":
                meal_plan = "H Plan"
                meal_cost = 1117
            elif plan_choice == "9":
                meal_plan = "J Plan"
                meal_cost = 873
            else:
                print("Invalid choice.")
                return None, None  # Return None, None for invalid choice

            return meal_plan, meal_cost
        else:
            print("You have chosen not to have a meal plan.")
            return None, None  # Return None, None if no meal plan chosen

def college_3():
    meal_cost = 0
    fall_tuition = 0
    spring_tuition = 0

    print("Welcome to Rowan University!")
    print("Rowan University will become a new model for higher education by being inclusive, agile, and responsive, offering diverse scholarly and creative educational experiences, pathways, environments, and services to meet the needs of all students; maintaining agility by strategically delivering organizational capacity across the institution; and responding to emerging demands and opportunities regionally and nationally.")

    while True:
        college_type = input("Is the college public or private? (PRIVATE/PUBLIC): ").upper()
        if college_type == "PRIVATE":
            print("Invalid choice. This is a public college!")
            continue
        elif college_type == "PUBLIC":
            break
        else:
            print("Invalid choice. Please choose either PUBLIC or PRIVATE.")
            continue

    print("You are pursuing an M.S. in Computer Science.")
    print("You must complete 30 credits in order to earn your desired graduate degree!")

    # Semester Information
    fall_credits = int(input("How many credits are you taking in the Fall? "))
    spring_credits = int(input("How many credits are you taking in the Spring? "))

    # Tuition Calculation
    fall_tuition = tuition(fall_credits)
    spring_tuition = tuition(spring_credits)

    print("Fall Semester Tuition:", fall_tuition)
    print("Spring Semester Tuition:", spring_tuition)

    # Housing Information
    fall_room_cost, spring_room_cost = housing()

# Meal Information for Fall Semester
    print("For the Fall Semester:")
    fall_meal_plan, fall_meal_cost = meals()
    if fall_meal_cost is not None:
        meal_cost += fall_meal_cost

# Total costs calculation for Fall Semester
    total_cost_fall = fall_tuition + fall_room_cost + meal_cost if fall_meal_cost is not None else fall_tuition + fall_room_cost

# Meal Information for Spring Semester
    print("\nFor the Spring Semester:")
    spring_meal_plan, spring_meal_cost = meals()
    if spring_meal_cost is not None:
        meal_cost = 0  # Reset meal_cost for the Spring Semester
        meal_cost += spring_meal_cost

# Total costs calculation for Spring Semester
    total_cost_spring = spring_tuition + spring_room_cost + meal_cost if spring_meal_cost is not None else spring_tuition + spring_room_cost

 # Print fall semester summary
    print("\nFall Semester Summary:")
    print("Fall Credits:", fall_credits)
    print("Status:", "Full-time" if fall_credits > 6 else "Part-time")  # Print status based on credits
    print("Tuition Cost:", fall_tuition)
    print("Housing Cost:", fall_room_cost)
    print("Meal Cost:", fall_meal_cost if fall_meal_cost is not None else 0)
    print("Total Cost for Fall Semester:", total_cost_fall)
    # Print spring semester summary
    print("\nSpring Semester Summary:")
    print("Spring Credits:", spring_credits)
    print("Status:", "Full-time" if spring_credits > 6 else "Part-time")  # Print status based on credits
    print("Tuition Cost:", spring_tuition)
    print("Housing Cost:", spring_room_cost)
    print("Meal Cost:", spring_meal_cost if spring_meal_cost is not None else 0)
    print("Total Cost for Spring Semester:", total_cost_spring)

    total_cost_year = total_cost_fall + total_cost_spring
    print("Total cost for the academic school year:", total_cost_year)

    total_credits_needed = 30

    total_credits_year = fall_credits + spring_credits

    years_to_graduate = total_credits_needed / total_credits_year

    print("Number of Years to Graduate: " + str(years_to_graduate))

    estimated_degree_cost = total_cost_year * years_to_graduate
    print("Estimated Degree Cost: $" + str(estimated_degree_cost))



def tuition(credits):
    tuition_per_credit = 980.30

    if credits <= 6:
        print("You are a part-time student.")
    else:
        print("You are a full-time student.")
        tuition_per_credit = 980.30

    return credits * tuition_per_credit

def housing():
    fall_room_cost = 0  # Default value for fall room cost
    spring_room_cost = 0  # Default value for spring room cost

    housing_choice = input("Will you be staying on campus or commuting for fall? (ON CAMPUS/COMMUTING): ").upper()

    if housing_choice == "ON CAMPUS":
        print("Here are your on-campus housing options for fall:")
        print("1. Traditional Residence Halls")
        print("2. Holly Pointe Commons")
        print("3. Edgewood Park Apts")
        print("4. Rowan Boulevard")
        print("5. Townhouse")
        print("6. Whitney Center")
        choice = input("Enter which building you want to live in (1/2/3/4/5/6): ")

        if choice == "1":
            print("You have chosen the Traditional Residence Hall.")
            room_choice = input("Which room would you like to live in? (DOUBLE/SINGLE): ").upper()
            if room_choice == "DOUBLE":
                fall_room_cost = 4565
                print("Cost of Double room: $4565 per semester")
            elif room_choice == "SINGLE":
                fall_room_cost = 5444
                print("Cost of Single room: $5444 per semester")
            else:
                print("Invalid room choice.")

        elif choice == "2":
            print("You have chosen the Holly Pointe Commons.")
            room_choice = input("Which room would you like to live in? (DOUBLE/SINGLE): ").upper()
            if room_choice == "DOUBLE":
                fall_room_cost = 5450
                print("Cost of Double room: $5450 per semester")
            elif room_choice == "SINGLE":
                fall_room_cost = 5838
                print("Cost of Single room: $5838 per semester")
            else:
                print("Invalid room choice.")

        elif choice == "3":
            print("You have chosen Edgewood Park Apartment.")
            fall_room_cost = 4874
            print("This is a double occupancy bedroom.")

        elif choice == "4":
            print("You have chosen Rowan Boulevard.")
            fall_room_cost = 6349
            print("This is a single occupancy bedroom.")

        elif choice == "5":
            print("You have chosen Townhouses.")
            fall_room_cost = 6349
            print("This is a single occupancy bedroom.")

        elif choice == "6":
            print("You have chosen Whitney Center.")
            fall_room_cost = 6349
            print("This is a single occupancy bedroom.")

    elif housing_choice == "COMMUTING":
        print("You chose to commute for fall.")
        print("Assuming you live with your parents, and are commuting from home, your cost is $0")
    else:
        print("Invalid choice. Please choose between ON CAMPUS and COMMUTING.")

    # Prompt for spring housing choices
    spring_housing_choice = input("Will you be staying on campus or commuting for the Spring? (ON CAMPUS/COMMUTING): ").upper()

    if spring_housing_choice == "ON CAMPUS":
        print("Here are your on-campus housing options for the Spring:")
        print("1. Traditional Residence Halls")
        print("2. Holly Pointe Commons")
        print("3. Edgewood Park Apts")
        print("4. Rowan Boulevard")
        print("5. Townhouse")
        print("6. Whitney Center")
        choice = input("Enter which building you want to live in (1/2/3/4/5/6): ")
        if choice == "1":
            print("You have chosen the Traditional Residence Hall for the Spring.")
            room_choice = input("Which room would you like to live in? (DOUBLE/SINGLE): ").upper()
            if room_choice == "DOUBLE":
                spring_room_cost = 4565
                print("Cost of Double room: $4565 per semester")
            elif room_choice == "SINGLE":
                spring_room_cost = 5444
                print("Cost of Single room: $5444 per semester")
            else:
                print("Invalid room choice.")
        elif choice == "2":
            print("You have chosen the Holly Pointe Commons.")
            room_choice = input("Which room would you like to live in? (DOUBLE/SINGLE): ").upper()
            if room_choice == "DOUBLE":
                spring_room_cost = 5450
                print("Cost of Double room: $5450 per semester")
            elif room_choice == "SINGLE":
                spring_room_cost = 5838
                print("Cost of Single room: $5838 per semester")
            else:
                print("Invalid room choice.")

        elif choice == "3":
            print("You have chosen Edgewood Park Apartment.")
            spring_room_cost = 4874
            print("This is a double occupancy bedroom.")

        elif choice == "4":
            print("You have chosen Rowan Boulevard.")
            spring_room_cost = 6349
            print("This is a single occupancy bedroom.")

        elif choice == "5":
            print("You have chosen Townhouses.")
            spring_room_cost = 6349
            print("This is a single occupancy bedroom.")

        elif choice == "6":
            print("You have chosen Whitney Center.")
            spring_room_cost = 6349
            print("This is a single occupancy bedroom.")

    elif spring_housing_choice == "COMMUTING":
        print("You chose to commute for the Spring.")
        print("Assuming you live with your parents, and are commuting from home, your cost is $0")
    else:
        print("Invalid choice. Please choose between ON CAMPUS and COMMUTING.")

    return fall_room_cost, spring_room_cost


def meals():
    # Fall semester
    print("To determine a meal plan, will you be living on-campus for fall semester?")
    on_campus_fall = input("Enter your choice (YES/NO): ").upper()

    if on_campus_fall == "YES":
        print("Here are your meal plan options for on-campus residents for fall semester:")
        print("1. All Access Plan w/ $100 Dining Dollars & 100 Rowan Bucks: In this plan, a student can receive 42 meal swipes per week.")
        print("2. 14 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks: In this plan, a student gets 14 meals per week that can be used at any on-campus dining facility that offers a meal equivalency.")
        print("3. 10 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks: In this plan, a student gets 10 meals per week that can be used at any on-campus dining facility that offers a meal equivalency.")
        print("4. 7 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks: In this plan, a student gets 7 meals per week that can be used at any on-campus dining facility that offers a meal equivalency.")

        plan_choice = input("Enter the number corresponding to your desired meal plan (1/2/3/4): ")

        meal_cost = 0  # Placeholder for meal cost
        if plan_choice == "1":
            meal_plan = "All-Access Plan w/ $100 Dining Dollars & $100 Rowan Bucks"
            meal_cost = 2539
        elif plan_choice == "2":
            meal_plan = "14 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks"
            meal_cost = 2372
        elif plan_choice == "3":
            meal_plan = "10 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks"
            meal_cost = 2107
        elif plan_choice == "4":
            meal_plan = "7 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks"
            meal_cost = 1673
        else:
            print("Invalid choice.")
            return None, None  # Return None, None for invalid choice

        return meal_plan, meal_cost

    else:
        print("Do you want a meal plan for fall semester?")
        com_meal_plan_fall = input("Enter your choice (YES/NO): ").upper()

        if com_meal_plan_fall == "YES":
            print("Here are your meal plan options for commuters and non-residence halls for fall semester:")
            print("1. 60 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks: In this meal plan, students will receive 50 regular meal swipes that can be used at any on-campus dining facility that offers a meal equivalency. The remaining 10 meal swipes are called On / Off-campus meals.")
            print("2. 30 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks: In this meal plan, students will receive 25 regular meal swipes that can be used at any on-campus dining facility that offers a meal equivalency. The remaining 5 meal swipes are called On / Off-campus meals where students can swipe their Rowan Cards at any on-campus dining location")
            plan_choice = input("Enter the number corresponding to your desired meal plan (1/2): ")

            meal_cost = 0  # Placeholder for meal cost
            if plan_choice == "1":
                meal_plan = "60 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks"
                meal_cost = 811
            elif plan_choice == "2":
                meal_plan = "30 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks"
                meal_cost = 493
            else:
                print("Invalid choice.")
                return None, None  # Return None, None for invalid choice
        else:
            print("You have chosen not to have a meal plan for fall semester.")


    # Spring semester
    print("To determine a meal plan, will you be living on-campus for spring semester?")
    on_campus_spring = input("Enter your choice (YES/NO): ").upper()

    if on_campus_spring == "YES":
        print("Here are your meal plan options for on-campus residents for spring semester:")
        print("1. All Access Plan w/ $100 Dining Dollars & 100 Rowan Bucks: In this plan, a student can receive 42 meal swipes per week.")
        print("2. 14 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks:In this plan, a student gets 14 meals per week that can be used at any on-campus dining facility that offers a meal equivalency.")
        print("3. 10 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks: In this plan, a student gets 10 meals per week that can be used at any on-campus dining facility that offers a meal equivalency.")
        print("4. 7 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks: In this plan, a student gets 7 meals per week that can be used at any on-campus dining facility that offers a meal equivalency.")

        plan_choice = input("Enter the number corresponding to your desired meal plan (1/2/3/4): ")

        meal_cost = 0  # Placeholder for meal cost
        # Determine the cost for the selected meal plan
        if plan_choice == "1":
            meal_plan = "All-Access Plan w/ $100 Dining Dollars & $100 Rowan Bucks"
            meal_cost = 2539
        elif plan_choice == "2":
            meal_plan = "14 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks"
            meal_cost = 2372
        elif plan_choice == "3":
            meal_plan = "10 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks"
            meal_cost = 2107
        elif plan_choice == "4":
            meal_plan = "7 Meal Plan w/ $100 Dining Dollars & $200 Rowan Bucks"
            meal_cost = 1673
        else:
            print("Invalid choice.")
            return None, None  # Return None, None for invalid choice

        return meal_plan, meal_cost

    else:
        print("Do you want a meal plan for spring semester?")
        com_meal_plan_spring = input("Enter your choice (YES/NO): ").upper()

        if com_meal_plan_spring == "YES":
            print("Here are your meal plan options for commuters and non-residence halls for spring semester:")
            print("1. 60 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks: In this meal plan, students will receive 50 regular meal swipes that can be used at any on-campus dining facility that offers a meal equivalency. The remaining 10 meal swipes are called On / Off-campus meals.")
            print("2. 30 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks: In this meal plan, students will receive 25 regular meal swipes that can be used at any on-campus dining facility that offers a meal equivalency. The remaining 5 meal swipes are called On / Off-campus meals where students can swipe their Rowan Cards at any on-campus dining location")
            plan_choice = input("Enter the number corresponding to your desired meal plan (1/2): ")

            meal_cost = 0  # Placeholder for meal cost
            # Determine the cost for the selected meal plan
            if plan_choice == "1":
                meal_plan = "60 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks"
                meal_cost = 811
            elif plan_choice == "2":
                meal_plan = "30 Block plan w/ $75 Dining Dollars & $100 Rowan Bucks"
                meal_cost = 493
            else:
                print("Invalid choice.")
                return None, None  # Return None, None for invalid choice

            return meal_plan, meal_cost

        else:
            print("You have chosen not to have a meal plan for spring semester.")
            return None, None  # Return None, None if no meal plan chosen for spring semester

main()
