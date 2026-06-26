screen show_image_with_frame(img,frame_size = 6,x_align = 0.5,y_align = 0.5):
    frame :
        background "#000000"
        xalign x_align
        yalign y_align
        padding (frame_size, frame_size)
        add img :
            xalign 0.5
            yalign 0.5

screen show_image_with_frame_and_fade(img,frame_size = 6,x_align = 0.5,y_align = 0.5,duration_show = 1.0,duration_hide = 1.0,alpha_max = 1.0):
    frame :
        at fade_with_show_and_hide(duration_show,duration_hide,alpha_max)
        background "#000000"
        xalign x_align
        yalign y_align
        padding (frame_size, frame_size)
        add img :
            xalign 0.5
            yalign 0.5


screen show_image_with_frame_and_quick_fade(img,frame_size = 6,x_align = 0.5,y_align = 0.5,duration_show = 1.0,duration_hide = 1.0,alpha_max = 1.0):
    frame :
        at fade_with_show_and_quick_hide(duration_show,duration_hide,alpha_max)
        background "#000000"
        xalign x_align
        yalign y_align
        padding (frame_size, frame_size)
        add img :
            xalign 0.5
            yalign 0.5
