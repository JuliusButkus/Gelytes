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
            delete_window()
        elif event == "-UPDATE-":
            pass

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

def delete_window():
    zones = session.query(Location.zone).distinct().all()
    quantities = session.query(FlowerPlanting.qty).distinct().all()
    
    delete_layout = [
        [sg.Text("Select records to delete:")],
        [sg.Listbox(values=zones, size=(20, 5), key="-DELETE_ZONE-", enable_events=True)],
        [sg.Listbox(values=quantities, size=(20, 5), key="-DELETE_QUANTITY-", enable_events=True)],
        [sg.Button("Delete", key="-DELETE_CONFIRM-"), sg.Button("Cancel", key="-DELETE_CANCEL-")]
    ]

    delete_window = sg.Window("Delete Records", delete_layout, finalize=True)

    while True:
        event, values = delete_window.read()

        if event == "-DELETE_CANCEL-" or event == sg.WINDOW_CLOSED:
            sg.popup("Deletion canceled.")
            break
        elif event == "-DELETE_CONFIRM-":
            selected_zone = values["-DELETE_ZONE-"]
            selected_quantity = values["-DELETE_QUANTITY-"]
            
            if not selected_zone and not selected_quantity:
                sg.popup("Please select at least one criteria for deletion.")
            else:
                if selected_zone and selected_quantity:
                    back_end.delete_item(FlowerPlanting, qty=selected_quantity)
                    back_end.delete_item(Location, zone=selected_zone)
                elif selected_zone:
                    back_end.delete_item(Location, zone=selected_zone)
                elif selected_quantity:
                    back_end.delete_item(FlowerPlanting, qty=selected_quantity)
                sg.popup("Records deleted successfully.")
                delete_window.close()
                break

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

def delete_window():
    zone_list = [location.zone for location in session.query(Location).all()]
    delete_layout = [
        [sg.Combo(values=zone_list, key="-ZONE-", size=(20, 5),)],
        [sg.Button("Confirm", key="-CONFIRM-"), sg.Button("Cancel", key="-CANCEL-")]
        ]
    
    delete_window = sg.Window("Delete window", delete_layout)

    while True:
        event, values = delete_window.read()
        selected_zone = values["-ZONE-"]
        if event == "-CONFIRM-":
            try:
                session.query(FlowerPlanting)\
                .filter(FlowerPlanting.location.has(Location.zone == selected_zone))\
                .update({"location_id": None, "qty": None}, synchronize_session=False)
                session.commit()
                print(f"Deleted zone and qty for {selected_zone}")
            except Exception as error:
                session.rollback()
                sg.popup(f"Error deleting zone and qty for {selected_zone}: {str(error)}")
        if event == "-CANCEL-" or event == sg.WINDOW_CLOSED:
            sg.popup()
            break

if __name__ == "__main__":
    main()


        

