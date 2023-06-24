from datetime import datetime

class Convert:
    def timestamp_to_date(timestamp, format="%Y-%m-%d %H:%M"):
        date = datetime.fromtimestamp(timestamp)
        date = date.strftime(format)
        return date
    
    def mhz_to_ghz(mhz):
        ghz = mhz / 1000
        ghz = round(ghz, 1)
        return f"{ghz} GHz"

    def bytes_to_unit(bytes_value):
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        unit_index = 0
        while bytes_value >= 1024 and unit_index < len(units) - 1:
            bytes_value /= 1024
            unit_index += 1
        return f"{int(bytes_value)} {units[unit_index]}"

    


        



