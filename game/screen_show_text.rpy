screen show_text_slow_with_button(msg,cps = 8, font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    modal True

    button:
        xfill True
        yfill True
        # background Solid("#0008")
        action Return()

        text msg:
            xalign x_align
            yalign y_align
            textalign txt_align
            size font_size
            color font_color
            slow True 
            slow_cps cps


screen show_text_slow_with_duration(msg,duration = 3, cps = 8, font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    modal True

    text msg:
        xalign x_align
        yalign y_align
        textalign txt_align
        size font_size
        color font_color
        slow True 
        slow_cps cps
    timer duration action Return()


screen centered_text_screen(msg, ypos, auto_return_time=3.0):
    modal True

    # 添加计时器，经过 auto_return_time 秒后自动执行 Return() 返回，显示下一句
    timer auto_return_time action Return()

    button:
        xfill True
        yfill True
        action Return()
    
    text msg:
        text_align 0.5
        xalign 0.5
        ypos ypos
        # 样式美化
        outlines [(4,"#00362e",0,0)]
        size 33
        line_leading -10
    
# 1. 先在外部定义好背景缓慢放大的动画
transform bg_zoom_in(zoom_duration):
    align (0.5, 0.5)
    zoom 1.0
    linear zoom_duration zoom 2.0 

# 在 scene.rpy 中添加这个整合界面
screen auto_show_screen(bg_name, dialogue_list, text_interval=3.0, zoom_duration=20.0):
    modal True  # 如果希望播放时玩家不能点击屏幕，就取消这行的注释
    zorder 100

    # 1. 播放背景图，并附加缓慢放大的动画 (zoom_transform)
    add bg_name at bg_zoom_in(zoom_duration)

    # 2. 文字自动轮播逻辑
    default current_index = 0

    # 计时器：每隔 text_interval 秒，自动显示下一句话
    timer text_interval:
        repeat True
        action If(
            current_index < len(dialogue_list) - 1,
            true=SetScreenVariable("current_index", current_index + 1),
            false=Return()
        )

    # 3. 渲染 NVL 样式的文字 (保持你之前设计的居中描边样式)
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
            $ text_content = dialogue_list[current_index]
            text text_content:
                style "nvl_text"
