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
image bg dark_red = "bg/bg_dark_red.png"

#image church
image bg church = "church/bg_church.png"
image rope = "church/rope.png"
image curtain_left = "church/curtain_left.png"
image curtain_right = "church/curtain_right.png"

image bg statue_eyes = "bg/bg_statue_eyes.png"
image bg dark_red = "bg/bg_dark_red.png"

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

transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0


# 定义带自动打字效果的 NVL 叙述者（cps=20 代表每秒显示20个字）
define nvl_narrator = Character(None, kind=nvl, cps=20)

# 配置 NVL 窗口和文字的样式
style nvl_window:
    xfill True
    yfill True
    background None  # 透明背景

style nvl_text:
    outlines [(4, "#00362e", 0, 0)]  # 深绿色描边
    size 33
    line_leading -10
    color "#ffffff"  # 白色文字
    
    # 核心改动：设置文字水平、垂直居中，并指定 ypos 保持和你最初的位置一致
    text_align 0.5   # 文本块内部水平居中
    xalign 0.5       # 文本块在屏幕水平居中
    ypos 950         # 这里对应你最初代码里的 850，如果某些句子是 900 可以按需调整
    xpos 950


# 游戏在此开始。
label start:
    # jump test
    jump vol_0

    return