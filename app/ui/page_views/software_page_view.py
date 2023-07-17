from models.software_model import SoftwareModel

from ui.common.page import Page
from ui.common.table import TableForm, TableSingleColumn

from utils.convert import Convert
from utils.log import Log

class SoftwarePageView(Page):
    def __init__(self):
        super().__init__('Software')

        self.os_table = TableForm(title='Operating System')
        self.apps_tables = []
        
        self.insert_widget(self.os_table)

        self._controller = SoftwarePageController(self)
        Log.debug_init(self)
    
    def add_app_table(self, data, title):
        table = TableSingleColumn(title)
        table.set_data(data)
        self.insert_widget(table)        



class SoftwarePageController:
    def __init__(self, view: SoftwarePageView):
        self.view = view
        self.model = SoftwareModel()

        self.set_os_table_data()
        self.set_apps_tables(self.model.get_installed_apps())
        Log.debug_init(self)

    def set_os_table_data(self):        
        table_data = [
            ('Type', f"{self.model.get_os_type()} ({self.model.get_os_family()})"),
            ('OS', f"{self.model.get_os_name()} {self.model.get_os_version()}"),
            ('Hostname', self.model.get_hostname()),
            ('Boot Time', Convert.timestamp_to_date(self.model.get_boot_time()))]
        
        self.view.os_table.set_data(table_data)

    def set_apps_tables(self, installed_apps):
        for package_name, app_list in installed_apps:
            if package_name == 'Snap Apps' or package_name == 'Flatpak Apps':
                self.view.add_app_table(data=app_list, title=package_name)