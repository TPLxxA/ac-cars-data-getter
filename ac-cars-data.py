import os
import csv
import json

def get_race_class():
    tags = ui_data.get('tags', '')
    tags = [s.replace("#", "") for s in tags]
    tags = [s.lower() for s in tags]

    for tag in tags:
        if tag in race_class_tags_lower:
            return race_class_tags_lower[tag]

    return ""

data_dir = r'E:\SteamLibrary\steamapps\common\assettocorsa\content\cars'
race_class_tags = {"ACL GTC": "AC Legends GTC 60s", "TCL60": "Touring Car Legends 60s", "ACL Prototypes": "AC Legends Prototypes", "ACL GTR": "Ac Legends GTR", "TransAm Legends": "TransAm Legends", "Gr7": "Group 7", "GPL67": "Grand Prix", "TCL70": "Touring Car Legends 70s", "TC2000": "Súper TC2000", "Super Silhouette": "Super Silhouette", "attc gra": "ATCC Group A", "attc grc": "ATCC Group C", "A2 Group": "A2 Group", "GTP": "IMSA GTP", "FTCC Production": "FTCC Production", "group c": "Group C", "group c2": "Group C2", "Copa Shell": "Copa Shell", "BTCC": "BTCC", "DTM": "DTM", "nascar": "NASCAR", "gt2": "GT2", "GT500": "GT500", "gt300": "GT300", "GT1": "GT1", "jtcc": "JTCC", "LMP": "LMP", "N-GT": "N-GT", "V8SC": "V8 Supercars", "lmp1": "LMP1", "DP": "Daytona Prototype", "SCCA": "SCCA Sports Car", "STCC": "STCC", "WTCC": "WTCC", "GTE": "GTE", "CT3": "Gran Turismo Group 3", "Stock Lights": "Stock Car Lights", "GT4": "GT4", "LMP2": "LMP2", "Clase 3": "Turismo Nacional Clase 3", "USCC": "USCC", "F500": "Formula 500", "TCR": "TCR", "TopCar": "Top Car", "LMP3": "LMP3", "geely": "Geely Super Cup Esports", "Stock Car Pro": "Stock Car Pro Series", "Hypercars R": "Hypercars R", "RCRS": "RCRS Super Production", "LMH": "Le Mans Hypercars", "hipole": "HiPole Bronze Cup", "SMP Historic": "SMP Historic Cup", "UFRA Class 1": "UFRA Class 1"}
race_class_tags_lower = {}
for key, value in race_class_tags.items():
    race_class_tags_lower[key.lower()] = value

# open the output csv file and write the header row
with open('cars_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Folder', 'Brand', 'Name', 'Class', 'Race Class','Year', 'Author'])

    # loop through the car folders
    for folder in os.listdir(data_dir):
        car_dir = os.path.join(data_dir, folder)
        if not os.path.isdir(car_dir):
            continue

        # read the ui_car.json file
        ui_file = os.path.join(car_dir, 'ui', 'ui_car.json')
        if not os.path.isfile(ui_file):
            continue

        try:
            with open(ui_file, 'rb') as f2:
                ui_data = json.loads(f2.read().decode('utf-8'))

            # extract the required fields and write to the output csv file
            brand = ui_data.get('brand', '')
            name = ui_data.get('name', '')
            class_ = ui_data.get('class', '')
            year = ui_data.get('year', '')
            author = ui_data.get('author', '')
        except:
            brand = ""
            name = ""
            car_class = ""
            year = ""
            author = ""
        
        if class_ in ["race", "rally", "rally raid"]:
            race_class = get_race_class()
        else:
            race_class = ""

        writer.writerow([folder, brand, name, class_, race_class, year, author])