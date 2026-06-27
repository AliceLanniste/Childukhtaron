#define character
define common_character_args = dict(
    ctc="ctc_icon"
)
define narrator = Character(what_outlines =gui.narrator_dialogue_outline,**common_character_args)
define tutor = Character("家庭教师",**common_character_args)
define player = Character("古尔",**common_character_args)
define rules = Character("舍规",image = "rules",**common_character_args)
define peter = Character("彼得",**common_character_args)
define sister = Character("修女",**common_character_args)
define clock = Character("钟表",**common_character_args)
define nun_trainee = Character("见习修女",**common_character_args)
define nun_mary = Character("玛利安",**common_character_args)
define hecate = Character("赫卡特",**common_character_args)
define player_and_peter = Character("古尔、彼得",**common_character_args)
define student_1 = Character("学生1",**common_character_args)
define student_2 = Character("学生2",**common_character_args)
define student_3 = Character("学生2",**common_character_args)
define prince = Character("王子",**common_character_args)
define young_lady = Character("少女",**common_character_args)
define robber = Character("强盗",**common_character_args)
define warrior = Character("骑士",**common_character_args)
define princess = Character("公主",**common_character_args)
define messenger = Character("神使",**common_character_args)

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

image ctc_icon:
    "ui/arrow.png"
    xoffset 10
    yoffset 5
    linear 0.35 yoffset 10
    linear 0.35 yoffset 5
    repeat


transform slow_zoom_statue():
    zoom 1.0
    xalign 0.05
    yalign 0.35
    linear 20 zoom 2

# 游戏在此开始。
label start:
    # jump test
    hide screen black_cover
    $ quick_menu = False
    call disclaimer

    $ quick_menu = True
    jump vol_0

    return

screen black_cover():
    add Solid("#000000") 
    zorder 100 

# 免责声明内容不应该把放于游戏内，应该放在游戏外。
label disclaimer:
    $ _skipping = False  # 禁用 Ctrl 快进
    
    stop music fadeout 1.0 
    scene black
    with Dissolve(1.0)

    # 此时 show screen 不再带有 modal，不会死锁引擎
    show screen show_text("游戏内出现的所有⼈物、宗教组织及事件，均与现实世界中的任何信仰、团体或个⼈⽆关。\n ⼀切设定仅为艺术创作，如有雷同，纯属巧合。")
    with Dissolve(2.0)
    
    # 正常的 pause 会在这里安全地等待 3 秒，玩家怎么点都没用
    $ renpy.pause(3.0) 
    
    hide screen show_text with Dissolve(2.0)
    
    show logo with Dissolve(2.0)
    play music "audio/05_amb_cicada_01.mp3" fadein(2)
    $ renpy.pause(3.0)
    hide logo with Dissolve(2.0)
    
    $ _skipping = True  # 恢复快进
    return

