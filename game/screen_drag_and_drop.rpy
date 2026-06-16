init python:
    def on_dragging_rope(dragged_items):
        if dragged_items[0].y >= -980:
            renpy.jump("after_drag_rope")

screen church_drag_rope():
    drag:
        at church_after_drag_rop
        xpos 0
        ypos -1080
        image "church/rope.png" 
        dragging on_dragging_rope
        drag_offscreen (0,-1661 , -1080, 0)

transform church_after_drag_rop:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 5 ypos -2000