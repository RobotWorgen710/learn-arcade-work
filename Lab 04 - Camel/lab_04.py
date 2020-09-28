# Lab 4 Stealing a car

import random


def main():
    """Printing Backstory and Instructions"""
    print("""
    Welcome to Minor Theft Auto
    You just stole a car from a dealership but the manager called the police. 
    They are hot on your trail and you must make it to a warehouse a few states over where you can modify
    the car so they aren't looking for it and to escape the police.
    """)
    done = False

    total_player_miles_traveled = 0
    total_police_miles_traveled = -100
    engine_heat = 0
    gas_stops = 3
    gas_remaining = 17

    while not done:

        """Options for the player"""
        print("""
        A. Fill up with gas.
        B. Drive at the speed limit.
        C. Drive at top speed.
        D. Stop for the night.
        E. Status Check.
        Q. Quit.
        """)
        choice = input("What is your choice? ")
        choice = choice.lower()
        oasis = random.randint(1, 20)

        if choice == "a":
            """Stop for gas"""
            if gas_stops >= 1:
                gas_remaining = 17
                gas_stops -= 1
                total_police_miles_traveled += random.randint(10, 25)
                print("You refilled the gas.")
                if gas_stops > 1:
                    print("You can stop for gas " + str(gas_stops) + " more times.")

                elif gas_stops == 1:
                    print("You can stop for gas " + str(gas_stops) + " more time.")
                else:
                    print("You don't have any more money for gas.")
            else:
                print("You don't have any more money for gas.")

        elif choice == "b":
            """Drive at the speed limit"""
            player_day_miles = random.randint(40, 60)
            total_player_miles_traveled += player_day_miles
            police_day_miles = random.randint(45, 60)
            total_police_miles_traveled += police_day_miles
            engine_heat += 1
            gas_remaining -= random.randint(1, 2)
            print("You traveled " + str(player_day_miles) + " miles.")

        elif choice == "c":
            """Drive full throttle"""
            player_day_miles = random.randint(65, 80)
            total_player_miles_traveled += player_day_miles
            police_day_miles = random.randint(45, 60)
            total_police_miles_traveled += police_day_miles
            gas_remaining -= random.randint(2, 4)
            engine_heat += random.randint(2, 3)
            print("You traveled " + str(player_day_miles) + " miles.")

        elif choice == "d":
            """Rest for the night"""
            night_miles = random.randint(65, 80)
            engine_heat = 0
            print("The car has cooled down.")
            print("The police covered " + str(night_miles) + " miles while you were stopped!")
            total_police_miles_traveled += night_miles

        elif choice == "e":
            """Status Check"""
            print("Miles traveled: " + str(total_player_miles_traveled))
            print("Gas stops remaining: " + str(gas_stops))
            print("The police are " + str(total_player_miles_traveled - total_police_miles_traveled),
                  " miles behind you!")
            print("You have " + str(1000 - total_player_miles_traveled) + " left to travel")

        elif choice == "q":
            """Quiting the game"""
            print("You quitter")
            print("Game Over")
            done = True

        if engine_heat > 10 and total_player_miles_traveled < 1000:
            """Engine over heating"""
            print("You blew up the engine! The police found you be the side of the road.")
            print("You were " + str(1000 - total_player_miles_traveled) + " miles away from the warehouse.")
            print("Game Over")
            done = True

        if 10 > engine_heat >= 7 and total_player_miles_traveled < 1000:
            """Showing a warning that the engine is getting hot"""
            print("The engine is getting hot.")

        if 5 >= gas_remaining >= 1 and total_player_miles_traveled < 1000 and not done:
            "Warning that the gas is getting low"
            print("You car is low on gas.")

        if gas_remaining <= 0 and total_player_miles_traveled < 1000:
            """Car running out of gas"""
            print("You ran out of gas and the police caught you.")
            print("You were " + str(1000 - total_player_miles_traveled) + " miles away from the warehouse.")
            print("Game Over")
            done = True

        if total_police_miles_traveled >= total_player_miles_traveled:
            """Player getting caught by the police"""
            print("The police caught up with you and took you to jail")
            print("You were " + str(1000 - total_player_miles_traveled) + " miles away from the warehouse.")
            print("Game Over")
            done = True

        if total_player_miles_traveled - total_police_miles_traveled and not done < 50:
            """Warning that the police are close behind"""
            print("The police are close behind you.")

        if total_player_miles_traveled >= 1000:
            """How to win the game"""
            print("You made it back to the warehouse where you can modify the car.")
            print("Congratulations you win!")
            print("The police were " + str(total_player_miles_traveled - total_police_miles_traveled) +
                  " miles behind you!")
            done = True

        if oasis == 13:
            """Random chance car show"""
            engine_heat = 0
            gas_remaining = 17
            print("You found a car show where people help you escape the police")
            print("Someone gave you some extra gas and help you cool down the engine")


if __name__ == '__main__':
    main()
