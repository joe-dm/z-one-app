from utils.decorators import singleton
from utils.log import Log
from utils.session import Session
from utils.file import JSON


@singleton
class DeviceModel:
    def __init__(self):
        Log.task('Gathering device info')              

        self._system_manufacturer = None
        self._system_product = None 
        self._system_serial_num = None
        self._system_uuid = None
        self._system_sku_num = None
        self._system_family = None

        self._bios_vendor = None
        self._bios_version = None
        self._bios_revision = None
        self._bios_firmware_revision = None
        self._bios_release = None
        self._bios_rom_size = None  
        self._bios_language = None

        self._board_manufacturer = None
        self._board_product = None 
        self._board_version = None 
        self._board_serial_num = None 
        self._board_capacity = None
        self._board_ram_slots = None

        self._gather_info_from_os()
    
    def _gather_info_from_os(self):
        # from dmi
        if Session.os_type == 'Linux' and Session.is_admin:
            # get system info from json file
            dmi_system_info = JSON.find_dmi_entries('System Information')
            dmi_system_info = dmi_system_info[0]
            # get bios info from json file
            dmi_bios_info = JSON.find_dmi_entries('BIOS Information')
            dmi_bios_info = dmi_bios_info[0]            
            dmi_bios_language_info = JSON.find_dmi_entries('BIOS Language Information')
            dmi_bios_language_info = dmi_bios_language_info[0]
            # get baseboard info from json file
            dmi_board_info = JSON.find_dmi_entries('Base Board Information')
            dmi_board_info = dmi_board_info[0]
            dmi_board_mem_array = JSON.find_dmi_entries('Physical Memory Array')
            dmi_board_mem_array = dmi_board_mem_array[0]

            # set system values
            self._system_manufacturer = dmi_system_info['Manufacturer']
            self._system_product = dmi_system_info['Product Name']
            self._system_serial_num = dmi_system_info['Serial Number']
            self._system_uuid = dmi_system_info['UUID']
            self._system_sku_num = dmi_system_info['SKU Number']
            self._system_family = dmi_system_info['Family']
            # set bios info values
            self._bios_vendor = dmi_bios_info['Vendor']
            self._bios_version = dmi_bios_info['Version']
            self._bios_revision = dmi_bios_info['BIOS Revision']
            self._bios_firmware_revision = dmi_bios_info['Firmware Revision']
            self._bios_release = dmi_bios_info['Release Date']
            self._bios_rom_size = dmi_bios_info['ROM Size']
            self._bios_language = dmi_bios_language_info['Currently Installed Language']
            # set board info
            self._board_manufacturer = dmi_board_info['Manufacturer']
            self._board_product = dmi_board_info['Product Name']
            self._board_version = dmi_board_info['Version']
            self._board_serial_num = dmi_board_info['Serial Number']
            self._board_capacity = dmi_board_mem_array['Maximum Capacity']
            self._board_ram_slots = dmi_board_mem_array['Number Of Devices']
    
    # system info getters
    def get_system_manufacturer(self):
        return self._system_manufacturer
    def get_system_product(self):
        return self._system_product
    def get_system_serial_num(self):
        return self._system_serial_num
    def get_system_uuid(self):
        return self._system_uuid
    def get_system_sku_num(self):
        return self._system_sku_num
    def get_system_family(self):
        return self._system_family
    # bios info getters
    def get_bios_vendor(self):
        return self._bios_vendor
    def get_bios_version(self):
        return self._bios_version
    def get_bios_revision(self):
        return self._bios_revision
    def get_bios_firmware_revision(self):
        return self._bios_firmware_revision
    def get_bios_release(self):
        return self._bios_release
    def get_bios_rom_size(self):
        return self._bios_rom_size
    def get_bios_language(self):
        return self._bios_language
    # board info getters
    def get_board_manufacturer(self):
        return self._board_manufacturer
    def get_board_product(self):
        return self._board_product
    def get_board_version(self):
        return self._board_version
    def get_board_serial_num(self):
        return self._board_serial_num
    def get_board_capacity(self):
        return self._board_capacity
    def get_board_ram_slots(self):
        return self._board_ram_slots


