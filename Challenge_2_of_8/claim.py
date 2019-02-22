# UI File

import ClaimRepository


while True:
    print('\nWelcome to Komodo Claims Dept.!\n')
    user_input = input('1) List Claims:\n' +
                       '2) Justify Claims:\n' +
                       '3) Enter New Claim:\n' +
                       '4) Exit\n' +
                       '>')

    if user_input == '1':
        list_of_claims = ClaimRepository.claim_list
        length_of_list = len(list_of_claims)
        if length_of_list > 0:
            print(list_of_claims)
        else:
            print("No Claims Found!\n")
    elif user_input == '2':
        list_of_claims = ClaimRepository.claim_list
        length_of_list = len(list_of_claims)
        if length_of_list > 0:
            print(list_of_claims[0])
            ask_q = input("Do you waish to manage this claim? y/n\n> ")
            if ask_q == 'y':
                review_q = list_of_claims.pop(0)                                # GOOD pop trick - for JDS
                print("Claim addressed!\n")
            elif ask_q == 'n':
                print("Action Cancelled!\n")
            else:
                print("Syntax Error!\n")
        else:
            print("No Claims Found!\n")
    elif user_input == '3':
        claimID = input("Enter Claim ID: ")
        claimType = input("Enter Claim Type: ")
        description = input("Enter Claim Description: ")
        claimAmount = input("Enter Claim Amount in Dollars and Cents: ")
        dateOfIncident = input("Enter Incident Date: ")
        dateOfClaim = input("Enter Date of Claim: ")
        isValid = bool(input("Is it valid? (Hit enter for False or type any character then enter, for True): "))
        ClaimRepository.enter_claims_list(claimID, claimType, description, claimAmount, dateOfIncident, dateOfClaim, isValid)
        print("New Claim Added")
    elif user_input == '4':
        exit(0)
