screen save():
    tag menu
    use file_slots(_("存档"))

screen load():
    tag menu
    use file_slots(_("存档"))

screen custom_navigation():

    vbox:
        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

     
        use save_and_load_button(_("存档"), ShowMenu("load"))
        use save_and_load_button(_("设置"), ShowMenu("custom_preferences"))
        use save_and_load_button(_("历史"), ShowMenu("custom_history"))
        use save_and_load_button(_("返回"), Return())
        use save_and_load_button(_("返回菜单"), ShowMenu("main_menu"))

screen background_menu(title="",scroll=None, yinitial=0.0, spacing=0):
    # 底层主背景
    fixed:  
        add "ui/save/ui_save_bg_1.png"
    
    # 左侧导航按钮
    vbox:
        xpos 180
        ypos 260
        spacing 30
        use custom_navigation

    add "ui/save/ui_save_bg_2.png"

    frame:
        
        style "game_menu_content_frame"

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                # scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    spacing spacing

                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial yinitial

                # scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                spacing spacing

                transclude

        else:

            transclude
        
    
  
   
    
    # # 返回按钮
    # imagebutton:
    #     idle "ui/save/bg_menu_4-back.png"
    #     hover "ui/save/bg_menu_4-back.png"
    #     action ShowMenu("main_menu") 

screen file_slots(title):
    # 调用公共背景界面
    use background_menu(title)
    
    # 存档槽位网格
    grid gui.file_slot_cols gui.file_slot_rows:
        style_prefix "slot"
        xalign 0.6
        yalign 0.5
        spacing gui.slot_spacing
        for i in range(gui.file_slot_cols * gui.file_slot_rows):
            $ slot = i + 1
            button:
                action FileAction(slot)
                alternate FileDelete(slot)  # 右键删除
                
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
        # hover_background "ui/save/ui_save_button_black.png"
        selected_idle_background "ui/save/ui_save_button_red.png"  # 选中状态的红色背景
      
        text_style "save_load_button_text"
        action button_action

# screen custom_preferences():
#     tag menu
    
#     # 调用公共背景界面，这里不显示左侧第一个标题按钮
#     use background_menu("")
    
#     # 下面是你原本设置界面的内容（请根据你实际的设置代码补充）
#     # 建议放在一个 viewport 或者 fixed 中，并设置合适的 xpos 和 ypos
#     # 例如：


#     fixed:
#         # 3. 核心居中代码：将内部的 vbox 整体放置在屏幕正中央
#         vbox:
#             align (0.5, 0.5)  # 等价于 xalign 0.5 和 yalign 0.5
#             spacing 30        # 上下元素之间的间距

#             hbox:
#                 style_prefix "slider"
                
                
#                 vbox:
                  
                
#                     label _("文字速度")
#                     bar value Preference("text speed")

#                     if config.has_music:
#                         label _("音乐音量")
#                         bar value Preference("music volume")
                    
#                     if config.has_sound:
#                         label _("音效音量")
#                         bar value Preference("sound volume")
#                         if config.sample_sound:
#                             textbutton _("测试") action Play("sound", config.sample_sound)

#                     if config.has_voice:
#                         label _("语音音量")
#                         bar value Preference("voice volume")
#                         if config.sample_voice:
#                             textbutton _("测试") action Play("voice", config.sample_voice)

# screen custom_preferences():
#     tag menu
    
#     # 调用公共背景界面
#     use background_menu("")
    
#     fixed:
#         vbox:
#             align (0.5, 0.5)  # 整体居中
#             spacing 30        # 每一行之间的间距
#             style_prefix "slider"  # 统一应用滑块样式
            
#             # 【文字速度】
#             hbox:
#                 spacing 20  # label 和 bar 之间的间距
#                 yalign 0.5  # 确保同行元素垂直居中对齐
#                 label _("文字速度"):
#                     xsize 200
#                     text_align 1.0 # 文字靠右显示，紧贴进度条
#                     yalign 0.5  # 确保文字自身也是垂直居中的
#                 bar value Preference("text speed")

#             # 【音乐音量】
#             if config.has_music:
#                 hbox:
#                     spacing 20
#                     yalign 0.5
#                     label _("音乐音量")
#                     bar value Preference("music volume")
                
#             # 【音效音量】
#             if config.has_sound:
#                 hbox:
#                     spacing 20
#                     yalign 0.5
#                     label _("音效音量")
#                     bar value Preference("sound volume")
#                     if config.sample_sound:
#                         textbutton _("测试") action Play("sound", config.sample_sound)

#             # 【语音音量】
#             if config.has_voice:
#                 hbox:
#                     spacing 20
#                     yalign 0.5
#                     label _("语音音量")
#                     bar value Preference("voice volume")
#                     if config.sample_voice:
#                         textbutton _("测试") action Play("voice", config.sample_voice)


screen custom_preferences():
    tag menu

    # 调用公共背景界面
    use background_menu("")

    fixed:
        vbox:
            align (0.5, 0.5)  # 整体居中
            spacing 30        # 每一行之间的间距
            style_prefix "slider"

            # 【文字速度】
            hbox:
                spacing 20      # 文字和进度条的间距

                label _("文字速度")
                bar value Preference("text speed")
                   

            # 【音乐音量】
            if config.has_music:
                hbox:
                    spacing 20
                    label _("音乐音量")
                    
                    bar value Preference("music volume")

            # 【音效音量】
            if config.has_sound:
                hbox:
                    spacing 20
                    label _("音效音量")
                       
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("测试") action Play("sound", config.sample_sound)

            # 【语音音量】
            if config.has_voice:
                hbox:
                    spacing 20
                    label _("语音音量")
                      
                      
                        
                    bar value Preference("voice volume")
                    if config.sample_voice:
                        textbutton _("测试") action Play("voice", config.sample_voice)

screen custom_history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    use background_menu("", scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果 history_height 为 None 时仍可正常显示条目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置
                        ## 了的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("尚无对话历史记录。")

