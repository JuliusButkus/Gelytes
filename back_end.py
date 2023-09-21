import db
from db import Flowers, Month, Location,  DateToPlant, Color






# Gėliu pridėjimas  Julius
def add_flowers(flower_name, blooming_duration):
    flower = Flowers(flower_name, blooming_duration)
    db.session.add()
    db.session.commit()
    return flower


# spalvu pridėjimas Ilija

def add_color(color_name):
    new_color = Color(color=color_name)
    session.add(new_color)
    session.commit()

# mėnsiu suvedimas turėtu but suvesta


# zonu pridėjimas    Dainius


# Gėliu priskyrimas zonoms    Ruslanas

def assign_flower_to_location(session: Session, flower_name: str, location_zone: str, qty: int):
    try:
        flower = session.query(Flowers).filter_by(flower_name=flower_name).first()
        location = session.query(Location).filter_by(zone=location_zone).first()

        if flower and location:
            date_to_plant = DateToPlant(flower=flower, location=location, qty=qty)
            session.add(date_to_plant)
            session.commit()
            print(f"Assigned {flower_name} to {location_zone}.")
            return True
        else:
            print("The flower or location does not exist in the database.")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    finally:
        # Always close the session
        session.close()


# Filtravimas paga zonas pagal spalvas pagal geles    Mindaugui



# papildimoa funkcija kiek laiko tesiasi zydėjimas
