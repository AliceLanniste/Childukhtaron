init python:
    def on_dragging_rope(dragged_items):
        if dragged_items[0].y >= -1000:
            renpy.jump("after_drag_rope")

screen church_drag_rope():
    drag:
        xpos 0
        ypos -1500
        image "church/rope.png"
        drag_name "drag test!"
        dragging on_dragging_rope
        drag_offscreen (0,-1766 , -1500, 0) 