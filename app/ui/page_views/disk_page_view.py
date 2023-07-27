from models.disk_model import DiskModel

from ui.common.page import Page
from ui.common.table import TableForm
from utils.log import Log

class DiskPageView(Page):
    def __init__(self):
        super().__init__('Disks')
        self._controller = DiskPageController(self)
        self.check_missing_info()
        Log.debug_init(self)


    def add_device_table(self, data, title):
        table = TableForm(title)
        table.set_data(data)
        self.insert_widget(table)


class DiskPageController:
    def __init__(self, view: DiskPageView):
        self.view = view
        self.model = DiskModel()
        self.set_device_tables()

    def set_device_tables(self):
        disk_devices = self.model.get_disk_devices()

        if disk_devices:
            for device in disk_devices:
                # define if disk is solid/rotational
                rotational = device.get('ROTA', None)
                if rotational == '1': disk_type = 'Rotational'
                elif rotational == '0': disk_type = 'Solid'
                else: disk_type = None

                # get disk table data
                disk_table_data = [
                    ('Path', device.get('PATH', None)),
                    ('State', device.get('STATE', None)),
                    ('Size', device.get('SIZE', None)),
                    ('Transport', device.get('TRAN', None)),
                    ('Model', device.get('MODEL', None)),
                    ('Serial', device.get('SERIAL', None)),
                    ('Type', disk_type),
                    ('Read-Only', device.get('RO', None))
                ]

                # create table in the view
                device_name = device.get('NAME', None)
                self.view.add_device_table(data=disk_table_data, title=f'Device: {device_name}')

                # get partitions data
                partitions = device.get('PARTITIONS', [])
                if partitions:
                    for partition in partitions:
                        partition_table_data = [
                            ('Description', partition.get('PARTTYPENAME', None)),
                            ('Fylesystem', partition.get('FSTYPE', None)),
                            ('Size', partition.get('SIZE', None)),
                            ('Used', partition.get('FSUSED', None)),
                            ('Mount Point', partition.get('MOUNTPOINT', None))]
                        
                        partition_name = partition.get('NAME', None)
                        self.view.add_device_table(data=partition_table_data, title=f"Partition: {device_name}/{partition_name}")