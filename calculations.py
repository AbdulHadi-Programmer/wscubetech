print("Dynamic Scripts Team: \nThe Money Distributer in the System \n---------------------------------------")

# Lead
def calculate_lead_distribution(total_project):
    project_hunter = total_project * 0.20
    group_fund = total_project * 0.05 # Calculate and give the 5% of total project 
    lead_share = total_project * 0.75 # Calculate lead share
    # lead_share = total_project - project_hunter - group_fund 
    num_of_member = int(input("Enter the No of Members Worked on this Project: "))
    no_per_person = (lead_share - 10000) / num_of_member
    lead_with_person_share = no_per_person + 10_000

    if num_of_member > 1:  
        print(f"Lead get {no_per_person} pkr + 10_000 = {lead_with_person_share} because he has main authority and responsibility")  
        print(f"The Money is Divided into {num_of_member:.2f} Members, each get: {no_per_person} ")
    else: 
        print(f"The Amount that Lead get (75%) : {lead_share} pkr ")

    print(f"The Project Total Cost is : {total_project} pkr")
    print(f"The Project Hunter get (20%): {project_hunter} pkr \n\n\n")
    # print(f"The Lead give Group Fund (5%) : {group_fund} pkr ")

calculate_lead_distribution(100_000)

# def the(prompt):
#     print(prompt)
# the("Abdul Hadi is a Developer and Programmer")

# Core Members
def calculate_core_distribution(total_project):
    project_hunter = total_project * 0.20
    group_fund = total_project * 0.15 # Calculate and give the 5% of total project 
    lead_share = total_project * 0.10 # Calculate lead share
    core_amount = total_project * 0.55 # Calculate core share
    num_of_member = int(input("Enter the No of Members Worked on this Project: "))
    no_per_person = core_amount / num_of_member

    print(f"*) The Project Total Cost is: {total_project} pkr")
    print(f"1.  The Project Hunter get (20%): {project_hunter} pkr")
    print(f"2. The Group Fund He Give (15%): {group_fund} pkr ")
    print(f"3. The Lead get (10%): {lead_share} pkr ")

    if num_of_member > 1 :    
        print(f"4. The Money is Divided into {num_of_member:.2f} Members, each get: {no_per_person} ")

    else:
        print(f"4. The Core Team Member get (55%): {core_amount:.2f} pkr \n\n\n")

calculate_core_distribution(100_000)


# Members :
def calculate_member_distribution(total_project):
    project_hunter = total_project * 0.20
    group_fund = total_project * 0.25 # Calculate and give the 5% of total project 
    lead_share = total_project * 0.10 # Calculate lead share
    member_amount = total_project * 0.45 # Calculate lead share
    no_of_members = int(input("Enter the No of Members Worked on this Project."))
    no_per_person = member_amount / no_of_members


    print(f"*) The Project Total Cost is: {total_project} pkr")
    print(f"1.  The Project Hunter get (20%): {project_hunter} pkr")
    print(f"2. The Group Fund He Give (25%): {group_fund} pkr ")
    print(f"3. The Lead get (10%): {lead_share} pkr ")

    if no_of_members > 1:
        print(f"4. The Money is Divided into {no_of_members} Members, each get: {no_per_person} ")

    else:
        print(f"4. The Team Member get (45%): {member_amount} pkr \n\n\n")

calculate_member_distribution(100_000)


def calculate_group_fund_distribution():   # fund):
    # current_fund = 200
    fund = 200

    food_entertainment = fund * 0.20
    group_rewards = fund * 0.30
    group_expenses = fund * 0.50
    
    print(f"*) The Fund is Distributed into 3 Parts:")
    print(f"-  The Total Fund is : {fund}")
    print(f"1. The Food and Entertainment is (20%): {food_entertainment} pkr")
    print(f"2. The Group Rewards is (30%): {group_rewards} pkr")
    print(f"3. The Group Expenses is (50%): {group_expenses} pkr ")

calculate_group_fund_distribution()
