sidebar_button = (
        #f'background-color: {ThemeColor.gray_3};'
        f'background-color: none;'
        f'border: none;'
        f'color: {ThemeColor.white};'
        f'text-align: left;'
        f'border-radius: 0px;'
        #f'border: 0.5px solid {ThemeColor.gray};'        
    )
    sidebar_button_active = sidebar_button + (
        f'background-color: {ThemeColor.primary};'        
        f'color: {ThemeColor.black};'   
        #f'border: 1px solid {ThemeColor.secondary};'     
    )
    sidebar_button_hover = sidebar_button + (
        #f'border: 1px solid {ThemeColor.secondary};'
        f'background-color: {ThemeColor.black_midnight};'
    )






sidebar_button = (
        f'background-color: {ThemeColor.gray_3};'        
        f'color: {ThemeColor.white};'
        f'text-align: left;'        
        f'border: 0.5px solid {ThemeColor.gray};'        
    )
    sidebar_button_active = sidebar_button + (
        f'background-color: {ThemeColor.primary};'        
        f'color: {ThemeColor.black};'   
        f'border: 1px solid {ThemeColor.primary};'     
    )
    sidebar_button_hover = sidebar_button + (
        f'border: 1px solid {ThemeColor.primary};'
        f'background-color: {ThemeColor.black_midnight};'
    )