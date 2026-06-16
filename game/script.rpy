#define character
define tutor = Character("家庭教师")
define player = Character("古尔")
define rules = Character("舍规",image = "rules")
define peter = Character("彼得")
define sister = Character("修女")
define clock = Character("钟表")
define nun_trainee = Character("见习修女")
define nun_mary = Character("玛利安")
define hecate = Character("赫卡特")
define narrator = Character(what_outlines =gui.narrator_dialogue_outline)

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
image game_title_finnal = "other/bg_title_fin.png"

image letter 1 = "other/letter_1.png"
image rules= "other/rules_1.png"
image logo = "other/logo.png"
image white = "other/bg_white.png"




transform slow_zoom_statue():
    zoom 1.0
    xalign 0.05
    yalign 0.35
    linear 20 zoom 2
# 游戏在此开始。
label start:
    # jump test
    jump vol_0

    return