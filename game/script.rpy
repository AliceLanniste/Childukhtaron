#角色定义
define player = Character("男主")
define rules = Character("舍规")
define clock = Character("钟表")
define peter = Character("皮特")
define nun_trainee = Character("见习修女")
define nun_mary = Character("修女玛丽")
define nuns = Character("神女们")

#角色立绘定义
image rules stage_lighting = "character/rules/rules_stage_lighting.png"
image rules humming = "character/rules/rules_humming.png"

image clock twist = "character/clock/clock_twist.png"

#BG定义
image bg cicada = "bg/bg_cicada.jpg"
image bg dark_black = "bg/bg_dark_black.png"
image bg room_now = "bg/bg_room_now.jpg"
image bg room_past = "bg/bg_room_past.jpg"
image bg room_past_twist = "bg/bg_room_past_twist.jpg"
image bg rules = "bg/bg_rules.jpg"
image bg awake = "bg/bg_awake.jpg"

image bg masks = "bg/bg_masks.png"
image bg pool = "bg/bg_pool.jpg"
image bg view_form_far = "bg/bg_view_form_far.png"
image bg she_coming = "bg/bg_she_coming.png"
image bg statue_eyes = "bg/bg_statue_eyes.png"

#以下为缺失BG
image bg invitation_letter_unopened = "bg/bg_invitation_letter_unopened.png"
image bg invitation_letter_opened = "bg/bg_invitation_letter_opened.png"
image bg church_inside_full_shot = "bg/bg_church_inside_full_shot.png"
image bg statue_and_table = "bg/statue_and_table.png"

#其它image
image black_circle = Solid("#000")

#transform定义
transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0

# 游戏在此开始。
label start:
    jump opening_statement
    # jump test

    return