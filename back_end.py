from db import Flower, Month, Location, FlowerPlanting, Color, session


def add_item(class_name, **kwargs):
    item = class_name(**kwargs)
    session.add(item)
    session.commit()
    print(item)
    return item

def delete_item(class_name, **kwargs):
    item = class_name(**kwargs)
    session.delete(item)
    session.commit()

def flowers_info(flower, color, location, qty, month):
    try:
        if flower and location and color and month:
            flower_planting = FlowerPlanting(flower=flower, location=location, color=color, month=month, qty=qty)
            session.add(flower_planting)
            session.commit()
            print(f"Assigned {flower} to {location}, bloom color {color}, month to plant {month}.")
            print(f' {qty} planted')
            return True
        else:
            print("The flower or location does not exist in the database.")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False



# items_in_class(Flower)
# add_item(Flower, flower_name="Tulip", bloom_duration=38)
# add_item(Color, color="pink")
# add_item(Month, month="January")
# add_item(Location, zone="yard")
# flowers_info("Tulip", "pink", "yard", 50, "January")
# flower = session.query(FlowerPlanting).filter_by().all()
# print(flower)