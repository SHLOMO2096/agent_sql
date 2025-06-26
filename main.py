from Dal.agent_dal import Agent_dal


print("Welcome to the Eagle's Eye system!")
while True:
    print("\nPlease select an option:")
    print("1. Add Agent")
    print("2. Get All Agents")
    print("3. Get Agent by Code Name")
    print("4. Update Agent")
    print("5. Delete Agent")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    dal = Agent_dal()

    if choice == '1':
        parmeters = {'codeName':"" , 'realName':"", 'location':"", 'status':"", 'missionsCompleted':""}
        for key in parmeters.keys():
            value = input(f"Enter {key.replace('_', ' ').title()}: ")
            parmeters[key] = value
        dal.add_agent(parmeters['codeName'], parmeters['realName'],parmeters['location'],parmeters['status'], parmeters['missionsCompleted'])
        print("Agent added successfully!")
    elif choice == '2':
        dal.get_all_agents()
    elif choice == '3':
        # Call function to get agent by code name
        pass
    elif choice == '4':
        # Call function to update agent
        pass
    elif choice == '5':
        # Call function to delete agent
        pass
    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")