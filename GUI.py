import PySimpleGUI as GUI # from https://www.tutorialspoint.com/pysimplegui/pysimplegui_popup_windows.htm
from spell_checker import spell_check #
GUI.theme("Black")

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


window = GUI.Window("Web Scraper", layout, margins=(300,300))


while True:
    event, values = window.read()
    if event == "Cancel" or event == GUI.WIN_CLOSED:
        break
    
    if event == "Submit":
        if values[0] and values[1] and values[2] and values[3]:
            if values[1].isdigit() and values[2].isdigit():     
                correction = spell_check(values[0])

                if correction is not None:
                    print(list(correction)[0])
                else:
                    print(values[0])
            else:
                GUI.popup("Please enter only numbers for fields 2 and 3")
        else:
            GUI.popup("Please fill everything correctly")
    
        