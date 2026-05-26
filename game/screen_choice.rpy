screen choice(items):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing
        for i in items:
            textbutton i.caption :
                padding (50, 5)
                idle_background "#000000b0"
                hover_background "#000000ff"
                selected_idle_background "#000000ff"
                insensitive_background "#000000b0"
                text_idle_color "#dddddd"
                text_hover_color "#ffffff"
                text_selected_color "#ffffff"
                text_insensitive_color "#888888"
                action i.action