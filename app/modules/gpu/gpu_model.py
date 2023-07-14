from modules.software.software_model import SoftwareModel

class GPUModel:
    def __init__(self):
        software = SoftwareModel()
        print(software.get_os_type(), software.get_os_family())




    