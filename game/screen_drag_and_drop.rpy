default rope_hover = False
default is_dragging_rope = False
init python:
    def on_dragged_rope(drags, drop):
        store.is_dragging_rope = False
        renpy.restart_interaction()
    def on_dragging_rope(dragged_items):
        store.is_dragging_rope = True
        renpy.restart_interaction()
        if dragged_items[0].y >= -1050:
            renpy.jump("after_drag_rope")

screen church_drag_rope():
    drag:
        at church_after_drag_rop
        xpos 0
        ypos -1080
        dragging on_dragging_rope
        dragged on_dragged_rope
        drag_offscreen (0,-1661 , -1080, 0)
        if not is_dragging_rope :
            hovered SetVariable("rope_hover", True)
            unhovered SetVariable("rope_hover", False)
        if not is_dragging_rope and rope_hover:
            add "church/hover_rope.png" 
        else:
            add "church/rope.png" 

transform church_after_drag_rop:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 5 ypos -2000