screen save():
    tag menu
    on "show" action FilePage(1)
    use file_slots(_("保存"))

screen load():
    tag menu
    on "show" action FilePage(1)
    use file_slots(_("读取"))

screen file_slots(title):
    add "ui/save/ui_save_bg_1.png"
    textbutton _("返回"):
        background "#0000005d"
        action Return()
    vbox :
        xpos 30
        ypos 260
        spacing 30
        use save_and_load_button(title,FilePage(1))
        use save_and_load_button(_("自动"),FilePage("auto"))
        use save_and_load_button(_("快速"),FilePage("quick"))
    add "ui/save/ui_save_bg_2.png"

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
                        color "#000000"
                        xalign 0.5 
                
screen save_and_load_button(title,button_action):
    textbutton title :
        xsize 700
        ysize 89
        xalign 0.5
        yalign 0.5
        text_xalign 0.5
        text_yalign 0.5
        background "ui/save/ui_save_button.png"
        action button_action