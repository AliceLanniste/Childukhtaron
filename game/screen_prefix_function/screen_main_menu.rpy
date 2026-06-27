init python:
    def has_any_save():
        return len(renpy.list_saved_games()) > 0
screen main_menu():

    ## 此语句可确保替换掉任何其他菜单屏幕。
    tag menu

    add gui.main_menu_background
    add gui.game_menu_title at fade_in
    if gui.show_name:

        hbox:
            xalign 0.5              # 水平居中
            yalign 0.7             # 垂直位置
            spacing 200              # 按钮之间的水平间距（像素）
            use main_menu_button("进入山谷",Start())
            if has_any_save():
                use main_menu_button("你的随笔",ShowMenu("load"))
            use main_menu_button("离开山谷",Quit(confirm=not main_menu))

        hbox:
            xalign 1.0
            yalign 1.0
            spacing 10
            # text "关于《奇尔杜克塔伦山谷》":
                # size gui.title_text_size
                # color "#dddddd"
            text "v[config.version]":
                color "#dddddd"

screen main_menu_button(txt,btn_action):
    textbutton txt:
        padding (80, 5)
        idle_background gui.choice_button_idle_background_color
        hover_background gui.choice_button_hover_background_color
        selected_idle_background gui.choice_button_selected_idle_background_color
        insensitive_background gui.choice_button_insensitive_background_color
        text_idle_color gui.choice_button_text_idle_color
        text_hover_color gui.choice_button_text_hover_color
        text_selected_color gui.choice_button_text_hover_color
        text_insensitive_color gui.choice_button_text_insensitive_color
        action btn_action

        activate_sound "audio/ui/02-ui-choose-0.ogg"           
        hovered Play("sound", "audio/ui/02-ui-choose.ogg") 

screen menu_icon:
    zorder 100
    if not main_menu and quick_menu:
        imagebutton:
            xalign 0.999 
            yalign 0.001  
            
            activate_sound "audio/ui/01-ui-book open(2).ogg"
            action [ ShowMenu("")] 
            hovered Play("sound", "audio/ui/02-ui-choose.ogg")
              
            idle "ui/save/logo_menu_enter.png" 
            hover "ui/save/logo_menu_enter_hover.png"     
           