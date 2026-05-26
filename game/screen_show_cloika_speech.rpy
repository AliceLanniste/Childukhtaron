screen show_cloika_speech(frame_size = 6):
    frame at repeated_intense_flashing:
        background "#000000"
        xalign 0.5
        yalign 0.5
        padding (frame_size, frame_size)
        add "other/cloika_speech_2.png" :
            xalign 0.5
            yalign 0.5

transform repeated_intense_flashing:
    alpha 1.0
    linear 0.1 alpha 0.0
    linear 0.1 alpha 1.0
    repeat