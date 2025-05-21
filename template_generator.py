from datetime import datetime
import pandas as pd

def create_waybill_from_template(driver, vehicle, route):
    output_file = f"waybill_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    data = {
        "Дата": [datetime.now().strftime("%d.%m.%Y")],
        "Водій": [driver['ПІБ']],
        "Авто": [f"{vehicle['модель']} ({vehicle['держномер']})"],
        "Маршрут": [f"{route['Пункт А']} - {route['Пункт Б']}"],
        "Кілометраж": [route["Кілометраж"]],
    }

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

    return {
        "driver": driver['ПІБ'],
        "vehicle": f"{vehicle['модель']} ({vehicle['держномер']})",
        "route": f"{route['Пункт А']} - {route['Пункт Б']}",
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
