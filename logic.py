import pandas as pd
from template_generator import create_waybill_from_template

loaded_data = {
    "drivers": None,
    "vehicles": None,
    "routes": None,
}

def load_excel_data(file_paths):
    for path in file_paths:
        if "driver" in path.lower():
            loaded_data["drivers"] = pd.read_excel(path)
        elif "vehicle" in path.lower():
            loaded_data["vehicles"] = pd.read_excel(path)
        elif "route" in path.lower():
            loaded_data["routes"] = pd.read_excel(path)

def generate_waybill():
    if not all(loaded_data.values()):
        print("Не всі дані завантажені")
        return None
    return create_waybill_from_template(
        driver=loaded_data["drivers"].iloc[0],
        vehicle=loaded_data["vehicles"].iloc[0],
        route=loaded_data["routes"].iloc[0]
    )
