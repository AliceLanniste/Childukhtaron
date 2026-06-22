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
define warrior = Character("武士",**common_character_args)
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
    yoffset 0
    linear 0.5 yoffset 5
    linear 0.5 yoffset 0
    repeat