from start_up_commands import load_commands

review_rate = 7

def decision(date_of_last_boot, num_boots_today, date_of_last_review):
    com_dict = load_commands()

    commands_to_execute = []

    ####
    #Decide if start up should be run 
    ###
    if num_boots_today <= 1:
        commands_to_execute.append(com_dict["start_up"])

    #Decide if urgent material should be displayed first
        #if todist returns urgent_today: execute
        #if urgent email is found

    #####
    #Decide if review should be run
    #####
    review_delta = date_of_last_boot - date_of_last_review
    review_days = review_delta.days
    #Todo: put in todoist here as well!
    if review_days >= review_rate:
        commands_to_execute.append(com_dict["review"])

    #####
    #Work should be run
    #####
    commands_to_execute.append(com_dict["work_dashboard"])

    #####
    #End of day should be run
    ####
    commands_to_execute.append(com_dict["end_of_day"])

    return commands_to_execute
