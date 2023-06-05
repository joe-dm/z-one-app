class ThemeSize:
    widget_spacing = 3
    sidebar_button = 32
    sidebar_icon = 20

class ThemeColor:
    # main colors
    primary =       '#ff8400'
    secondary =     '#7dd2ff'   
    secondary_dark ='#3daee9'  
    # traffic light
    green =         '#79ffb1'
    yellow =        '#fffd8a'
    red =           '#ff7d6c'
    # grayscale
    white =         '#ffffff'
    gray_light =    '#cccccc'
    gray_dark =     '#757575'
    black =         '#1d2022'
    black_dark =    '#191919'

class ThemeFont:
    console_family = 'monospace'
    console_size = 10

class ThemeStylesheet:
    console = (
        f"background-color: {ThemeColor.black_dark};"
        f"border:none;"
    )    
    sidebar_button = (
        f"text-align: left;"
        f"padding: 0px 5px 0px 5px;"
    )