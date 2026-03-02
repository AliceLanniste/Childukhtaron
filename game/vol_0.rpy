default prelude_choice_1_checked = False

label vol_0:
    scene bg cicada
    "听说蝉真实的眼睛像网一样密密麻麻地，兜住两只器官，膨胀而成复眼。"
    "那蝉的眼中会有几个世界呢？这些世界会不会各有所异？会不会每个世界里都倒映出一个男孩苍白着脸，举起镊子和相框的摸样？"
    "他的眼里映着蝉将死的样子吗？"
    "会不会有一刻，这是两个活着的生命在彼此注视？"
    "远处的警告声，打断了我和蝉的交流——到点要去清洗那些被黄油香气浸透得发腻的铁锈机器。"
    "沉默着我洗刷油污，蝉也沉默着，被针刺穿翅膀与腹部。"
    "我的生活里，没有永恒。"
    "但蝉的生命里有。"

label campus_dormitory_past:
    scene black
    player "……头有些晕，近来总是在梦中无法醒来"
    with hpunch
    player "糟糕……手指动不了，看来我应该还在梦里"
    show bg room_past
    with hpunch
    player "这是……宿舍？和我的宿舍格局很相似，但有些破旧"
    player "出去看看？……嗯？门怎么推不开，噢，十一点五十分，难道是宵禁期间修女们把门都锁上了？"
    player "如果我没记错的话我们的宿舍门上应该有一个小的瞭望口，就在舍规底下……"
    show rules
    player "这和现在的舍规也差不多么……"
    "被学生撕毁的舍规\n
    一、净体祷告方得主庇佑，诸君应……\n
    二、晚上十点后禁止学生离寝，在校内走动……图书馆……\n
    三、请勿破坏任何……\n
    四、钟声响起后不应聚集、喧哗，以致……"
    show rules
    with hpunch
    rules "谁允许你无礼的脏手碰我！"
    player "?!"
    player "……难道是梦中梦？"
    rules "做梦做梦，还觉得是做梦蠢货！遵守规矩让你很不满吗！"
    player "……先生，你……"
    show bg rules_stage
    with fade
    show rules stage_loop_video
    call screen show_text_on_center("恶行说，\n没有人所见即为才智！")
    call screen show_text_on_center("妄念说，\n不择手段实现即为权力！")
    call screen show_text_on_center("机会说，\n谋杀规则即为新生！")

    scene bg room_past
    with fade
    player "可是先生……"
    show rules at slight_left
    rules "你们大可呼天喊地去抱怨！最后终究会乖乖听话！"
    "舍规背面被你翻开。上面写着学生们的愤懑\n
    “见鬼，谁想遵守这些狗屁规矩”\n
    “鬼地方，不是人待得！”\n
    “撕过，后悔了……”"
    player "谁不想当黑羊呢……如果不给他人添麻烦的话。"
    rules "对，麻烦，恐怖的麻烦！"
    show clock twist at slight_right
    clock "到点了！麻烦！哈哈哈哈"
    clock "格朗迪里有座钟，午夜已有五声响，今夜钟声即将近，谁的歌谣再唱起……"
    show rules humming at slight_left
    rules "听到钟声，请遵舍规！哈哈哈哈"
    scene bg room_past_twist
    player "不好，我要逃出去！醒醒……快醒醒"
    #背景-扭曲宿舍-效果-随着敲门声逐格加速放大（旋转），直到全黑（背景音乐敲门声）
    scene bg room_past_twist at zoom_with_align(2,3)
    pause 3.0
    scene black
# label test:

    show bg awake
    with fade
    player "谁？！"
    do_not_konw_who "兄弟！醒醒！不会睡着了吧？"
    player "……我的手……能动了……！终于离开梦境了吗？"
    show bg room_now
    "从噩梦中分娩出世，一脉相承的暗淡和霉味让你几乎难以辨别是否回到了真实中。"
    "昏暗的寝室内，钟摆已然来到11点过5分，老实无言的舍规盖住门上的瞭望窗，但依稀能看到纸下曾有旧版被撕去的痕迹。"
    do_not_konw_who "糟糕，修女来了，兄弟！记得带上强盗面具，我先走了……"
    sister "宵禁已到，诸位请遵循舍规，虔诚祷告以获庇佑。"
    "祷告的嗡鸣声环绕在你周身，你几乎能想象到一间间无数狭长的房间中匍匐着具具年轻的躯体。非教徒的你伫立在原地，在肃穆的昏暗中萌生出隐秘而微妙的窃喜，像借着神的视角俯瞰信徒。"
    sister "请祷告。"

label menu_pray:
    menu:
        "祷告" if prelude_choice_1_checked == False:
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
    player "修女好像走了……"
    player "聚会的时间我记得好像……在邀请函上写着。"
    "邀请函随着你小心的动作妥帖地从书包中抽出"
    show letter 1
    "多么考究的一封信，连火漆上的纹饰都繁复华丽！"
    "凑近时可以闻到牛皮纸上隐隐透出松柏和什么花朵的冷淡的香气，像女孩清泠狡黠的眼神。握着这封信，你仿佛抓住了某个馥郁的秘密。"
    "打开信封，你看见银灰色的信纸上印着优雅的斜体字:"

label player_home:
    "打开信封能看见银灰色的信纸上印着优雅的斜体字:"
    #（拆信声）
    call screen show_text_on_center(
    """
    邀参演者午夜时分，于“亨特礼堂”举行之宴
    请您带上面具，盛装出演
    我将遵循主古老的教诲，用鸠鸟的血液招待魔鬼
    如蒙亲至，不胜荣幸
    赫卡特
    """)

    scene bg masks at zoom_with_align(1.8,2,0.1,0.2)
    player "我记得赫卡特小姐分配的……好像只有强盗角色，为什么寄来的信封里有两张面具？"
    player "难道这是她的主意？"
    #"王子的面具更微妙地显眼（时间长）"
    player "好精致的面具，这角色比我从前寄宿的贵族老爷还体面！"
    #视角移向强盗面具 逐渐缩小至回前景
    #强盗的面具更微妙地显眼（时间短）
    show bg masks at slide_xoffset(2,-1000)
    pause 3.0
    show bg masks at reset_image(3.0)
    player "可是皮特还在等着我一起赴约……"
    "（午夜钟声响起）"
    player "就这样吧，该赴约了——"
    menu:
        "选择王子面具":
            $ player_select_mask_prince = True

        "选择强盗面具":
            $ player_select_mask_prince = False

    #立绘-出现在左边：玩家换上西装，发梳到脑后
    show player at slight_left
    pause 3.0
    #立绘-老旧的宿舍门推开，舍规掉落
    show rules at slight_right
    pause 3.0
label church_square:
    scene bg view_form_far
    nun_trainee "修修修女——（喷嚏）这么冷的天气，谁会到这禁林……等等这居然有个礼堂？"
    "黑夜悄悄来临，银月挂上树梢。\n乌鸦从林中飞出，诸鬼纷纷现身此世。\n南瓜灯露出瘆人的微笑，黑洞洞的眼望着嬉笑的人群。\n相由心生，面具下神鬼莫辨。\n"
    show nun_mary at slight_left
    nun_mary "此处原是旧教的祈祷处，远道而来的异国人捐赠后修建的，前几年已改为礼堂。"
    nun_trainee "原来如此啊……这么阴森（冷颤）那些孩子们真要在这苦修吗？"
    nun_mary "……勿要揣摩他者。"
    nun_trainee "噢！抱歉！抱歉！真主会赞许他们的虔诚……"

    scene bg pool
    nuns "池盈如月，女神泪滴，映主慈爱，罪恶消弭\n
    泪水汇聚于此，所愿真、所愿诉、所愿熄"
    show player back at fade_in(1.0)
    player "大家都来赴约了……每个人似乎都有自己想扮演的角色，今晚果真是盛宴啊！"
    player "我的选择会让她满意吗？"
    peter "嘿！瞧瞧这位年轻的……"
    if player_select_mask_prince :
        jump prince_mask
    else:
        jump bandit_mask

label prince_mask:
    show player prince_mask
    player "（略显抱歉的笑容）我……抱歉皮特，"
    peter "好了，害！强盗先生您的“脸”，还有这衬衫，先生，看来是没有一点悔意的！"
    player "放了你鸽子，对不起皮特……我也想当一次有姓名的人物……"
    peter "……"
    jump after_choosing_the_mask

label bandit_mask:
    show player bandit_mask
    player "（苦笑）怎么样？我可是放弃了王子角色，皮特先生你可要补偿你的强盗搭档"
    show peter relax
    peter "好小子，你没失约这场戏可就能演了！"
    show peter happy
    peter "别板着脸了强盗先生！"
    jump after_choosing_the_mask

label after_choosing_the_mask:
    "（惊呼声）"
    scene bg she_coming
    "众学生们的惊呼声中，美丽的少女被簇拥着登场，她轻轻向男主看了一眼露出神秘的微笑。"
    "她碧色的、漂亮的眼眸里闪过一丝意味深长的神情。忽然微微笑了。这微笑并不会让她看起来轻浮，反而凸显了她神秘，一种属于女孩子独有的、不让人讨厌的狡猾。"
    player "所有人都注视着她……"
    scene bg pool
    show nun_mary
    nun_mary "注视并非祝祷，其中叵测你是否愿意接受？"
    "男主、皮特" "修女夜安"
    nun_mary "……"
    player "（独白）修女为什么这样看着我？"
    "（钟声响起）"
    "玛丽修女嗤笑（脚步声走去）"
    peter "呼，她可真吓人，对吧？咱们也进去吧！"

label church_inside:
    scene bg church_inside_full_shot
    "时光叹息被镌刻在建筑中，似悲似喜的厚重赋予这砖瓦横梁、装饰浮雕别样的质感。烛光如梦似幻，千年前是否也有一双感怀而渴慕的眼同此刻重叠？"
    "（人群对话宴会声响）"
    player "（独白）学校里竟有这样光彩的地方！谁能想到来在这偏远村庄里已被惊艳了无数次……"
    show peter smile
    peter "这破地方居然还没散架！我说什么，这密特拉塑像缺得叫工匠怎么修补嘛……"
    player "皮特，你来过这？"
    show peter helpless
    peter "何止是来过，我每次贪玩都在这报应了！从前这是大人物们祷告的地方，后来被弃置了。"
    player "（失笑）你啊——"
    player "（独白）命运眷顾我！让我窥见这世界不为俗人敞开的高贵之处。"
    show peter complicated
    peter "这里只有她是例外。"
    scene bg statue_and_table
    "她精致、精美的双眼，如贫瘠原野上燃烧的火焰，奇尔杜克塔伦山谷里唯一的红宝石，在时间洪流里不堕光泽，熠熠生辉。"
    player "（沉思）这张脸，为何美得似曾相识？"
    show students with_mask
    "学生1""哎，你们说这雕像和村口的石女雕像有些相似……"
    "学生2""这可是男学生们投票得出这是校内最美丽的神像！"
    "学生3""听说这个神女像塑成后，异样地沉重，村民们花费数月无法挪动，最后不知如何搬来了这个教堂里……"
    show peter laugh
    peter "你不会相信了吧？想那些没答案的事不如多吃点食堂没见过的东西！"
    player "宴会的食物比食堂丰盛得多呢，这倒是罕见。"
    "学生1""竟有这么多葡萄酒，许多年未见了！葡萄酒真是神赐予人沉醉狂欢的魔药！"
    "学生2""在大家念祝词前，偷偷吃点应该没事吧……"
    "学生3""我的真主，怎么这鸡腿没味道？！"
    show hecate with_mask_and_wine_glass
    hecate "晚上好，欢迎诸君来到迈赫尔节的盛宴。"
    "学生们""（欢呼）"
    show hecate eyes
    hecate "承命运不弃，我等于丰收之日再度赴约，重演此幕。"
    hecate "请带上面具，举起手中的酒液，这杯鸠酒将敬给真主！阿赫里曼（魔鬼）必亡。"
    scene bg statue_and_table
    "不知来处的寒风吹开紧闭得浮雕大门，像古老的身躯复苏，缓慢而嘲哳开启。礼堂中所有的蜡烛应景地熄灭，高台上之上祂漆黑的帘幕骤启，昏暗的月光透过彩色玻璃下礼堂内，像照在被戈壁侵蚀过的枯林。手臂们高举起酒杯，掌中一盏盏深色的酒液在昏暗中倒映出诡异的光。"
    show hecate raise_the_cup_and_recite
    hecate "敬真主！是您古老的教导，致使我们齐聚一堂！惩治那些该长居于地狱的阿赫里曼！"
    "众人""敬真主！"
    hecate "以牙还牙，以眼还眼。敬真主！"
    "众人""敬真主！"
    "命运之酒汩汩流淌，暴虐的醉意将不熄的愤怒、败坏的虔诚与浑浊的爱重领回此刻。莫比乌斯环的起点处，戏剧开场。"
    scene bg poisoned
    "男主举着杯，杯中酒液竟顺着自己举杯的手蜿蜒而下，诡异如藤蔓般扎进血肉里。"
    player "……嘶！好痛！！！该死……我的手臂……这酒？！"
    #play bgm
    hecate "让我们欢迎，每一位主角归位！"
    show bg illusion
    "宴会的现场一地尸体中有6个身影站着，六颗人头上戴着一张张浮夸的面具，以诡异的平转方式回头，酒液似血一般从眼孔中渗出来。角色分别为：武士、异国王子、神使、公主、少女、强盗。"
    if player_select_mask_prince :
        jump the_lie
    else:
        jump the_truth
       
label the_lie:
    "王子（玩家）""我能否成为歌颂的主角？"
    "公主（赫卡特）""世上本没有完整而真实的慷慨，宽恕本非罪人应为。"
    "武士""主上！我将为她而战……"
    "少女（玛丽修女）""爱我者杀我，我爱者死去……命运啊，你不该永远苛待我！"
    "强盗""世人嫉恶，却不仇己，岂不可笑哈哈哈！"
    "神使（皮特）""命运如轮，轨迹无尽，诱惑之眼，视之应何？"
    jump game_title
     
label the_truth:
    "王子""我已成为歌颂的主角，可心口的空洞为何无法填满？"
    "公主（玛丽修女）""爱我者杀我，我爱者死去……命运啊，你应如我所愿一次！"
    "少女（赫卡特）""世上本没有完整而真实的慷慨，谁宽恕他？谁又成全我！"
    "武士""主上！我将为她而战……"
    "强盗（玩家）""放纵欲求，去争夺渴望之人、渴望之物！"
    "神使（皮特）""命运如轮，轨迹无尽，诱惑之眼，视之应何？"
    jump game_title

label game_title:
    scene bg statue_eyes
    
    call screen centered_text_screen(
    """   
    如果你望向神明的眼，能看见多少灵魂？\n
    是密密麻麻地许多，纷纷住满荒唐的念头，相互纠缠着打成死结?\n
    或是孤零零的伫着，浑浊得可以囊括无数颜色。 
    """)
    call screen centered_single_screen(
    """
    这死寂而无情的神眼，\n
    如永恒的镜湖，将真相沉溺。\n
  
    """)
    call screen centered_single_screen(
    """
    直到浸泡其中的灵魂之尸们在日夜不甘中膨胀，\n
    不受控地上浮，让腐烂已久的情绪得以呼吸。
    """)
    
    call screen centered_single_screen("戏剧在永恒中绮丽")
    call screen centered_single_screen("奇尔杜克塔伦山谷在静默中凄鸣")

    scene bg dark_red
    with fade
    show game_title
    #标题-渐显
    pause(10)