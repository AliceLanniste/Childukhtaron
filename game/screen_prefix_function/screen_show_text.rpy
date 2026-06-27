screen show_text(msg,font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    # modal True

    text msg:
        xalign x_align
        yalign y_align
        textalign txt_align
        size font_size
        color font_color

screen show_text_slow_with_button(msg,cps = 8, font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    modal True

    button:
        xfill True
        yfill True
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

screen show_text_with_frame(msg,font_size = 32,font_color = "#ffffff", frame_size_x = 1080, frame_size_y = 1080,text_x_align = 0.5, text_y_align = 0.5,txt_align = 0.5,l_spacing= 30):
    modal True

    button:
        at fade_with_show_and_hide(1,1)
        xsize frame_size_x
        ysize frame_size_y
        xalign 0.5
        yalign 0.5
        background Solid("#0008")
        action Return()
    text msg:
        at fade_with_pause_show_and_hide(1,1,1)
        xalign text_x_align
        yalign text_y_align
        textalign txt_align
        size font_size
        color font_color
        line_spacing l_spacing

