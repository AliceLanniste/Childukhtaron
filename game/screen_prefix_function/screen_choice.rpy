screen choice(items):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing
        for i in items:
            textbutton i.caption :
                padding (50, 5)
                idle_background gui.choice_button_idle_background_color
                hover_background gui.choice_button_hover_background_color
                selected_idle_background gui.choice_button_selected_idle_background_color
                insensitive_background gui.choice_button_insensitive_background_color
                text_idle_color gui.choice_button_text_idle_color
                text_hover_color gui.choice_button_text_hover_color
                text_selected_color gui.choice_button_text_hover_color
                text_insensitive_color gui.choice_button_text_insensitive_color
                action i.action