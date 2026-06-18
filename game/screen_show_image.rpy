screen show_image_with_frame(img, frame_size=6, x_align=0.5, y_align=0.5, fade_out=False):
    # 如果传入了 fade_out=True，就在整个 frame 上应用渐隐动画
    $ current_transform = bg_fade_out if fade_out else None
    frame:
        at current_transform
        
        background "#000000"
        xalign x_align
        yalign y_align
        padding (frame_size, frame_size)
        
        add img:
            xalign 0.5
            yalign 0.5

    # 如果是渐隐模式，1秒后自动关闭屏幕
    if fade_out:
        timer 1.0 action Return()