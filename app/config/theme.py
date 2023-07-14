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
        /* SIDEBAR */
        #SidebarButton, #SidebarToggleButton{{
            {Style.sidebar_button()};
        }}        
        #SidebarToggleButton{{
            border: 0.5px solid {ThemeColor.gray};
            text-align: center;
        }}    
        #SidebarToggleButton:hover{{
            background-color: {ThemeColor.black_midnight};
        }}

        /* CONSOLE */ 
        #Console{{
            background-color: {ThemeColor.black_dark};
            border: none;
            font-family: "Courier New", monospace;
            font-size: 13px;
        }}

        /* PAGE */
        #Page QWidget{{
            background-color: transparent;             
        }}
        #Page{{
            background-color: {ThemeColor.black_midnight};        
            border: none;      
        }}
        #PageTitleLabel{{
            font-size: 16px;
            font-weight: bold;
            color: {ThemeColor.primary};
        }} 
        

        /* WIDGETS */
        #FancyTableTextEdit {{
            border: 1px solid {ThemeColor.gray_2};             
        }}    
        #FancyTableLabel {{
            font-size: 14px; 
            color: {ThemeColor.gray};            
        }}   
        #ChartView {{
            border: none;
        }}
        QFrame#StatCard{{            
            border: none;
        }} 
        #StatCardTitleLabel{{
            font-size: 12px;
            color: {ThemeColor.gray};   
        }}
        #StatCardTextLabel{{
            font-size: 18px;
            font-weight: bold;
            font-family: "Courier New", monospace;
            color: {ThemeColor.white};  
        }}
        #StatCardUnitLabel{{
            font-size: 12px;
            color: {ThemeColor.white_2};
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
        #DialogHeadingLabel{{
            font-weight: bold;
            font-size: 18px;
            color: {ThemeColor.white};
        }}

        /* OTHER LABELS */        
        #LabelWidgetTitle{{
            font-size: 14px;        
            color: {ThemeColor.secondary};
        }}
        #LabelHeading{{
            font-size: 22px;
            color: {ThemeColor.white};
        }}
        

        /* OTHER ELEMENTS */
        #LineHorizontal{{
            {Style.line_horizontal()};
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