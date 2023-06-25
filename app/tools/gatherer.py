from tools.gatherer_modules.cpu import CPUGatherer, CPUMonitor
from tools.gatherer_modules.network import NetworkMonitor

class Gatherer:
    def __init__(self):

        cpu_gatherer = CPUGatherer()
        cpu_mon = CPUMonitor()

        net_mon = NetworkMonitor()
