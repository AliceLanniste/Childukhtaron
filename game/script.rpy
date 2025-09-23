# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define player = Character("男主")
define peter = Character("皮特")
define nun = Character("修女")
define robber = Character("强盗")
define princess = Character("公主")
define knight = Character("武士")
define leading_actress = Character("少女")
define envoy = Character("神使")

image bg dark = "bg/bg_dark.png"
image bg invitation_letter_unopened = "bg/bg_invitation_letter_unopened.png"
image bg invitation_letter_opened = "bg/bg_invitation_letter_opened.png"
image bg two_masks = "bg/bg_two_masks.png"
image bg church_square_long_shot = "bg/bg_church_square_long_shot.png"
image bg pool = "bg/bg_pool.png"
image bg leading_actor_nervous = "bg/bg_leading_actor_nervous.png"
image bg leading_actress_appear = "bg/bg_leading_actress_appear.png"
image bg nun_clap = "bg/bg_nun_clap.png"
image bg church_inside_full_shot = "bg/bg_church_inside_full_shot.png"
image bg banquet_poisoning = "bg/bg_banquet_poisoning.png"
image bg the_six_phantom_figures = "bg/bg_the_six_phantom_figures.png"
image bg statue_eye = "bg/bg_statue_eye.png"
image bg game_title = "bg/bg_game_title.png"

transform slight_left :
    xalign 0.25
    yalign 1.0
# 游戏在此开始。

label start:
    jump opening_statement

    return