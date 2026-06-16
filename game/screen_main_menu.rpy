init python:
    def has_any_save():
        return len(renpy.list_saved_games()) > 0
screen main_menu():

    ## 此语句可确保替换掉任何其他菜单屏幕。
    tag menu

    add gui.main_menu_background

    if gui.show_name:

        vbox:
            xalign 0.5
            yalign 0.9
            spacing 10
            use main_menu_button("进入山谷",Start())
            if has_any_save():
                use main_menu_button("你的随笔",ShowMenu("load"))
            use main_menu_button("离开山谷",Quit(confirm=not main_menu))

            text "关于《奇尔杜克塔伦山谷》":
                size gui.title_text_size
                color "#dddddd"
                xalign 0.5

            text "v[config.version]":
                color "#dddddd"
                xalign 0.5

screen main_menu_button(txt,btn_action):
    textbutton txt:
        padding (150, 10)
        idle_background gui.choice_button_idle_background_color
        hover_background gui.choice_button_hover_background_color
        selected_idle_background gui.choice_button_selected_idle_background_color
        insensitive_background gui.choice_button_insensitive_background_color
        text_idle_color gui.choice_button_text_idle_color
        text_hover_color gui.choice_button_text_hover_color
        text_selected_color gui.choice_button_text_hover_color
        text_insensitive_color gui.choice_button_text_insensitive_color
        action btn_action