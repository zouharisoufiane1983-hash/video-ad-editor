from moviepy import ColorClip, concatenate_videoclips

scene1 = ColorClip(size=(1280, 720), color=(20, 20, 20), duration=3)
scene2 = ColorClip(size=(1280, 720), color=(60, 60, 60), duration=3)
scene3 = ColorClip(size=(1280, 720), color=(100, 100, 100), duration=4)

video = concatenate_videoclips([scene1, scene2, scene3])

video.write_videofile(
    "first_10s.mp4",
    fps=24,
    codec="libx264",
    audio=False
)

print("10 SECOND VIDEO OK")
