from ui.common.page import Page
from ui.common.table import TableForm, TableSingleColumn

class SoftwarePageView(Page):
    def __init__(self):
        super().__init__('Software')

        self.os_table = TableForm(title='Operating System')
        self.apps_tables = []
        
        self.insert_widget(self.os_table)
    
    def add_app_table(self, data, title):
        table = TableSingleColumn(title)
        table.set_data(data)
        self.insert_widget(table)        