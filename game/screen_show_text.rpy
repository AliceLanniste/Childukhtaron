screen show_text_slow_with_button(msg,cps = 8, font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    modal True

    button:
        xfill True
        yfill True
        # background Solid("#0008")
        action Return()

        text msg:
            xalign x_align
            yalign y_align
            textalign txt_align
            size font_size
            color font_color
            slow True 
            slow_cps cps


screen show_text_slow_with_duration(msg,duration = 3, cps = 8, font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    modal True

    text msg:
        xalign x_align
        yalign y_align
        textalign txt_align
        size font_size
        color font_color
        slow True 
        slow_cps cps
    timer duration action Return()


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
        

    
  