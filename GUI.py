import PySimpleGUI as GUI # from https://www.tutorialspoint.com/pysimplegui/pysimplegui_popup_windows.htm
from spell_checker import spell_check # Library that checks if words are spelled correctly

GUI.theme("DarkTeal9")

def welcome_page() -> bool:
    layout = [
        [GUI.Text("Welcome to our Page, please push Start to use")],
        [GUI.Button("START NOW"), GUI.Button("Cancel")]
    ]
    window = GUI.Window("Welcome Page", layout, margins=(300,300), element_justification='c')

    while True:
        event, values = window.read()
        if event == "START NOW" or event == GUI.WIN_CLOSED:
            window.close()
            return True
        if event == "Cancel":
            window.close()
            return False

def submission_page(proceed:bool) -> dict:
    # Makes text fields used for user input
    if (proceed):
        layout = [
            [GUI.Text('Please enter \n1.What you want to eat\
                    \n2.Price range options: inexpensive, moderate, expensive')],
            [GUI.Text('Food', size =(15, 1)), GUI.InputText()],
            [GUI.Text('Price Range', size =(15, 1)), GUI.InputText()],
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
                if values[0] and values[1]:     
                        
                    # Makes sure what they want to eat is spelled correctly
                    correction = spell_check(values[0])
                    # If spelled incorrectly, a message appears with a likely suggestion
                    if correction is not None:
                            GUI.popup("Do you mean "+correction+"?")
                    else:
                        if values[1] in ['inexpensive', 'moderate', 'expensive']:
                            window.close()
                            return values
                        else:
                            GUI.popup("Please choose only: inexpensive, moderate or expensive")
                # If not all fields are filled in it prompts them to do so
                else:
                    GUI.popup("Please fill ALL fields please")
def results_page(result: list):
    layout = [
        [GUI.Text("Your Restaurant: "+ result[1])],
        [GUI.Text("Your Price Range: "+ result[0])],
        [GUI.Text("Rating: "+ str(result[2]))],
        [GUI.Text("Address: "+ result[3])],
        [GUI.Cancel()]
    ]
    window = GUI.Window("Web Scraper", layout, margins=(300,300))
    while True:
        event, values = window.read()
        if event == "Cancel" or event == GUI.WIN_CLOSED:
                break
