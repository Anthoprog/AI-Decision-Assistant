import tkinter as tk
from tkinter import messagebox


# Task 1: Represent the Conditions
# These are variables that represent the different conditions for commuting
def initialize_conditions():
    return {
        'Rain': False,
        'HeavyTraffic': False,
        'EarlyMeeting': False,
        'Strike': False,
        'Appointment': False,
        'RoadConstruction': False,
        'TrexOnTheRoad': False  # New condition: T-Rex on the road
    }


# Task 2: Define the Commuting Options
# These are functions that return the commuting options as strings
def work_from_home():
    return "Work from Home (WFH)"


def drive():
    return "Drive"


def take_public_transport():
    return "Take Public Transport"


# Task 3: Create the Knowledge Base
# This function determines the best commuting option based on the rules
def get_commute_suggestion(conditions):
    rain = conditions['Rain']
    heavy_traffic = conditions['HeavyTraffic']
    early_meeting = conditions['EarlyMeeting']
    strike = conditions['Strike']
    appointment = conditions['Appointment']
    road_construction = conditions['RoadConstruction']
    trex_on_the_road = conditions['TrexOnTheRoad']

    # New rule: If there's a T-Rex on the road, work from home
    if trex_on_the_road:
        return work_from_home()  # T-Rex on the road -> Work from Home
    elif appointment:
        return drive()  # If there's an appointment, you should drive
    elif road_construction:
        return work_from_home()  # Avoid driving if there is road construction
    elif rain or early_meeting:
        return work_from_home()  # Work from home if it's raining or there's an early meeting
    elif not rain and not heavy_traffic and not strike:
        return drive()  # Drive if there's no rain, traffic, or strike
    elif not strike and not rain:
        return take_public_transport()  # Take public transport if no strike or rain
    else:
        return "No suitable option found"


# Task 5: Perform Model Checking
# This function shows the suggestion in the GUI
def show_suggestion():
    conditions = {
        'Rain': rain_var.get(),
        'HeavyTraffic': heavy_traffic_var.get(),
        'EarlyMeeting': early_meeting_var.get(),
        'Strike': strike_var.get(),
        'Appointment': appointment_var.get(),
        'RoadConstruction': road_construction_var.get(),
        'TrexOnTheRoad': trex_on_the_road_var.get()  # Get T-Rex condition
    }

    # Get commuting suggestion based on the knowledge base
    suggestion = get_commute_suggestion(conditions)

    # Display the result
    messagebox.showinfo("Commuting Suggestion", f"The assistant suggests: {suggestion}")


# Task 4: Define Queries
# Creating the Tkinter GUI to query the commuting options
def commuting_assistant_gui():
    # Initialize the main window
    window = tk.Tk()
    window.title("Commuting Assistant")

    # Initialize condition variables for the checkboxes
    global rain_var, heavy_traffic_var, early_meeting_var, strike_var, appointment_var, road_construction_var, trex_on_the_road_var
    rain_var = tk.BooleanVar()
    heavy_traffic_var = tk.BooleanVar()
    early_meeting_var = tk.BooleanVar()
    strike_var = tk.BooleanVar()
    appointment_var = tk.BooleanVar()
    road_construction_var = tk.BooleanVar()
    trex_on_the_road_var = tk.BooleanVar()  # New variable for T-Rex on the road

    # Labels and checkboxes for the conditions
    tk.Label(window, text="Select the current conditions:").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    tk.Checkbutton(window, text="Is it raining?", variable=rain_var).grid(row=1, column=0, sticky='w')
    tk.Checkbutton(window, text="Is there heavy traffic?", variable=heavy_traffic_var).grid(row=2, column=0, sticky='w')
    tk.Checkbutton(window, text="Do you have an early meeting?", variable=early_meeting_var).grid(row=3, column=0,
                                                                                                  sticky='w')
    tk.Checkbutton(window, text="Is there a public transport strike?", variable=strike_var).grid(row=4, column=0,
                                                                                                 sticky='w')
    tk.Checkbutton(window, text="Do you have a doctor's appointment?", variable=appointment_var).grid(row=5, column=0,
                                                                                                      sticky='w')
    tk.Checkbutton(window, text="Is there road construction?", variable=road_construction_var).grid(row=6, column=0,
                                                                                                    sticky='w')
    tk.Checkbutton(window, text="Is there a T-Rex on the road?", variable=trex_on_the_road_var).grid(row=7, column=0,
                                                                                                     sticky='w')  # New checkbox for T-Rex

    # Button to generate the commuting suggestion
    tk.Button(window, text="Get Suggestion", command=show_suggestion).grid(row=8, column=0, columnspan=2, pady=10)

    # Run the main loop of the application
    window.mainloop()


# Task 7: Add More Rules
# New rule for T-Rex on the road has been added above in the get_commute_suggestion function.

# Run the GUI application
if __name__ == "__main__":
    commuting_assistant_gui()
