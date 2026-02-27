#define character
define do_not_konw_who = Character("??")
define player = Character("男主")
define rules = Character("舍规",image = "rules")
define sister = Character("修女")
define clock = Character("钟表")
define peter = Character("皮特")
define nun_trainee = Character("见习修女")
define nun_mary = Character("修女玛丽")
define nuns = Character("神女们")
define hecate = Character("赫卡特")

#image character
image rules= "character/rules/rules_1.png"
image rules stage_loop_video = Movie(
    play = "video/video_rules_stage.webm",
    loops = -1)



image player back = "character/player/player_back.png"
image player prince_mask = "character/player/player_prince_mask.png"
image player bandit_mask = "character/player/player_bandit_mask.png"

image peter happy = "character/peter/peter_happy.png"
image peter relax = "character/peter/peter_relax.png"
image peter smile = "character/peter/peter_smile.png"
image peter helpless = "character/peter/peter_helpless.png"
image peter complicated = "character/peter/peter_complicated.png"
image peter laugh = "character/peter/peter_laugh.png"

image rules stage_lighting = "character/rules/rules_stage_lighting.png"
image rules humming = "character/rules/rules_humming.png"

image clock twist = "character/clock/clock_twist.png"

image hecate with_mask_and_wine_glass = "character/hecate/hecate_with_mask_and_wine_glass.png"
image hecate eyes = "character/hecate/hecate_eyes.png"
image hecate raise_the_cup_and_recite = "character/hecate/hecate_raise_the_cup_and_recite.png"

image students with_mask = "character/other/sudiostudents_with_mask.png"



#image other
image game_title = "other/game_title.png"
image letter 1 = "other/letter_1.png"

#image bg
image bg cicada = "bg/bg_cicada.png"
image bg room_past = "bg/bg_room_past.png"
image bg room_past_twist = "bg/bg_room_past_twist.jpg"
image bg room_now = "bg/bg_room_now.png"
image bg rules_stage = "bg/bg_rules_stage.png"
image bg awake = "bg/bg_awake.png"

image bg dark_red = "bg/bg_dark red.png"
image bg dark_black = "bg/bg_dark_black.png"
image bg illusion = "bg/bg_illusion.png"
image bg masks = "bg/bg_masks.png"
image bg poisoned = "bg/bg_poisoned.png"
image bg pool = "bg/bg_pool.jpg"
image bg rules = "bg/bg_rules.jpg"
image bg she_coming = "bg/bg_she_coming.png"
image bg view_form_far = "bg/bg_view_form_far.jpg"
image bg statue_eyes = "bg/bg_statue_eyes.png"
#以下为缺失BG
image bg invitation_letter_unopened = "bg/bg_invitation_letter_unopened.png"
image bg invitation_letter_opened = "bg/bg_invitation_letter_opened.png"
image bg church_inside_full_shot = "bg/bg_church_inside_full_shot.png"
image bg statue_and_table = "bg/statue_and_table.png"

#game data
default player_select_mask_prince = False

#transform
transform slight_left :
    xalign 0.25
    yalign 1.0

transform slight_right :
    xalign 0.75
    yalign 1.0

transform reset_image(duration=0.0):
    linear duration zoom 1.0 alpha 1.0 xoffset 0 yoffset 0

transform zoom_with_align(zoom_size=1.5, duration=1.0, x_align=0.5, y_align=0.5):
    xalign x_align
    yalign y_align
    linear duration zoom zoom_size

transform slide_xoffset(duration=1.0, x_offset=200):
    linear duration xoffset x_offset

transform fade_in(duration=1.0):
    alpha 0.0
    linear duration alpha 1.0

# 游戏在此开始。
label start:
    # jump test
    jump vol_0

    return