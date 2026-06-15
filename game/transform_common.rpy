transform fade_with_show_and_hide(duration_show = 1.0, duration_hide = 1.0):
    on show:
        alpha 0.0
        linear duration_show alpha 1.0
    on hide:
        linear duration_hide alpha 0

transform fade_with_pause_show_and_hide(duration_pause = 1.0, duration_show = 1.0, duration_hide = 1.0):
    on show:
        alpha 0.0
        pause duration_pause
        linear duration_show alpha 1.0
    on hide:
        linear duration_hide alpha 0