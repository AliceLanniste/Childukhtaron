

#image bg
image bg cicada_1 = "bg/bg_cicada_1.png"
image bg cicada_2 = "bg/bg_cicada_2.png"
image bg room_past = "bg/bg_room_past.png"
image bg rules_stage = "bg/bg_rules_stage.png"
image bg awake = "bg/bg_awake.png"
image bg room_now = "bg/bg_room_now.png"
image bg view_form_far = "bg/bg_view_form_far.png"
image bg pool = "bg/bg_pool.png"

image bg statue_eyes = "bg/bg_statue_eyes.png"

#image church
image bg church = "church/bg_church.png"
image rope = "church/rope.png"
image curtain_left = "church/curtain_left.png"
image curtain_right = "church/curtain_right.png"

image bg statue_eyes = "bg/bg_statue_eyes.png"
image bg dark_red = "bg/bg_dark_red.png"

#image other
image dark_red = "other/dark_red.png"
image game_title_start = "other/bg_title.png"
image game_title_fin = "other/bg_title_fin.png"
image letter 1 = "other/letter_1.png"
image rules= "other/rules_1.png"
image disclaimer_logo_img ="ui/save/logo.png"

# 1. 定义浮动动画
transform ctc_bounce:
    yalign 0.5
    block:
        linear 0.4 yoffset -8  # 向上浮动 6 像素
        linear 0.4 yoffset 6   # 回到原位
        repeat

# 2. 将图片和动画绑定
image ctc_arrow:
    "ui/save/arrow.png"  # 请确保这个路径正确
    ctc_bounce




#define character
define tutor = Character("家庭教师",ctc="ctc_arrow", ctc_position="nestled")
define player = Character("古尔",ctc="ctc_arrow", ctc_position="nestled")
define rules = Character("舍规",image = "rules",ctc="ctc_arrow", ctc_position="nestled")
define peter = Character("彼得",ctc="ctc_arrow", ctc_position="nestled")
define sister = Character("修女",ctc="ctc_arrow", ctc_position="nestled")
define clock = Character("钟表",ctc="ctc_arrow", ctc_position="nestled")
define nun_trainee = Character("见习修女",ctc="ctc_arrow", ctc_position="nestled")
define nun_mary = Character("玛利安",ctc="ctc_arrow", ctc_position="nestled")
define hecate = Character("赫卡特",ctc="ctc_arrow", ctc_position="nestled")
define narrator = Character(what_outlines =gui.narrator_dialogue_outline)

screen menu_icon:
    zorder 100
    if not main_menu and quick_menu:
        button:
            xalign 0.98  
            yalign 0.02  

            action ShowMenu("load")
            add "ui/save/logo_menu_enter.png"

transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0

# 游戏在此开始。
label start:
    jump test
    $ quick_menu = False
    call disclaimer

    $ quick_menu = True
    # jump vol_0

    return

# 免责声明内容不应该把放于游戏内，应该放在游戏外。
label disclaimer:
    # 隐藏默认的对话框背景，让画面更干净
    window hide 
    
    # 显示文字：
    # 1. 使用 Text 创建文本对象，设置白色、大小和居中
    # 2. 应用我们刚才定义的 cinematic_text 动画
    show expression Text(
        "游戏内出现的所有⼈物、宗教组织及事件，均与现实世界中的任何信仰、团体或个⼈⽆关。\n⼀切设定仅为艺术创作，如有雷同，纯属巧合。", 
        color="#fff", 
        size=36, 
        text_align=0.5,  # 文本内容居中对齐
        layout="subtitle" # 自动换行处理
    ) at cinematic_text as disclaimer_text
    
    # 等待动画播放完毕（1.5 + 3.0 + 1.5 = 6秒）
    # 如果你想让玩家随时可以点击跳过，可以改为：
    # $ renpy.pause(hard=False) 
    pause 6.0 
    
    # 动画结束后，彻底隐藏该文字
    hide  disclaimer_text

    show expression "ui/save/logo.png" at cinematic_text as disclaimer_logo
    pause 6.0  # 等待 Logo 动画播放完毕
    hide disclaimer_logo
    
    # 恢复对话框
    window show

    # 返回到调用它的地方
    return


transform cinematic_text:
    # 1. 初始状态：完全透明，位于屏幕正中间
    alpha 0.0
    align (0.5, 0.5) 
    
    # 2. 渐显 (1.5秒)
    linear 1.5 alpha 1.0
    
    # 3. 停留 (3秒)
    pause 3.0
    
    # 4. 渐隐 (1.5秒)
    linear 1.5 alpha 0.0