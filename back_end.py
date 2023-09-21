import db
from db import Flowers, Month, Location,  DateToPlant, Color





# Gėliu pridėjimas  Julius
def add_flowers(flower_name, blooming_duration):
    flower = Flowers(flower_name, blooming_duration)
    db.session.add()
    db.session.commit()
    return flower


# spalvu pridėjimas Ilija


# mėnsiu suvedimas turėtu but suvesta


# zonu pridėjimas    Dainius


# Gėliu priskyrimas zonoms    Ruslanas


# Filtravimas paga zonas pagal spalvas pagal geles    Mindaugui



# papildimoa funkcija kiek laiko tesiasi zydėjimas
