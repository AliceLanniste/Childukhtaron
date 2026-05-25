screen show_image_with_frame(img,frame_size = 6,x_align = 0.5,y_align = 0.5):
    $ w, h = renpy.image_size(img)
    frame :
        background "#000000"
        xalign x_align
        yalign y_align
        xsize w+frame_size*2
        ysize h+frame_size*2
        add img :
            xalign 0.5
            yalign 0.5