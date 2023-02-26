import PySimpleGUI as GUI # from https://www.tutorialspoint.com/pysimplegui/pysimplegui_popup_windows.htm
from spell_checker import spell_check # Library that checks if words are spelled correctly

GUI.theme("DarkTeal9")

def submission_page():
    # Makes text fields used for user input
    layout = [
        [GUI.Text('Please enter \n1.What you want to eat\
                \n2.What is your price range\
                \n3.Distance you are willing to travel (in miles)\
                \n4.Your current location')],
        [GUI.Text('Food', size =(15, 1)), GUI.InputText()],
        [GUI.Text('Price Range', size =(15, 1)), GUI.InputText()],
        [GUI.Text('Distance', size =(15, 1)), GUI.InputText()],
        [GUI.Text('YOUR LOCATION', size =(15, 1)), GUI.InputText()],
        [GUI.Submit(), GUI.Cancel()]
    ]

    # Creates the GUI window for user
    window = GUI.Window("Web Scraper", layout, margins=(300,300))

    # Handles all the events when buttons on GUI are pressed
    while True:
        # 'Listens' for when user presses buttons on the GUI
        event, values = window.read()
        # Closes GUI when user presses cancel or 'X' button
        if event == "Cancel" or event == GUI.WIN_CLOSED:
            break
        # Handles user information when the user hits submit 
        if event == "Submit":
            # Makes sure that all fields are filled in
            if values[0] and values[1] and values[2] and values[3]:
                # Makes sure that fields 2 and 3 are integers since they are
                # price (in whole dollars) and miles
                if values[1].isdigit() and values[2].isdigit():     
                    
                    # Makes sure what they want to eat is spelled correctly
                    correction = spell_check(values[0])
                    # If spelled incorrectly, a message appears with a likely suggestion
                    if correction is not None:
                        GUI.popup("Do you mean "+correction+"?")
                    else:
                        print(values[0])
                # If fields 2 or 3 are not integers, a message prompts them to please 
                # re-enter the information
                else:
                    GUI.popup("Please enter only numbers for fields 2 and 3")
            # If not all fields are filled in it prompts them to do so
            else:
                GUI.popup("Please fill ALL fields please")

def GUI_main():
    submission_page()