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


class Style:    
    def custom_style():
        style = (f''' 
        /* GUI COMPONENTS */ 
        #Console{{
            background-color: {ThemeColor.black_dark};
            border: none;
            font-family: "Courier New", monospace;
            font-size: 13px;
        }}
        #Page QWidget{{
            background-color: {ThemeColor.black_midnight};        
            border: none;      
        }}

        /* SIDEBAR */
        #SidebarButton, #SidebarToggleButton{{
            {Style.sidebar_button()}
        }}        
        #SidebarToggleButton{{
            border: 0.5px solid {ThemeColor.gray};
            text-align: center;
        }}    
        #SidebarToggleButton:hover{{
            background-color: {ThemeColor.black_midnight};
        }}

        /* WIDGETS */
        #Table {{
            background-color: transparent; 
            alternate-background-color: {ThemeColor.gray_3}; 
        }}

        /* DIALOGS */
        #DialogOverlay {{
            background-color: rgba(78, 87, 95, 0.3);
        }}
        #DialogContainer {{
            border: 2px solid {ThemeColor.gray};
        }}
        #DialogProgressBar {{
            border: 1px solid {ThemeColor.secondary};
        }}

        /* LABELS */
        #LabelPageTitle{{
            font-size: 16px;
            font-weight: bold;
            color: {ThemeColor.primary};
        }} 
        #LabelWidgetTitle{{
            font-size: 14px;            
            color: {ThemeColor.secondary};
        }}
        #LabelHeading{{
            font-size: 22px;
            color: {ThemeColor.white};
        }}
        #LabelDialogHeading{{
            font-weight: bold;
            font-size: 18px;
            color: {ThemeColor.white};
        }}

        /* OTHER ELEMENTS */
        #LineHorizontal{{
            {Style.line_horizontal()}
        }}
        ''')
        return style
    
    def line_horizontal(color=ThemeColor.gray, width=1):
        style = f'''
            border-style: none;
            border-bottom: {width}px solid {color};
        '''
        return style

    def sidebar_button(active=False, hover=False): 
        background = 'transparent'
        color = ThemeColor.white                

        if hover:
            background = ThemeColor.black_midnight
        elif active:
            background = ThemeColor.primary
            color = ThemeColor.black            

        style = f'''
        background-color: {background};
        color: {color};
        border: none;            
        text-align: left;
        border-radius: 0px;
        '''
        return style