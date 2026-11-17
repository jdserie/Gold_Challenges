import math

import outing_respitory


def main():
    while True:
        print('\nWelcome to Komodo Outings!\n')
        user_input = input('1) List All Outings:\n' +
                           '2) Add Outings to List:\n' +
                           '3) View Calculations:\n' +
                           '4) Exit\n' +
                           '>')

        if user_input == "1":
            o_events = outing_respitory.list_all_events()
            if len(o_events) > 0:
                for a in o_events:
                    print(a)
            else:
                print("No Events Found!\n")
        elif user_input == "2":
            outing_type_check = input("Enter an Outing Type (Golf, Bowling, Amusement Park, Concert): ").upper()
            if outing_type_check not in {"GOLF", "BOWLING", "AMUSEMENT PARK", "CONCERT"}:
                print("Not a valid outing type.")
                continue
            try:
                cost = float(input("Enter the individual cost: "))
                date = input("Enter the date of the outing: ")
                attendance = int(input("Expected attendance: "))
                if not math.isfinite(cost) or cost < 0 or attendance < 0:
                    raise ValueError
            except ValueError:
                print("Enter a valid nonnegative cost and a whole attendance count.")
                continue
            outing_respitory.add_event(outing_type_check, cost, date, attendance)
            print("Outing added.")
        elif user_input == "3":
            calc_type = input("1) Overall\n2) By Type\n> ")
            if calc_type == "1":
                o_events_price = outing_respitory.calc_overall()
                o_events = outing_respitory.list_all_events()
                if len(o_events) > 0:
                    print(f"${o_events_price}")
                else:
                    print("No Events Found!\n")
            elif calc_type == "2":
                lookup_type = input("Select Outing: Golf, Bowling, Amusement Park, Concert\n> ").upper()
                ind_event_price = outing_respitory.calc_by_type(lookup_type)
                event_list = outing_respitory.list_all_events()
                if len(event_list) > 0:
                    print(f"${ind_event_price}")
                else:
                    print("No Events Found!\n")
            else:
                print("Invalid Event!")
        elif user_input == "4":
            return


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")
