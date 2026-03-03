screen show_text_on_center(msg,cps = 8, font_size = 72, font_color = "#912020"):
    modal True  # 防止点到下面的UI

    button:
        xfill True
        yfill True
        action Return()

        text msg:
            xalign 0.5
            yalign 0.5
            textalign 0.5
            size font_size
            color font_color
            slow True 
            slow_cps cps


screen centered_text_screen(msg, ypos):
    modal True

    button:
        xfill True
        yfill True
        action Return()
    
    text msg:
        text_align 0.5
        xalign 0.5
        ypos ypos
        #样式美化
        outlines [(4,"#00362e",0,0)]
        size 33
        line_leading -10
        

    
  