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

#image other
image rules= "other/rules_1.png"
image rules stage_loop_video = Movie(
    play = "video/video_rules_stage.webm",
    loops = -1)
image cloika_eye = "other/cloika_eye.png"
image letter 1 = "other/letter_1.png"
image cloika_masks = "other/cloika_masks.png"
image cloika_the_nun = "other/cloika_the_nun.png"
image cloika_she_coming p1 = "other/cloika_she_coming_p1.jpg"
image cloika_she_coming p2 = "other/cloika_she_coming_p2.jpg"
image cloika_wine_and_food = "other/cloika_wine_and_food.png"
image cloika_speech = "other/cloika_speech.png"
image game_title = "other/bg_title.png"

#image bg
image bg cicada_1 = "bg/bg_cicada_1.png"
image bg cicada_2 = "bg/bg_cicada_2.png"
image bg room_past = "bg/bg_room_past.png"
image bg rules_stage = "bg/bg_rules_stage.png"
image bg awake = "bg/bg_awake.png"
image bg room_now = "bg/bg_room_now.png"
image bg view_form_far = "bg/bg_view_form_far.png"
image bg pool = "bg/bg_pool.png"

image bg church = "bg/bg_church.png"
image bg statue_eyes = "bg/bg_statue_eyes.png"
image bg dark_red = "bg/bg_dark_red.png"

#transform
transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0

# 游戏在此开始。
label start:
    jump test
    # jump vol_0

    return