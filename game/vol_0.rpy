default prelude_choice_1_checked = False
label vol_0:
    scene black with dissolve
    
    show screen menu_icon
    scene bg cicada_1
    with Dissolve (2)
    with Pause(2)
    "听说蝉真实的眼睛像网一样密密麻麻地，\n {w=0.3}兜住两只器官，膨胀而成复眼。"
    "那蝉的眼中会有几个世界呢？"
    "这些世界会不会各有所异？"
    extend "\n会不会每个世界里都倒映出一个男孩苍白着脸，举起镊子和相框的摸样？"
    "他的眼里映着蝉将死的样子吗？"
    "会不会有一刻，{w=0.6}这是两个活着的生命在彼此注视？"
    "远处的警告声，打断了我和蝉的交流"
    extend "\n——到点要去清洗那些被黄油香气浸透得发腻的铁锈机器。"
    "沉默着我洗刷油污，{w=0.6}蝉也沉默着，被针刺穿翅膀与腹部。"
    "我的生活里，{w=0.3}没有永恒。"
    "但蝉的生命里有。"
    stop music 
    tutor "多么动人的文章，您的写作进步远超我的想象"
    tutor "还好从前的艰苦没有给您留下阴影！"
    tutor "您顺利完成波斯语的课程后便能去贵族学校进修了吧？\n那个什么山谷来着？"
    player "是的，去......呃，抱歉，是一所在当地颇负盛名的教会学校，我找找那封律师函……"
    player "嗯，是{outlinecolor=#a55800}奇尔杜克塔伦山谷{/outlinecolor}。我还从没有出过小镇哩，也不知道今后会怎样。"
    tutor "听地名似乎是个颇有历史的文雅之地！"
    tutor "听您的——咳，叔叔提起了，您结业后就能获得遗产吧?\n我的上帝！这是我做梦都……"

    scene black with Dissolve(2.0)

    play music "07_foley_clock_chime_01.ogg"

    player "……{w=0.6}头好晕，近来总是在梦中无法醒来"
    player "怎么又梦到写作课了……"
    player "现在的学校里再没有如此不吝赞扬我的老师。从前的事好像遥远得已经模糊了。"
    

    scene black
    with hpunch
    play sound "08_impact_buzz_01.ogg"

    player "糟糕……"
    stop music   fadeout 3.0
    extend "\n手指动不了，看来我应该还在梦里"

    show bg room_past
    with hpunch
    play music "audio/bgm/1.1-room-past-0.mp3"

    player "这是……{w=0.6}校舍?" 
    extend "\n和我的房间格局很相似，但有些破旧"
    player "出去看看？"
    
    
    play sound "11_door_push_01.ogg"
    with hpunch
    player "{w=0.3}……嗯？" 

    play sound "12_door_push_02.ogg"
    with hpunch
    pause 0.3
    with hpunch
    player "{w=0.3} 门怎么推不开?"
    player "噢，十一点五十分，{w=0.3}难道是宵禁期间修女们把门都锁上了？"
    player "如果我没记错的话……{w=0.3}\n
    房门上应该有一个小的瞭望口，就在舍规底下……"

    show rules
    
    play sound "13_foley_paper_01.ogg"

    player "这和现在的舍规也差不多么……"

    call screen show_text_with_frame(
        "被学生撕毁的舍规\n\n一、净体祷告方得主庇佑，诸君应\n二、晚上十点后禁止学生离寝，在校内走动\n{space=380}图书馆\n三、请勿破坏任何\n四、钟声响起后不应聚集、喧哗，以....",
        font_size = 32,txt_align = 0)
    pause 1.0
    show rules
    with hpunch

    stop music
    play sound "15_impact_hit.ogg"

    rules "谁允许你无礼的脏手碰我！"
    player "......?!"
    play music "audio/bgm/1.1-room-past-0.mp3" fadein 0.5
    player "……{w=0.6}难道是梦中梦？"
    rules "做梦做梦，还觉得是做梦蠢货！\n
    遵守规矩让你很不满吗！"
    player "……先生，你……"

    scene bg rules_stage
    with dissolve
    show rules loop_animation
    play sound "audio/bgm/1.2-rule-rotating.mp3"
    play sound2 "16_foley_writing_02.ogg"
    call screen show_text_slow_with_duration("恶行说，\n 没有人所见即为才智！",font_size = 160,font_color = "#912020")
    call screen show_text_slow_with_duration("妄念说，\n不择手段实现即为权力！",font_size = 160,font_color = "#912020")
    call screen show_text_slow_with_duration("机会说，\n谋杀规则即为新生！",font_size = 160,font_color = "#912020")
    stop music fadeout 2.0
    scene bg room_past
    with dissolve
    player "可是先生……"
    
    play music "audio/bgm/1.1-room-past-0.mp3" fadein 1.0
    show rules at slight_left
    rules "你们大可呼天喊地去抱怨！\n 最后终究会乖乖听话！"
    
    "舍规背面被你翻开，上面写着学生们的愤懑。"
    play sound "13_foley_paper_01.ogg"
    player "“见鬼，谁想遵守这些狗屁规矩”"
    player "“鬼地方，不是人待得！”"
    player "“撕过，后悔了……”"
    player "谁不想当黑羊呢……如果不给他人添麻烦的话。"
    rules "对，麻烦！{w=0.3}恐怖的麻烦！"
    play sound "17_foley_clock_strike.ogg"
    "墙上的钟表猛然发出异响。"
    
    play music2 "18_door_knock_swell.ogg"
    $ renpy.music.set_volume(0.5, channel="music2")
    clock "到点了！麻烦！哈哈哈哈"   
    clock "坎达克里有座钟，午夜已有五声响，今夜钟声即将近，谁的歌谣再唱起……"
    "你听到奇怪的舍规也开始了哼唱。"
    rules "听到钟声，请遵舍规！\n哈哈哈哈"
    player "不好，我要逃出去！醒醒……快醒醒"
    
    scene black
    with eye_shut(0.5)
    play sound "19_whoosh_transition_01.ogg"
    show bg room_past
    show rules at slight_left
    play sound2 "20_impact_eye_appear.ogg"
   
    with eye_open(0.8)
    scene black
    with eye_shut(0.45)
    show bg room_past
    show rules at slight_left
    
    with eye_open(0.8)
    scene black
    with eye_shut(1.5)
    show bg room_past
    show rules at slight_left
    
    with eye_open(1.5)
    scene black
    with eye_shut(2)

    
    stop music
    stop music2

    play music "22_door_knock_01.mp3"
    show screen show_image_with_frame("other/cloika_eye.png") 
    pause 1.0
    hide screen show_image_with_frame
    

    scene bg awake
    play music2 "21_amb_indoor_01.mp3"
    player "谁？！"
    "从噩梦中分娩出世，\n一脉相承的暗淡和霉味让你几乎难以辨别是否回到了真实中。"
    stop music
    peter "兄弟！{w=0.6}醒醒！{w=1.2}\n......不会睡着了吧？"
    player "……{w=0.3}我的手{w=0.6}……{w=0.3}能动了……！"
    extend "\n终于离开梦境了吗？"
    
    scene bg room_now
    play music3 "23_foley_clock_tick_01.mp3"
    "昏暗的寝室内，\n{w=0.3}钟摆已然来到11点过5分 "
    
    "老实无言的舍规盖住门上的瞭望窗，\n{w=0.3}但依稀能看到纸下曾有旧版被撕去的痕迹。"
    play sound "27_foley_footsteps_approach.mp3"
    play sound2  "28_foley_clock_chime_02.ogg"
    peter "糟糕，{w=0.6}修女来了，\n {w=0.3}[player.name]！记得带上强盗面具，我先走了……"
    $ renpy.pause(3.0, hard=True)
    sister "宵禁已到"
    sister "诸位请遵循舍规，\n{w=0.3}虔诚祷告以获庇佑。"
    play music "29_amb_prayer_chant.mp3"
    #####play music4 "1-3-room-now-1.mp3"
    "祷告的嗡鸣声环绕在你周身，\n {w=0.6}你几乎能想象到一间间无数狭长的房间中匍匐着具具年轻的躯体 "
    "非信徒的你伫立在原地, \n{w=1.2}在肃穆的昏暗中萌生出隐秘而微妙的窃喜 "
    "像借着神的视角俯瞰信徒。 "
    sister "请祷告。"
    #play music "01"
    play sound "31_ui_click_confirm.ogg"
# label test:
label menu_pray:
    menu:
        "祷告" if not prelude_choice_1_checked:
            jump pray
        "不祷告":
            jump do_not_pray

label pray:
    player "……？"
    player "不可能……隔着舍规应该不会被发现……"
    $ prelude_choice_1_checked = True
    jump menu_pray

label do_not_pray:
    player "……？"
    player "不可能……隔着舍规应该不会被发现……"
    jump after_menu_pray

label after_menu_pray:
    stop music
    stop music3 fadeout 1.0
    play music "20_impact_eye_appear.ogg"
    $ renpy.pause(6.5, hard=True)
    stop music
    pause 1.0
    play sound "32_foley_footsteps_fade.ogg"
    $ renpy.pause(4.0, hard=True)
    player "修女好像走了……"
    player "聚会的时间我记得好像……在邀请函上写着。"
    "邀请函随着你小心的动作妥帖地从书包中抽出"
    play sound "13_foley_paper_01.ogg" 
    ####play music "1.3-room-now-1.mp3"
    show letter 1
    "{w=0.6}多么考究的一封信，\n{w=0.3}连火漆上的纹饰都繁复华丽！"
    "凑近时可以闻到牛皮纸上隐隐透出松柏\n和什么花朵的冷淡的香气"
    "像女孩清泠狡黠的眼神。 "
    extend"\n握着这封信，{w=0.3}你仿佛抓住了某个馥郁的秘密。"
     
    play sound "34_foley_paper_unfold.ogg"  

    "打开信封，你看见银灰色的信纸上印着优雅的斜体字:"

    show black:
        alpha 0
        linear 0.5 alpha 0.1
    call screen show_text_with_frame(
        "诚邀参演者午夜时分，于亨特礼堂举行夜宴。\n请您带上面具，盛装出演。\n我将遵循主古老的教诲，用鸠鸟的血液招待魔鬼。\n如蒙亲至，不胜荣幸。\n{space=800}赫卡特",
        font_size = 46,frame_size_x = 1470,text_y_align = 0.6,l_spacing = 40)
    hide black
    player "我记得赫卡特小姐分配的……{w=0.3}好像只有强盗角色\n{w=0.8}为什么寄来的信封里有两张面具？"

    $ cloika_masks_animation_stage = "zoom_to_left"
    show screen show_cloika_masks()
    player "难道这是她的主意？"
    "微妙地，{w=0.3}王子的面具在你看来格外显眼。"
    "王子戴着羽翼装饰的兜帽、高贵华丽的金色额饰。"
    extend "\n你注意到他光泽的肌肤、茂密的头发和充满魅力的笑容"
    player "好精致的面具，这角色比我从前寄宿的贵族老爷还体面！"
    $ cloika_masks_animation_stage = "zoom_to_right"
    "对比之下，{w=0.3}强盗的面具上，夸张的尖耳尖鼻像地精般凶恶。"
    extend"\n吓人的黑色刺青纹饰与胡子连成一片，张开獠牙似乎在呐喊什么。"
    $ cloika_masks_animation_stage = "reset"
    play music "28_foley_clock_chime_02.ogg"
    player "可是[peter.name]还在等着我一起赴约……"

    
    player "就这样吧，{w=0.3}该赴约了"
    stop music2
    hide screen show_cloika_masks
    pause 0.5
    scene black
    with fade
    pause 3.0
    
    scene bg view_form_far
    

    with fade
      ####  ####  ####  ####  ####stop music fadeout 3.0
    play music "40_amb_forest_autumn.ogg"
    play music "39_whoosh_transition_04.ogg"
    play music "40_amb_forest_autumn.ogg" noloop
    "离开校舍后，你的身影消失在树林中。"
    "奇尔杜克塔伦重重叠叠的峦和黑绿的树木，似乎能捂住一切造物的痕迹。在这里，火光黯淡于浓雾，鸟鸣销匿于深谷。所能做的，唯有祈祷。"

    nun_trainee "修、{w=0.3}修、{w=0.3}修女——{w=0.6}阿嚏！"
    extend "\n这么冷的天气，{w=0.3}谁会到这禁林……"
    extend"等等，这居然有个礼堂？"
    show screen show_image_with_frame_and_fade("other/cloika_the_nun.png",x_align = 0.95)
    "黑夜匍匐在禁谷之地中，浓稠的寒弥漫。\n{w=0.3}银月如半阖的眼，亘古如此地漠然望着人间的轮回"
    "冷雾浸入月光，泡制出一树树的惨白，\n{w=0.3}张牙舞爪的粗枝乱藤像已逝去的躯壳，附在大地上无声而狰狞的呐喊着。"
    "呼啸的风声里掺杂着羽翼扑朔，低低哭泣."
    extend "\n鬼影幢幢里唯有一座腐旧的礼堂清晰而执拗地伫立在原点。"
    play music "41_whoosh_transition_05.ogg"

    nun_mary "此处原是旧教的祈祷处，远道而来的异国人捐赠后修建的，前几年已改为礼堂。"
    nun_trainee "原来如此啊……{w=0.6}这么阴森……{w=0.6}那些孩子们真要在这苦修吗？"
    nun_mary "……勿要揣摩他者。"
    nun_trainee "噢！抱歉！抱歉！真神会赞许他们的虔诚……"
    play music  "42_whoosh_transition_06.ogg"
    hide screen show_image_with_frame_and_fade

    play music "43_amb_church_entrance.mp3"
    scene bg pool
    with fade


    "{w=1}礼堂外散落着孩童们乱刻的杰作——\n{w=0.6}一堆堆表情扭曲的石榴和南瓜雕塑，{w=0.3}没有火光的存在。"
    "于是妖邪、恶魔、精怪……\n从迷雾中陆续现身，嬉闹和夸张的笑声驱散了嘶哑鸦鸣。"
    "若是相由心生，{w=0.6}那么面具下神鬼莫辨。"

    player "大家都来赴约了……"
    extend "\n每个人似乎都有自己想扮演的角色，{w=0.3}今晚果真是盛宴啊！"
    player "我的选择会让她满意吗？"
    peter "嘿！瞧瞧这位年轻的……"
    player "{w=0.6}我…{w=1}…抱歉，{w=0.3}[peter.name]。"
    peter "好了，唉！{w=0.3}强盗先生您的“脸”，还有这衬衫\n{w=0.6}先生，看来是没有一点悔意的！"
    player "放了你鸽子，对不起[peter.name]……我也想当一次有姓名的人物……"
    peter "……"

    play music "44_human_girl_laugh.ogg"
    play music "45_whoosh_bell_chime.ogg" noloop
    show screen show_image_with_frame_and_fade("other/cloika_dancing_girls.png")
    "水池旁围伴着三位少女。\n{w=0.6}她们一边旋转着，{w=0.3}一边唱着音调怪异的曲子"
    play music "46_human_girl_murmur.ogg"

    call screen show_text_slow_with_button("池盈如月，女神泪滴，映主慈爱，罪恶消弭。",y_align = 0.65)
    call screen show_text_slow_with_button("泪水汇聚于此！",y_align = 0.65)
    call screen show_text_slow_with_button("所愿真！",y_align = 0.65)
    call screen show_text_slow_with_button("所愿诉！",y_align = 0.65)
    call screen show_text_slow_with_button("所愿熄！",y_align = 0.65)
    play music "43_amb_church_entrance.ogg"

    player "这是什么装扮？{w=0.6}有些像修女，但又不太像呢……"
    extend "\n[peter.name]，你知道吗？"
    peter "没错，她们可不是什么修女！"
    peter "嗯……{w=0.3}算是一种古老的节日装扮吧。\n{w=0.3}从很早以前就有这样的打扮了。不过也有修女会这么穿。"
    player "不愧是你[peter.name]，你好像什么都知道。"
    player "那我们也要去祷告吗？"
    peter "越来越会揶揄人了，先生，我还不了解你吗！"
    play music "47_human_crowd_gasp.ogg"
    hide screen show_image_with_frame_and_fade
    pause 2.0

    
    show screen show_image_with_frame_and_fade("other/cloika_she_coming_p1.jpg",x_align = 0.95) as she_coming_p1
    pause 2.0
    play music "48_foley_bell_double.ogg"
    show screen show_image_with_frame_and_fade("other/cloika_she_coming_p2.jpg",x_align = 0.8) as she_coming_p2

    "惊呼与议论交织，喧哗中她凭空出现 "

    
    "女人被簇拥着却有种离群的美丽，任由旁人目光染指"
    extend "\n这是你第一次在人群中直视她的面容，{w=0.3}这样的注视让你在惊艳中隐隐感到恼人的渴望。"
    player "所有人都注视着她……"
    "正当你心绪不宁时，她在众目睽睽中，轻巧而迅猛地攫住你的心脏。"
    extend "\n你听见自己急速的呼吸，{w=0.3}眼里只剩她那双碧色的眼眸，意味深长地看向你，忽然微微笑了。"
    "这微笑并不会让她看起来轻浮，反而凸显了神秘，\n{w=0.3}一种属于女孩子独有的、不让人讨厌的狡猾。"

    nun_mary "注视并非祝祷，其中叵测你是否愿意接受？"

    player_and_peter "啊、{w=0.3}修女夜安！"
    nun_mary "……"
    player "修女为什么这样看着我？"
    play music "28_foley_clock_chime_02.ogg"
    hide screen she_coming_p1
    hide screen she_coming_p2
    
    #"（钟声响起）"
    "[nun_mary.name]嗤笑 "
    peter "呼，她可真吓人，对吧？{w=0.3}咱们也进去吧！"
    play music "49_whoosh_transition_magic.ogg"
    play music "50_amb_hall_banquet.ogg"

    scene black with dissolve
    show bg church at fade_in(pos_y = -1080)
    show curtain_left at fade_in(pos_y = -780)
    show curtain_right at fade_in(pos_x = 960, pos_y = -780)
    player "学校里竟有这样光彩的地方！\n谁能想到来在这偏远村庄里已被惊艳了无数次……"
    "时光叹息被镌刻在建筑中，似悲似喜的厚重赋予\n这砖瓦横梁、装饰浮雕别样的质感。"
    "烛光如梦似幻，千年前是否也有一双感怀而渴慕的眼同此刻重叠？"
    peter "这破地方居然还没散架！我说什么，这密特拉塑像缺得叫工匠怎么修补嘛……"
    player "[peter.name]，你来过这？"
    peter "何止是来过，我每次贪玩都在这报应了！从前这是大人物们祷告的地方，后来被弃置了。"
    player "看来主格外关注你的举止呢"
    peter "……主吗？"
    player "命运眷顾我！{w=0.3}让我窥见这世界不为俗人敞开的高贵之处。"
    peter "这里只有她是例外。"
    play music "51_whoosh_rope_appear.ogg"
    call screen church_drag_rope

label after_drag_rope:
    play music "52_foley_rope_pull_down.ogg"
    hide screen church_drag_rope
    play music "55_cloth_curtain_move.ogg"
    show curtain_left:
        linear 5.0 xpos -960
    show curtain_right:
        linear 5.0 xpos 1920

    play music "54_whoosh_camera_pan.ogg"  noloop
   
    camera:
        linear 5.0 ypos 1080
        ypos 1080

    "{w=3.0}她精致、精美的双眼，\n如贫瘠原野上燃烧的火焰，"
    "奇尔杜克塔伦山谷里唯一的红宝石，在时间洪流里不堕光泽，熠熠生辉。"
    player "这张脸，为何美得似曾相识？"
    student_1 "哎，你们说这雕像和村口的石女雕像，是不是有些相似……"
    player "单独一尊倒是没有那群塑像吓人"
    student_2 "这可是男学生们公投得出这是校内最美丽的脸蛋！"
    player "若要我来选……"
    student_3 "听说这个女神像塑成后，异样地沉重，村民们花费数月无法挪动，最后不知如何搬来了这个礼堂里……"
    player "等我收到那份命运亏欠我的礼物，倒是可以搬一尊到我的庄园里！"
    peter "你不会相信他们说的吧？{w=0.3}想那些没答案的事不如多吃点食堂没见过的东西！"
    camera:
        linear 5.0 ypos 0
        ypos 0
    $ renpy.pause(5.0, hard=True)

    show screen show_image_with_frame_and_fade("other/cloika_wine_and_food.png")
   
    player "宴会的食物比食堂丰盛得多呢，这倒是罕见。"
    play music "56_foley_cutlery_clatter.ogg"
    play music "57_amb_banquet_01.ogg"
    student_1 "竟有这么多葡萄酒，许多年未见了！葡萄酒真是神赐予人沉醉狂欢的魔药！"
    player "从前当学徒时只能看着绅士们喝的葡萄酒，如今在学堂内竟应有尽有……"
    student_2 "在大家念祝词前，偷偷吃点应该没事吧……"
    "你看着食物犹豫又好奇"
    student_3 "我的真神，怎么这鸡腿没味道？！"
    player "嗯？应当不会吧……"
    play music  "58_glass_fork_clink.ogg"
    play music "59_amb_banquet_02.ogg"
    hecate "晚上好，欢迎诸君来到迈赫尔节的盛宴。"
    "身旁的学生们欢呼雀跃。"
    hecate "承命运不弃，我等于丰收之日再度赴约，重演此幕。"
    hecate "请带上面具，举起手中的酒液，这杯鸠酒将敬给真神！阿赫里曼必亡。"
    show black:
        alpha 0
        linear 1 alpha 0.5
        alpha 0.5
    hide screen show_image_with_frame_and_fade

    play  music "60_whoosh_cold_wind.ogg"
    play  music "61_door_wooden_creak.ogg"
    show screen show_image_with_frame_and_fade("other/cloika_speech_1.png") as cloika_speech_1
    "不知来处的寒风吹开了紧闭的大门，像古老的身躯复苏，缓慢而嘲哳开启。"
    "礼堂中所有的蜡烛应景地熄灭，高台上之上祂漆黑的帘幕骤启，"
    extend "\n昏暗的月光透过彩色玻璃下礼堂内，像照在被戈壁侵蚀过的枯林。"
    "所有手臂高举起酒杯，掌中一盏盏深色的酒液在昏暗中倒映出奇异的光。"
    hecate "敬真神！是您古老的教导，致使我们齐聚一堂！惩治那些该长居于地狱的阿赫里曼！"
    play audio "patricksilvey_weather_lightning_2_464187.mp3"
    "众人""敬真神！{nw}"
  
    show screen show_image_with_frame_and_fade("other/bg_white.png",duration_show = 0.1,duration_hide = 0.1,alpha_max = 0.5) as white
    pause 1.0
    hide screen white
    play music "62_glass_toast_clink.ogg"
    hecate "以牙还牙，以眼还眼。敬真神！"
    play audio "patricksilvey_weather_lightning_2_464187.mp3"
    "众人""敬真神！{nw}"
    play msuic "63_impact_flicker_buzz.ogg"
    show screen show_image_with_frame_and_fade("other/bg_white.png",duration_show = 0.1,duration_hide = 0.1,alpha_max = 0.7) as white
    pause 1.0
    hide screen white
    player "……嘶！好痛！！！"
    extend "\n该死……我的手臂…{w=0.6}…这酒？！{nw}"
    play audio "patricksilvey_weather_lightning_2_464187.mp3"
    show screen show_image_with_frame_and_fade("other/bg_white.png",duration_show = 0.1,duration_hide = 0.1) as white
    pause 1.0
    hide screen white
    hide screen cloika_speech_1
    show screen show_image_with_frame_and_fade("other/cloika_speech_2.png")
    "你杯中酒液竟顺着举杯的手蜿蜒而下，诡异如藤蔓般扎进血肉里。"
    "命运之酒汩汩流淌，{w=0.3}暴虐的醉意将不熄的愤怒、\n败坏的虔诚与浑浊的爱重领回此刻。"
    "莫比乌斯环的起点处，戏剧开场."
    #play bgm
    hecate "让我们欢迎，每一位主角归位！"
    hide screen show_image_with_frame_and_fade
    play music "64_glass_shatter.ogg"
    play music "65_foley_body_fall.ogg"
    scene black
    "你倒下了。"
    "目光所及之处，宴会厅一地的尸体中有六个身影站着。"
    "六颗人头上戴着一张张浮夸的面具，以诡异的平转方式回头，酒液似血一般从眼孔中渗出来。"
    show prince loop_animation
    prince "我能否成为歌颂的主角？{w=1.0}{nw}"

    show young_lady loop_animation
    young_lady "世上本没有完整而真实的慷慨，宽恕本非罪人应为。{w=1.0}{nw}"

    show robber loop_animation
    robber "世人嫉恶，却不仇己，岂不可笑哈哈哈！{w=1.0}{nw}"

    show warrior loop_animation
    warrior "主上！我将为她而战……{w=1.0}{nw}"

    show princess loop_animation
    princess "爱我者杀我，我爱者死去…{w=0.3}…命运啊，你不该永远苛待我！{w=1.0}{nw}"

    show messenger loop_animation
    messenger "命运如轮，轨迹无尽，诱惑之眼，视之应何？{w=1.0}{nw}"
    stop music
    show bg statue_eyes:
        alpha 0
        zoom 1.0
        xalign 0.05
        yalign 0.35
        linear 1.0 alpha 1.0
        linear 20 zoom 2 
    "如果你望向神明的眼，能看见多少灵魂？{w=1.0}{nw}"
    "是密密麻麻地许多，纷纷住满荒唐的念头，相互纠缠着打成死结?\n{w=0.6}或是孤零零的伫着，浑浊得可以囊括无数颜色。{w=1.0}{nw}"
    "这死寂而无情的神眼，\n如永恒的镜湖，将真相沉溺。{w=1.0}{nw}"
    "直到浸泡其中的灵魂之尸们在日夜不甘中膨胀，\n{w=0.6}不受控地上浮，让腐烂已久的情绪得以呼吸。{w=1.0}{nw}"
    "戏剧在永恒中绮丽{w=1.0}{nw}"
    $ renpy.pause(5.0, hard=True)
    show dark_red
    with Dissolve(5.0)
    "奇尔杜克塔伦山谷在静默中凄鸣{w=1.0}{nw}"
    show game_title_finnal
    with dissolve
    pause 30