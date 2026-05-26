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
        idle_background "#000000b0"
        hover_background "#000000ff"
        selected_idle_background "#000000ff"
        insensitive_background "#000000b0"
        text_idle_color "#dddddd"
        text_hover_color "#ffffff"
        text_selected_color "#ffffff"
        text_insensitive_color "#888888"
        action btn_action
