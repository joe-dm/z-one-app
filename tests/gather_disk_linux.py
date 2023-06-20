import subprocess

def get_physical_disks():
    output = subprocess.check_output(["lsblk", "-ndo", "NAME,TYPE,SIZE,MOUNTPOINT,MODEL,SERIAL"])
    lines = output.decode().splitlines()
    physical_disks = []

    for line in lines:
        values = line.split()
        if len(values) >= 4:
            device_name, device_type, size, mount_point = values[:4]
            model = values[4] if len(values) > 4 else ""
            serial = values[5] if len(values) > 5 else ""

            if device_type == "disk":
                # Remove the "G" from the size if present
                size = size.rstrip("G")

                disk_info = {
                    "Device": f"/dev/{device_name}",
                    "Mount Point": mount_point,
                    "Model": model,
                    "Serial": serial,
                    "Total Size": size,
                    "Used Size": "",
                    "Free Size": ""
                }
                physical_disks.append(disk_info)

    return physical_disks



disks = get_physical_disks()
for disk in disks:
    print("Device:", disk["Device"])
    print("Mount Point:", disk["Mount Point"])
    print("Model:", disk["Model"])
    print("Serial:", disk["Serial"])
    print("Total Size:", disk["Total Size"])
    print("Used Size:", disk["Used Size"])
    print("Free Size:", disk["Free Size"])
    print()
