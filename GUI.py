# Tikslas:
#     sukurti programėle kuri leistu susiformuoti gelynus. programa turėtu leisti susikurti vartotojui zonas, 
#     zonoms priskirti augalus is esamo sąraso arba isivesti augalus pačiam, taip pat nurodyti augalu spalvas bei zydėjimo trukmę dienomis.
#     vartotojas:
#     turi turėti galimybe matyti kokie augalai(ir spalvos) yra susodinti zonoje
#     turi tureti galimybe issifiltruoti augalus pagal sodinimo menesi arba zydėjimo trukme
#     issifiltruoti augalu kieki

import PySimpleGUI as sg
import back_end
from db import Flower, Color, FlowerPlanting, Location, Month, session
    

def main():
    flower_list = [flower.flower_name for flower in session.query(Flower).all()]
    color_list = [color.color for color in session.query(Color).all()]
    zone_list = [location.zone for location in session.query(Location).all()]
    month_list = [month.month for month in session.query(Month).all()]
    layout = [
        [sg.Combo(values=flower_list, key="-FLOWER-", size=(20, 5), enable_events=True),
         sg.Combo(values=color_list, key="-COLOR-", size=(20, 5), enable_events=True),
         sg.Combo(values=zone_list, key="-LOCATION-", size=(20, 5), enable_events=True),
         sg.Combo(values=month_list, key="-MONTH-", size=(20, 5), enable_events=True)],
        [sg.Table(
            values=[],
            headings=["flower_name", "color", "bloom_duration", "zone", "month", "QTY" ],
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
        elif event == "-FLOWER-": # Julius
            selected_flower = values["-FLOWER-"]
            filtered_flowers = (
                session.query(FlowerPlanting)
                .filter(FlowerPlanting.flower.has(flower_name=selected_flower))
                .all())
            update_table(main_window, filtered_flowers)
        elif event == "-COLOR-": # Dainius
            selected_color = values["-COLOR-"]
            filtered_flowers = (
                session.query(FlowerPlanting)
                .filter(FlowerPlanting.color.has(color=selected_color))
                .all())
            update_table(main_window, filtered_flowers)
        elif event == "-LOCATION-": # Mindaugas
            selected_location = values["-LOCATION-"]
            filtered_flowers = (
                session.query(FlowerPlanting)
                .filter(FlowerPlanting.location.has(zone=selected_location))
                .all())
            update_table(main_window, filtered_flowers)
        elif event == "-MONTH-":
            selected_month = values["-MONTH-"]
            filtered_flowers = (
                session.query(FlowerPlanting)
                .filter(FlowerPlanting.month.has(month=selected_month))
                .all())
            update_table(main_window, filtered_flowers)
        elif event == "-DELETE-":
            pass # Ilija   naujas langas istrinti zona ir kieki

    main_window.close()
    
def add_window():
    add_layout = [
        [sg.Listbox(values=["Flower", "Color", "Location"], size=(20, 5), enable_events=True, key="-CLASS-"), ],
        [sg.Text("Add flower name and bloom duration in days"), sg.Input(key="-FLOWER_NAME-", disabled=True, disabled_readonly_background_color="gray25")],
        [sg.Input(key="-DURATION-", disabled=True, disabled_readonly_background_color="gray25")],
        [sg.Text("Add flower color"), sg.Input(key="-COLOR-", disabled=True, disabled_readonly_background_color="gray25")],
        [sg.Text("Add location "), sg.Input(key="-ZONE-", disabled=True, disabled_readonly_background_color="gray25")],
        [sg.Button("Confirm", key="-CONFIRM-"), sg.Button("Cancel", key="-CANCEL-")]
    ]

    add_window = sg.Window("Add meniu", add_layout, finalize=True)

    while True:
        event, values = add_window.read()
        selected_classes = values["-CLASS-"]
        if selected_classes:
            selected_class = selected_classes[0]
            if selected_class == "Flower":
                add_window["-FLOWER_NAME-"].update(disabled=False)
                add_window["-DURATION-"].update(disabled=False)
                add_window["-COLOR-"].update(disabled=True)
                add_window["-ZONE-"].update(disabled=True)
            if selected_class == "Color":
                add_window["-COLOR-"].update(disabled=False)
                add_window["-ZONE-"].update(disabled=True)
                add_window["-FLOWER_NAME-"].update(disabled=True)
                add_window["-DURATION-"].update(disabled=True)
            if selected_class == "Location":
                add_window["-ZONE-"].update(disabled=False)
                add_window["-FLOWER_NAME-"].update(disabled=True)
                add_window["-DURATION-"].update(disabled=True)
                add_window["-COLOR-"].update(disabled=True)

        if event == "-CANCEL-" or event == sg.WINDOW_CLOSED:
            sg.popup()
            break
        elif event == "-CONFIRM-":
            if selected_class == "Flower":
                try:
                    flower_name = values["-FLOWER_NAME-"]
                    bloom_duration = int(values["-DURATION-"])
                    back_end.add_item(Flower, flower_name=flower_name, bloom_duration=bloom_duration)
                except ValueError:
                    sg.popup("nurodyta bloga reiksme")
            elif selected_class == "Color":
                color = values["-COLOR-"]
                back_end.add_item(Color, color=color)
            elif selected_class == "Location":
                zone = values["-ZONE-"]
                back_end.add_item(Location, zone=zone)      

    add_window.close()    

def join_window():
    flower_list = session.query(Flower).all()
    color_list = session.query(Color).all()
    zone_list = session.query(Location).all()
    month_list = session.query(Month).all()
    join_layout = [
        [sg.Combo(values=flower_list, key="-FLOWER-", size=(20, 5),)],
        [sg.Combo(values=color_list, key="-COLOR-", size=(20, 5),)],
        [sg.Combo(values=zone_list, key="-ZONE-", size=(20, 5),)],
        [sg.Combo(values=month_list, key="-MONTH-", size=(20, 5),)],
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
            try:
                selected_flower = values["-FLOWER-"]
                selected_color = values["-COLOR-"]
                selected_zone = values["-ZONE-"]
                selected_month = values["-MONTH-"]
                qty = int(values["-QTY-"])
                back_end.flowers_info(flower=selected_flower, color=selected_color, location=selected_zone, qty=qty, month=selected_month)
            except Exception as error:
                sg.popup(f'Turi buti pasirinkti visi laukai ir 5vestas kiekis: Klaida {error} ')

    join_window.close() 


def update_table(window, filtered_flowers):
    data = [
        [flower_planting.flower.flower_name,
         flower_planting.color.color,
         flower_planting.flower.bloom_duration,
         flower_planting.location.zone,
         flower_planting.month.month,
         flower_planting.qty]
        for flower_planting in filtered_flowers]

    window["-TABLE-"].update(values=data)

if __name__ == "__main__":
    main()


        

