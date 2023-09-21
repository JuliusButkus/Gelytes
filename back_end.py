from sqlalchemy.orm import Session
from db import session, Flowers, Location, DateToPlant

# Gėliu pridėjimas  Julius


# spalvu pridėjimas Ilija


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
