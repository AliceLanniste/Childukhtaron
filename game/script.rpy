

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

            action ShowMenu('save')
            add "ui/save/logo_menu_enter.png"

transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0

# 游戏在此开始。
label start:
    # jump test
    jump vol_0

    return