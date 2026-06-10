screen save():
    tag menu
    on "show" action FilePage(1)
    use file_slots(_("存档"))

screen load():
    tag menu
    # on "show" action FilePage(1)
    use file_slots(_("存档"))


screen file_slots(title):
    fixed:  
        add "ui/save/ui_save_bg_1.png"  # 底层主背景
      
    
    vbox :
        xpos 180
        ypos 260
        spacing 30
        # use save_and_load_button(title, )
        use save_and_load_button(title, FilePage(1))
        use save_and_load_button(_("设置"), ShowMenu("preferences"))
        # use save_and_load_button(_("设置"),ShowMenu("customePreferences"))
        # use save_and_load_button(_("自动"),FilePage("auto"))
        # use save_and_load_button(_("快速"),FilePage("quick"))
        # use save_and_load_button(_("返回"),Return())
        # use save_and_load_button(
        #     _("返回菜单"),
        #     Confirm("确定要返回主菜单吗？\n未保存的进度将会丢失。", Function(renpy.full_restart))
        # )
    add "ui/save/ui_save_bg_2.png"
    # add "ui/save/bg_menu_4-back.png"  # 
    imagebutton:
        idle "ui/save/bg_menu_4-back.png"
        hover "ui/save/bg_menu_4-back.png"
        action Return()

  
    grid gui.file_slot_cols gui.file_slot_rows:
        style_prefix "slot"
        xalign 0.6
        yalign 0.5
        spacing gui.slot_spacing
        for i in range(gui.file_slot_cols * gui.file_slot_rows):
            $ slot = i + 1
            button:
                action FileAction(slot)
            
                vbox:
                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                        color "#ffffff"
                        hover_color "#ff0000"
                        xalign 0.5 


                
screen save_and_load_button(title,button_action):
    textbutton title :
        xsize 555
        ysize 85
        xalign 0.5
        yalign 0.5
        text_xalign 0.4
        text_yalign 0.4
       
        idle_background "ui/save/ui_save_button_black.png"
        hover_background "ui/save/ui_save_button_black.png"
        selected_idle_background "ui/save/ui_save_button_red.png"  # 选中状态的红色背景
      
        text_style "save_load_button_text"
        action button_action



