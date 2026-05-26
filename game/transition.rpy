init python:
    def eye_shut(duration=1.0):
        return ImageDissolve("other/eye.png", duration, ramplen = 128 , reverse=True)
    def eye_open(duration=1.0):
        return ImageDissolve("other/eye.png", duration, ramplen = 128)
