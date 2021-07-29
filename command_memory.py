import pickle
from datetime import date

filename = 'decision_data'



def update_decision_data():
    ## Updates the stored decision data. 
    ## Returns the updated data
    with open(filename, 'rb') as f:
        decision_data = pickle.load(f)

    current_date = date.today()
    if current_date == decision_data["date_of_last_boot"]:
        decision_data["num_boots_today"] = decision_data["num_boots_today"]+1
    else:
        decision_data["num_boots_today"] = 1
        decision_data["date_of_last_boot"] = current_date
    #Store changes
    with open(filename, 'wb') as f:
        pickle.dump(decision_data, f)


def return_decision_data():
    with open(filename, 'rb') as f:
        decision_data = pickle.load(f)

    date_of_last_boot = decision_data["date_of_last_boot"]
    date_of_last_review = decision_data["date_of_last_review"]
    num_boots_today = decision_data["num_boots_today"]

    return date_of_last_boot, date_of_last_review, num_boots_today




