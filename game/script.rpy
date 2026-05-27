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

#image masks
image prince = "masks/prince.png"
image princess = "masks/princess.png"
image robber = "masks/robber.png"
image warrior = "masks/warrior.png"
image sister_mary = "masks/sister_mary.png"
image messenger = "masks/messenger.png"

#image other
image dark_red = "other/dark_red.png"
image game_title = "other/bg_title.png"
image letter 1 = "other/letter_1.png"
image rules= "other/rules_1.png"

define RULES_ANIMATION_SPEED = 0.2
image rules stage_loop_animation:
    "animation/rule/rule_1.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_2.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_3.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_4.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_5.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_6.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_7.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_8.png"
    pause RULES_ANIMATION_SPEED
    "animation/rule/rule_9.png"
    pause RULES_ANIMATION_SPEED
    repeat

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