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

#image bg
image bg cicada_1 = "bg/bg_cicada_1.png"
image bg cicada_2 = "bg/bg_cicada_2.png"
image bg room_past = "bg/bg_room_past.png"
image bg rules_stage = "bg/bg_rules_stage.png"
image bg awake = "bg/bg_awake.png"
image bg room_now = "bg/bg_room_now.png"
image bg view_form_far = "bg/bg_view_form_far.png"
image bg pool = "bg/bg_pool.png"
image bg bg_church = "bg/bg_church.png"
image bg statue_eyes = "bg/bg_statue_eyes.png"
image bg dark_red = "bg/bg_dark_red.png"
image bg rope = "bg/rope.png"
#image masks
image prince = "masks/prince.png"
image princess = "masks/princess.png"
image robber = "masks/robber.png"
image warrior = "masks/warrior.png"
image sister_mary = "masks/sister_mary.png"
image messenger = "masks/messenger.png"

#image other
image game_title = "other/bg_title.png"
image letter 1 = "other/letter_1.png"
image rules= "other/rules_1.png"
# image rules stage_loop_video = Movie(
#     play = "video/video_rules_stage.webm",
#     loops = -1)
image cloika_eye = Composite(
    (1651 + 2*20, 258 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_eye.png"
)
image cloika_masks = Composite(
    (1401 + 2*20, 812 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_masks.png"
)
image cloika_the_nun = Composite(
    (642 + 2*20, 973 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_the_nun.png"
)
image cloika_dancing_girls = Composite(
    (1530 + 2*20, 378 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_dancing_girls.png"
)
image cloika_she_coming p1 = Composite(
    (139 + 2*20, 942 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_she_coming_p1.jpg"
)
image cloika_she_coming p2 = Composite(
    (659 + 2*20, 942 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_she_coming_p2.jpg"
)
image cloika_wine_and_food = Composite(
    (1259 + 2*20, 475 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_wine_and_food.png"
)
image cloika_speech = Composite(
    (1259 + 2*20, 475 + 2*20),
    (0, 0), Solid("#000"),
    (20, 20), "other/cloika_speech.png"
)
default rope_drag_y = 0
default max_pull = 400

init python:
    def on_rope_dragged(draggable, *args):
        # drag_y 是相对于初始位置的偏移量
        # 我们限制最大值和最小值
        global rope_drag_y
        # 假设我们只允许向下拖，且最大拖 400
        rope_drag_y = max(0, min(draggable.drag_y, max_pull))
        renpy.notify("老大那个")
        # 如果需要松手后自动回弹或吸附，可以在这里写逻辑
        # 例如：if draggable.drag_y < 100: rope_drag_y = 0


define flash = Fade(0.05, 0.0, 0.1, color="#fff")
#transform
transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0

transform upper_fall:
    xalign 0.5 yalign 1.0
    ypos 1080 - (rope_drag_y / max_pull) * 1080  # 拖得越多，上图下落越多
    
# 定义血流向下的动画
transform blood_flow:
    # 初始位置在屏幕上方完全隐藏
    subpixel True
    yalign 0.0
    yoffset -1080 # 假设你的屏幕高度是1080
    
    # 模拟流下的过程
    easein 5.0 yoffset 1080 
    repeat

    
transform flicker_fix:
    # 闪黑
    matrixcolor BrightnessMatrix(-1.0)
    pause 0.1
    # 恢复
    matrixcolor BrightnessMatrix(0.0)
    pause 0.1
    # 重复执行上述逻辑 5 次
    repeat 5


# 游戏在此开始。
label start:
    # jump test
    jump vol_0

    return