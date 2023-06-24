import subprocess

def get_boost_clock_speed():
    output = subprocess.check_output(['dmidecode', '-t', 'processor'], universal_newlines=True)
    max_speed = None
    for line in output.split('\n'):
        if 'Max Speed:' in line:
            max_speed = line.split(':')[1].strip()
    return max_speed

boost_clock_speed = get_boost_clock_speed()
print(boost_clock_speed)