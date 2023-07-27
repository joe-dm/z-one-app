import math

from PySide6 import QtWidgets

from config.theme import ThemeColor

from models.device_model import DeviceModel
from models.software_model import SoftwareModel
from models.cpu_model import CPUModel
from models.memory_model import MemoryModel
from models.network_model import NetworkModel
from models.gpu_model import GPUModel

from ui.common.page import Page
from ui.common.card import DashboardCard
from ui.common.chart import Chart

from utils.convert import Convert
from utils.log import Log
from utils.session import Session


class DashboardPageView(Page):
    def __init__(self):
        super().__init__('Dashboard')

        # grid container
        self.grid_container = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(self.grid_container)
        self.grid_layout.setContentsMargins(0,0,0,0)

        # add common widgets
        self.grid_layout.addWidget(self.label_title, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.separator, 1, 0, 1, 2)
        self.grid_layout.addWidget(self.warning_missing_info,2 , 0, 1, 2)

        # device info area
        self.device_info = DashboardCard('Device')        
        self.grid_layout.addWidget(self.device_info, 3, 0)
        # os info area
        self.os_info = DashboardCard('OS')
        self.grid_layout.addWidget(self.os_info, 3, 1)

        # cpu info area
        self.cpu_chart = Chart('CPU', y_axis_max=100, height=85)
        self.cpu_info = DashboardCard()
        self.grid_layout.addWidget(self.cpu_chart, 4, 0)
        self.grid_layout.addWidget(self.cpu_info, 5, 0)
        # ram info area
        self.ram_chart = Chart('RAM', y_axis_max=100, height=85)
        self.ram_info = DashboardCard()
        self.grid_layout.addWidget(self.ram_chart, 4, 1)
        self.grid_layout.addWidget(self.ram_info, 5, 1)

        # network info area
        self.network_info = DashboardCard('Network')
        self.grid_layout.addWidget(self.network_info, 6, 0)
        # display info area
        self.display_info = DashboardCard('Display')
        self.grid_layout.addWidget(self.display_info, 6, 1)        

        # add the container to the parent layout        
        self.page_layout.addWidget(self.grid_container)
        
        self.controller = DashboardPageController(self)
        self.check_missing_info()
        Log.debug_init(self)

class DashboardPageController:
    def __init__(self, view: DashboardPageView):
        self.view = view

        # set device info
        self.device_model = DeviceModel()     
        if Session.is_admin:   
            device_info = (
                f'{self.device_model.get_system_product()}<br>'
                f'{self.device_model.get_system_family()}<br>'
                f'Motherboard: {self.device_model.get_board_product()}<br>'
                f'BIOS: {self.device_model.get_bios_vendor()} '
                f'{self.device_model.get_bios_version()} '
                f'{self.device_model.get_bios_revision()}')     
        else:
            device_info = 'Unavailable'
            self.view.missing_info = True
        self.view.device_info.set_info_text(device_info)

        # set os info
        self.software_model = SoftwareModel()
        os_info = (
            f'{self.software_model.get_os_type()} ({self.software_model.get_os_family()})<br>'
            f'{self.software_model.get_os_name()}<br>'
            f'Hostname: {self.software_model.get_hostname()}<br>'
            f'Boot Time: {Convert.timestamp_to_date(self.software_model.get_boot_time())}')
        self.view.os_info.set_info_text(os_info)

        # set cpu info
        self.cpu_model = CPUModel()
        cache_size, cache_unit = Convert.bytes_to_unit(self.cpu_model.get_total_cache())
        cpu_info = (
            f'{self.cpu_model.get_name()}<br>'
            f'{self.cpu_model.get_cores_physical()} Cores / {self.cpu_model.get_cores_logical()} Threads<br>'
            f'{self.cpu_model.get_frequency_max()} GHz {self.cpu_model.get_architecture()}-Bit Processor<br>'
            f'{cache_size} {cache_unit} Cache')
        self.view.cpu_info.set_info_text(cpu_info)
        self.cpu_model.signals.updated_usage.connect(self.view.cpu_chart.update_chart)

        # set ram info
        self.memory_model = MemoryModel()
        ram_size = self.memory_model.get_ram_total() / (1024 * 1024 * 1024)               
        ram_info = (
            f'{math.ceil(ram_size)} GB<br>'
            f'{self.memory_model.get_ram_type()}'
        )
        self.view.ram_info.set_info_text(ram_info)
        self.memory_model.signals.updated_ram_usage.connect(self.view.ram_chart.update_chart)

        # set network info
        self.network_model = NetworkModel()
        self.network_model.signals.updated_internet_available.connect(self.update_network_card)

        # set display info
        self.gpu_model = GPUModel()
        display_dict = self.gpu_model.get_display_adapter_dict()        
        display_info = (
            f'{display_dict["product"]}<br>'
            f'{display_dict["vendor"]}<br>'
            f'{display_dict["clock"]}<br>'
            f'{self.gpu_model.get_resolution()}'
        )
        self.view.display_info.set_info_text(display_info)
    
    def update_network_card(self, value):
        network_info = ''

        # check if internet is available
        if self.network_model.get_internet_available() == True:            
            network_info = f"<span style='color:{ThemeColor.green};'>Internet Available</span><br>"

            if self.network_model.get_speed_download():
                network_info += f'{self.network_model.get_speed_download():.1f} MBps (Download)<br>'
            if self.network_model.get_isp():
                network_info += f'{self.network_model.get_isp()}<br>'

            network_info += f'Quality: {self.network_model.get_quality()}'                
                
        else:
            network_info = f"<span style='color:{ThemeColor.red};'>Internet Unavailable</span>"
                
        self.view.network_info.set_info_text(network_info)
        