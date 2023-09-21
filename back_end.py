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


# Filtravimas paga zonas pagal spalvas pagal geles    Mindaugui



# papildimoa funkcija kiek laiko tesiasi zydėjimas
