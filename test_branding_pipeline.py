from video_editor.scenes import create_color_scene
from video_editor.branding import add_image
from video_editor.effects import zoom, fade_in, fade_out
from video_editor.export import export_video

logo = "assets/images/dar_ghizlane_logo.png"

video = create_color_scene(color=(15, 15, 15), duration=5)
video = add_image(video, logo, position=("center", "center"))
video = zoom(video, start=0.85, speed=0.03)
video = fade_in(video, 0.7)
video = fade_out(video, 0.7)

export_video(video, "outputs/branding_test.mp4", fps=24, audio=False)

print("BRANDING PIPELINE OK")
