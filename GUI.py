# Tikslas:
#     sukurti programėle kuri leistu susiformuoti gelynus. programa turėtu leisti susikurti vartotojui zonas, 
#     zonoms priskirti augalus is esamo sąraso arba isivesti augalus pačiam, taip pat nurodyti augalu spalvas bei zydėjimo trukmę dienomis.
#     vartotojas:
#     turi turėti galimybe matyti kokie augalai(ir spalvos) yra susodinti zonoje
#     turi tureti galimybe issifiltruoti augalus pagal sodinimo menesi arba zydėjimo trukme
#     issifiltruoti augalu kieki

import PySimpleGUI as sg
import back_end
    

def main():
    layout = [
        [sg.Table(
            values=[],
            headings=["flower_name", "color", "bloom_duration" "zone", "month" ],
            key="-TABLE-",
            justification='center',
            enable_events=True)
            ],
        [sg.Button("Add", key="-ADD-"), sg.Button("Join", key="-JOIN-"), sg.Button("Filter", key="-FILTER-"), sg.Button("Delete", key="-DELETE-")],
        [sg.Text("logeris", key="-LOGERIS-"), sg.Button("exit", key="-EXIT-")],
    ]

    main_window = sg.Window("Flowers", layout, finalize=True)

    while True:
        event, values = main_window.read()
        if event == "-EXIT-" or event == sg.WINDOW_CLOSED:
            sg.popup()
            break
        elif event == "-ADD-":
            add_window()
        elif event == "-JOIN-":
            join_window()
        elif event == "-FILTER-":
            filter_window()
        elif event == "-DELETE-":
            pass

    main_window.close()
    
def add_window():
    add_layout = [
        [sg.Listbox("class list", key="-CLASS-")],
        [sg.Text("Add flower name and bloom duration in days"), sg.Input(key="-FLOWER_NAME-")],
        [sg.Input(key="-DURATION-")],
        [sg.Text("Add flower color"), sg.Input(key="-COLOR-")],
        [sg.Text("Add location "), sg.Input(key="-ZONE-")],
        [sg.Button("Confirm", key="-CONFIRM-"), sg.Button("Cancel", key="-CANCEL-")]
    ]

    add_window = sg.Window("Add meniu", add_layout)

    while True:
        event, values = add_window.read()
        if event == "-CANCEL-" or event == sg.WINDOW_CLOSED:
            sg.popup()
            break
        elif event == "-CONFIRM-":
            pass

    add_window.close()    

def join_window():
    join_layout = [
        [sg.Listbox("flower list", key="-FLOWER-")],
        [sg.Listbox("color list", key="-COLOR-")],
        [sg.Listbox("zone list", key="-ZONE-")],
        [sg.Listbox("month list", key="-MONTH-")],
        [sg.Text("Add QTY "), sg.Input(key="-QTY-")],
        [sg.Button("Confirm", key="-CONFIRM-"), sg.Button("Cancel", key="-CANCEL-")]
        ]

    join_window = sg.Window("Add meniu", join_layout, finalize=True)

    while True:
        event, values = join_window.read()
        if event == "-CANCEL-" or event == sg.WINDOW_CLOSED:
            sg.popup()
            break
        elif event == "-CONFIRM-":
            pass

    join_window.close() 

def filter_window():
    filter_layout = [
        [sg.Listbox("flower list", key="-FLOWER-")],
        [sg.Listbox("color list", key="-COLOR-")],
        [sg.Listbox("zone list", key="-ZONE-")],
        [sg.Listbox("month list", key="-MONTH-")],
        [sg.Listbox("Filter", key="-FILTER-")],
        [sg.Button("Exit", key="-EXIT-") ]
        ]

    filter_window = sg.Window("Add meniu", filter_layout, finalize=True)

    while True:
        event, values = filter_window.read()
        if event == "-EXIT-" or event == sg.WINDOW_CLOSED:
            sg.popup()
            break
        elif event == "-CONFIRM-":
            pass

    filter_window.close()   

 

if __name__ == "__main__":
    main()


        

