#image gameover = "badending.png"

init python:
    def slider_update(st):
        global slider_speed

        for sprite in slider_sprites:
            if sprite.type == "slider":
                if round(sprite.x) < slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.x += slider_speed*chest_difficulty
                    slider_speed += 0.04
                elif round(sprite.x) >= slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.direction = "left"
                    slider_speed = 2
                elif round(sprite.x) > 0 and sprite.direction == "left":
                    sprite.x -= slider_speed*chest_difficulty
                    slider_speed += 0.04
                elif round(sprite.x) == 0 and sprite.direction == "left":
                    sprite.direction = "right"
                    slider_speed = 2
        if not stop_slider:
            return 0
        else:
            return None

    def check_slider_safe_zone():
        global chest_unlocked
        global chest_unlock_tries
        global stop_slider

        for slider in slider_sprites:
            if slider.type =="slider":
                for safe_zone in slider_sprites:
                    if safe_zone.type == "safe-zone":
                        if safe_zone.x < slider.x < safe_zone.x + safe_zone_size[0]:
                            chest_unlocked = True
                            stop_slider = True
                            renpy.play("audio/open-door.ogg", "sound")
                        elif chest_unlock_tries > 0:
                            renpy.play("audio/error.ogg","sound")
                            chest_unlock_tries -= 1
                        if chest_unlock_tries == 0:
                            renpy.show_screen("game_over")
                            #renpy.showing("images/badending.png", "images")
                            stop_slider = True

    def reset_chest_puzzle():
        global chest_unlocked
        global chest_unlock_tries
        global stop_slider
        global slider_speed

        chest_unlocked = False
        chest_unlock_tries = 2
        stop_slider = False
        slider_speed = 2

        for sprite in slider_sprites:
            if sprite.type == "slider":
                sprite.x = 0
            elif sprite.type == "safe-zone":
                random_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
                sprite.x = random_x

        slider_SM.redraw(0)
        renpy.restart_interaction()

transform full_size:
    zoom 1

transform half_size:
    zoom 0.5

transform chest_transform:
    zoom 0.5
    anchor (0.5,0.5)
    align (0.5,0.7)
    subpixel True
    on hover:
        easein 1.0 zoom 0.51
    on idle:
        easein 1.0 zoom 0.5

transform chest_unlocked_anim:
    zoom 0.5
    alpha 0.0
    parallel:
        easein 3.0 zoom 0.7
    parallel:   
        easein 2.0 alpha 1.0

screen game_over:
    modal True
    key "K_SPACE" action [Function(reset_chest_puzzle), Hide("game_over")]
    #show gameover
    #with Pause()
    
    frame:
        image "images/badending.png" at full_size
        #background "images/badending.png"
        xfill True
        yfill True
        frame:
            background "#ffffffe6" 
            xfill True
            padding (15,2)
            align (0.5,0.74)
            text "...Ulangi Mini Game..." color "#000000" size 34 xalign 0.5
        frame:
            background "#000000e6"
            xfill True
            padding (15,0)
            align (0.5,0.8)
            text "...Kembali ke Menu Utama..." color "#818181" size 34 xalign 0.5 
        

screen chest_puzzle:
    key["K_SPACE","mousedown_1"] action If(chest_unlocked, true=[Hide("chest_puzzle",transition = Fade(1,1,1)), Show("scene_1")], false = Function(check_slider_safe_zone))
    image "mengambilkeris1.png" at full_size
    if not chest_unlocked:
        frame:
            background "#FFFFFF"
            padding (5,5)
            align (0.5,0.25)
            text "Sisa Percobaan: [chest_unlock_tries]" size 24 color "#000000" text_align 0.5
        frame:
            background None
            align (0.5,0.3)
            xysize slider_bar_size
            image "slider-bar.png" at half_size
            add slider_SM
        image "chest-closed-idle.png" align (0.5,0.7) zoom 0.5
    else:
        image "chest-opened.png" align (0.5,0.7) at chest_unlocked_anim

screen scene_1:
    image "mengambilkeris1.png" at full_size
    imagebutton auto "chest-closed-%s.png" action [Hide("scene_1"), Show("chest_puzzle")] at chest_transform

label start:
    $slider_SM = SpriteManager(update = slider_update)
    $slider_sprites = []

    #safe zone variables
    $safe_zone_image = Image("safe-zone.png")
    $safe_zone_transform = Transform(child = safe_zone_image, zoom = 0.5)
    $safe_zone_size = (int(149 / 2), int(70 / 2))
    $slider_sprites.append(slider_SM.create(safe_zone_transform))    
    $slider_sprites[-1].type = "safe-zone"
    
    #slider variables
    $slider_bar_size = (int(545 / 2), int(70 / 2))
    $slider_image = Image("slider.png")
    $slider_transform = Transform(child = slider_image, zoom = 0.5)
    $slider_sprites.append(slider_SM.create(slider_transform))
    $slider_sprites[-1].type = "slider"
    $slider_sprites[-1].direction = "right"
    $slider_size = (int(48 / 2), int(66 / 2))
    $slider_speed = 2
    $stop_slider = False

    #home variable
    $chest_unlocked = False
    $chest_unlock_tries = 2
    $chest_difficulty = 1

    call screen scene_1
    return