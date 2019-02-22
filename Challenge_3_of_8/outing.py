
import outing_respitory

while True:
    print('\nWelcome to Komodo Claims Dept.!\n')
    user_input = input('1) List All Outings:\n' +
                       '2) Add Outings to List:\n' +
                       '3) View Claculations:\n' +
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
        if outing_type_check == "GOLF":
            outing_type = outing_type_check
            outing_cost_ind = float(input("Enter the Individual Cost: "))
            outing_date = input("Enter the Date of Outing: ")
            outing_attendance = float(input("Expected Attendance: "))
            outing_respitory.add_event(outing_type, outing_cost_ind, outing_date, outing_attendance)
            print("Outing Added!\n")
        elif outing_type_check == "BOWLING": 
            outing_type = outing_type_check
            outing_cost_ind = float(input("Enter the Individual Cost: "))
            outing_date = input("Enter the Date of Outing: ")
            outing_attendance = float(input("Expected Attendance: "))
            outing_respitory.add_event(outing_type, outing_cost_ind, outing_date, outing_attendance)
            print("Outing Added!\n")
        elif outing_type_check == "AMUSEMENT PARK": 
            outing_type = outing_type_check
            outing_cost_ind = float(input("Enter the Individual Cost: "))
            outing_date = input("Enter the Date of Outing: ")
            outing_attendance = float(input("Expected Attendance: "))
            outing_respitory.add_event(outing_type, outing_cost_ind, outing_date, outing_attendance)
            print("Outing Added!\n")
        elif outing_type_check == "CONCERT":
            outing_type = outing_type_check
            outing_cost_ind = float(input("Enter the Individual Cost: "))
            outing_date = input("Enter the Date of Outing: ")
            outing_attendance = int(input("Expected Attendance: "))
            outing_respitory.add_event(outing_type, outing_cost_ind, outing_date, outing_attendance)
            print("Outing Added!\n")
        else:
            print("Not a valid outing type!\n")
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
        exit(0)
