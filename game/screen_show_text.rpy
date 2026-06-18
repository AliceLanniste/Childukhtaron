screen show_text_slow_with_button(msg,cps = 8, font_size = 32, font_color = "#ffffff",x_align = 0.5, y_align = 0.5,txt_align = 0.5):
    modal True

    button:
        xfill True
        yfill True
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

#图像渐显
transform bg_fade_in:
    alpha 0.0
    delay 3.0
    linear 1.0 alpha 1.0
#图像渐失
transform bg_fade_out:
    alpha 1.0
    delay 3.0
    linear 1.0 alpha 0.0
    # 2. 定义文字渐显动画 (延迟1秒开始，1秒内完全显示)
transform text_fade_in:
    alpha 0.0
    delay 1.0  # 等待背景动画完成后再开始
    linear 1.0 alpha 1.0
screen show_text_with_frame(msg,font_size = 32,font_color = "#ffffff", frame_size_x = 1080, frame_size_y = 1080,text_x_align = 0.5, text_y_align = 0.5,txt_align = 0.5,l_spacing= 30):
    modal True
    # 1. 定义背景渐显动画 (0秒开始，1秒内完全显示)
   

    button:
        xsize frame_size_x
        ysize frame_size_y
        xalign 0.5
        yalign 0.5
        background Solid("#0008") at bg_fade_in
        action Return()

        text msg:
            xalign text_x_align
            yalign text_y_align
            textalign txt_align
            size font_size
            color font_color
            line_spacing l_spacing
            at text_fade_in