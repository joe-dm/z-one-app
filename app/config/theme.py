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
    # test widget
    test_widget = (
        f'border: 1px solid {ThemeColor.secondary};'
    )

    # widgets styles
    cpu_monitor = (
        f'''        
        QLabel#HeadingTitle {{
            font-size: 20px;    
            color: {ThemeColor.white};
        }}
        QLabel#HeadingAltText {{
            font-size: 12px;            
            color: {ThemeColor.gray};
            qproperty-alignment: 'AlignRight | AlignBottom';            
        }}
        '''  
    )    

    # console styles
    console = (
        f'background-color: {ThemeColor.black_dark};'
        f'border:none;'
        f'font-family: "Courier New", monospace;'
        f'font-size: 13px;'
    )    

    # dialog styles    
    dialog = (
        f'''
        EmbeddedDialog {{
            background-color: rgba(78, 87, 95, 0.3);
        }}
        QWidget#DialogContainer {{
            border: 2px solid {ThemeColor.gray};
        }}
        '''    
    )
    dialog_heading = (
        f'font-weight: bold;'
        f'font-size: 18px;'
        f'color: {ThemeColor.white};'
    )    

    # graph styles
    chart = (
        f'''
        QLabel#GraphTitle {{
            font-size: 14px;            
            color: {ThemeColor.white_2};
        }}
        QLabel#GraphMax {{
            font-size: 12px;
            color: {ThemeColor.gray}; 
            qproperty-alignment: 'AlignRight | AlignBottom';           
        }}
        '''   
    )
    # table styles    
    table = (
        f'''        
        QTableWidget {{              
            background-color: transparent; 
            alternate-background-color: {ThemeColor.gray_3};                              
        }}        
        '''
    )

    # page styles    
    page_stack = (
        f'background-color: {ThemeColor.black_midnight};'
        f'border: none;'         
    )
    page = (
        f'''
        QLabel#PageTitle {{
            font-size: 16px;
            font-weight: bold;
            color: {ThemeColor.primary};
        }}               
        '''  
    )    

    # labels
    label_heading = (
        f'font-size: 18px;'
        f'color: {ThemeColor.white};'
    )
    label_table_title = (
        f'font-size: 18px;'
        f'color: {ThemeColor.white};'
    )

    # lines
    line_horizontal_1 = (
        f'border-style: none;'
        f'border-bottom: 1px solid {ThemeColor.gray};'
    )

    # progress bars
    progress_bar = (
        f'border: 1px solid {ThemeColor.secondary};'
    )

    # sidebar styles
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
        f'border-radius: 0px;' 
    )
    sidebar_header_button_hover = sidebar_header_button + (
        f'background-color: {ThemeColor.black_midnight};'
        f'border: 0.5px solid {ThemeColor.gray};'
    )
    sidebar_header_text = (
        f'color: {ThemeColor.white};'
        f'font-size: 18px;'       
    )

    