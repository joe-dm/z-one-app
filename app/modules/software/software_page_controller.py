from modules.software.software_model import SoftwareModel
from modules.software.software_page_view import SoftwarePageView
from utils.helpers.convert import Convert

class SoftwarePageController:
    def __init__(self, model: SoftwareModel, view: SoftwarePageView):
        self.view = view
        self.model = model

        self.set_os_table_data()
        self.set_apps_tables(self.model.get_installed_apps())

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
