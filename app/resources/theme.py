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
    white_2 =       '#cccccc'  
    
    gray =          '#757575'
    gray_2 =        '#31363b'
    gray_3 =        '#272b2f'

    black_midnight ='#1d2022'
    black_dark =    '#191919'
    black =         '#000000'
    


class ThemeStylesheet:
    console = (
        f'background-color: {ThemeColor.black_dark};'
        f'border:none;'
        f'font-family: "Courier New", monospace;'
        f'font-size: 13px;'
    )

    page = (
        f'background-color: {ThemeColor.black_midnight};'
        f'border: none;'
    )
    page_title = (
        f'font-size: 20px;'
    )

    line_horizontal_1 = (
        f'border-style: none;'
        f'border-bottom: 1px solid {ThemeColor.gray};'        
    )
    line_horizontal_2 = (
        #f'border-style: solid;'
        f'border: 1px solid {ThemeColor.secondary};'      
    )

    sidebar_button = (
        f'background-color: none;'
        f'border: none;'
        f'color: {ThemeColor.white};'
        f'text-align: left;'
        f'border-radius: 0px;'      
    )
    sidebar_button_active = sidebar_button + (
        f'background-color: {ThemeColor.primary};'        
        f'color: {ThemeColor.black};'     
    )
    sidebar_button_hover = sidebar_button + (
        f'background-color: {ThemeColor.black_midnight};'
    )

    sidebar_header_button = (
        f'background-color: none;'
        f'border: 0.5px solid {ThemeColor.gray};'
    )
    sidebar_header_button_hover = sidebar_header_button + (
        f'background-color: {ThemeColor.black_midnight};'
        f'border: 0.5px solid {ThemeColor.gray};'
    )
    sidebar_header_text = (
        f'color: {ThemeColor.white};'
        f'font-size: 18px;'       
    )

    