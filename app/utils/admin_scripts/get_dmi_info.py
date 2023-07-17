import json
import os
from dmidecode import DMIDecode

def save_dmi_info_to_json(dmi_list, file_path):
    # Saving DMI entries to a JSON file
    with open(file_path, "w") as json_file:
        json.dump(dmi_list, json_file, indent=4)

def get_dmi_info():
    dmi = DMIDecode()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "output")
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

    all_dmi_data = []  # List to store all DMI entries

    for data_id in range(0, 1000):  # Assuming the maximum DMI ID is 1000
        dmi_data = dmi.get(data_id)
        if dmi_data:
            all_dmi_data.append(dmi_data)

    file_path = os.path.join(output_folder, "dmi_info.json")
    save_dmi_info_to_json(all_dmi_data, file_path)

get_dmi_info()
