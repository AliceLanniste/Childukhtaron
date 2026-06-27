
#animation

#image rules
define RULES_ANIMATION_SPEED = 0.2
image rules loop_animation:
    # 外部控制：只执行一次的“渐渐显出全貌”（淡入）
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整
    
    # 内部控制：无限循环的帧动画
    contains:
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
        repeat  # 这里的 repeat 只会让 contains 内部的帧循环，不会影响外面的淡入


#image masks
define MASK_ANIMATION_SPEED = 0.2
image prince loop_animation :
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整
   
    contains:
        "animation/masks/prince_1.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/prince_2.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/prince_3.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/prince_2.png"
        pause MASK_ANIMATION_SPEED
        repeat
image young_lady loop_animation :
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整
    contains:
        "animation/masks/young_lady_1.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/young_lady_2.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/young_lady_3.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/young_lady_2.png"
        pause MASK_ANIMATION_SPEED
        repeat
image robber loop_animation :
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整
    contains:
        "animation/masks/robber_1.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/robber_2.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/robber_3.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/robber_2.png"
        pause MASK_ANIMATION_SPEED
        repeat
image warrior loop_animation :
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整
    contains:
        "animation/masks/warrior_1.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/warrior_2.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/warrior_3.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/warrior_2.png"
        pause MASK_ANIMATION_SPEED
        repeat
image princess loop_animation :
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整\
    contains:
        "animation/masks/princess_1.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/princess_2.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/princess_3.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/princess_2.png"
        pause MASK_ANIMATION_SPEED
        repeat
image messenger loop_animation :
    alpha 0.0
    pause 1
    easein 4 alpha 1.0  # 1.5秒内从透明变成完全可见，时间可自行调整
    contains:
        "animation/masks/messenger_1.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/messenger_2.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/messenger_3.png"
        pause MASK_ANIMATION_SPEED
        "animation/masks/messenger_2.png"
        pause MASK_ANIMATION_SPEED
        repeat