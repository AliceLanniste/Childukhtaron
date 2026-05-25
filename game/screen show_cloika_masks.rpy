default cloika_masks_animation_stage = "zoom_to_left"

screen show_cloika_masks(frame_size = 6):
    $ w, h = renpy.image_size("other/cloika_masks.png")
    fixed :
        xalign 0.5
        yalign 0.5
        add Solid("#000000"):
            xalign 0.5
            yalign 0.5
            xsize w+frame_size*2
            ysize h+frame_size*2
        viewport:
            xalign 0.5
            yalign 0.5
            xsize w
            ysize h
            fixed:
                if cloika_masks_animation_stage == "zoom_to_left":
                    add "other/cloika_masks.png" at cloika_masks_animation_zoom_to_left
                elif cloika_masks_animation_stage == "zoom_to_right" :
                    add "other/cloika_masks.png" at cloika_masks_animation_zoom_to_right
                else:
                    add "other/cloika_masks.png" at cloika_masks_animation_right_to_reset


transform cloika_masks_animation_zoom_to_left():
    zoom 1.0
    linear 3.0 zoom 1.5 xpos 0 ypos -200
    zoom 1.5 xpos 0 ypos -200

transform cloika_masks_animation_zoom_to_right():
    zoom 1.5
    xpos 0 
    ypos -200
    linear 3.0 xpos -700
    xpos -700

transform cloika_masks_animation_right_to_reset():
    zoom 1.5
    xpos -700
    ypos -200
    linear 3.0 zoom 1.0 xpos 0 ypos 0
    zoom 1.0 xpos 0 ypos 0