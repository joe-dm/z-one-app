from models.device_model import DeviceModel

from ui.common.page import Page
from ui.common.table import TableForm

from utils.log import Log
from utils.session import Session


class DevicePageView(Page):
    def __init__(self):
        super().__init__('Device')

        self.system_table = TableForm(title='System')
        self.motherboard_table = TableForm(title='Motherboard')
        self.bios_table = TableForm(title='BIOS')        

        self._controller = DevicePageController(self)
        self.check_missing_info()
        Log.debug_init(self)


class DevicePageController:
    def __init__(self, view: DevicePageView):
        self.view = view
        self.model = DeviceModel()  
        self._missing_info = False

        self.set_tables()


    def set_tables(self):
        
        if Session.is_admin:
            self.view.insert_widget(self.view.system_table)
            self.view.insert_widget(self.view.motherboard_table)
            self.view.insert_widget(self.view.bios_table)

            system_table_data = [
                ('Manufacturer', self.model.get_system_manufacturer()),
                ('Product', self.model.get_system_product()),
                ('Serial Num', self.model.get_system_serial_num()),
                ('UUID', self.model.get_system_uuid()),
                ('SKU Num', self.model.get_system_sku_num()),
                ('Family', self.model.get_system_family())]
            self.view.system_table.set_data(system_table_data)
        
            bios_table_data = [
                ('Vendor', self.model.get_bios_vendor()),
                ('Version', self.model.get_bios_version()),
                ('Revision', self.model.get_bios_revision()),
                ('Release', self.model.get_bios_release()),
                ('Firmware Rev', self.model.get_bios_firmware_revision()),            
                ('ROM Size', self.model.get_bios_rom_size()),
                ('Language', self.model.get_bios_language())]
            self.view.bios_table.set_data(bios_table_data)

            board_table_data = [
                ('Manufacturer', self.model.get_board_manufacturer()),
                ('Product', self.model.get_board_product()),
                ('Version', self.model.get_board_version()),
                ('Serial Num', self.model.get_board_serial_num()),
                ('Max Capacity', self.model.get_board_capacity()),
                ('RAM Slots', self.model.get_board_ram_slots())]
            self.view.motherboard_table.set_data(board_table_data)
        else:
            self.view.missing_info = True
        

