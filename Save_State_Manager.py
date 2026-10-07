from datetime import date, datetime

def displaySaveStates():
    # Displays all three save states.
    return

def createNewSaveState(name):
    # Takes name, date, and time to create new save state.
    current_date = str(date.today())
    current_time = str(datetime.now().strftime("%H:%M:%S"))
    
    print("Name: " + name)
    print("Date: " + current_date)
    print("Time: " + current_time)

def loadSaveState(state_to_load):
    # Takes selected state and loads it.
    print("State to Load: " + state_to_load)

def deleteSaveState(state_to_delete):
    # Takes selected state and deletes it.
    print("State to Delete" + state_to_delete)