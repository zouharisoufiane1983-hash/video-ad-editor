from video_editor.scenes import create_color_scene
from video_editor.branding import add_image, add_text
from video_editor.effects import fade_in, fade_out
from video_editor.export import export_video

logo = "assets/images/dar_ghizlane_logo.png"

video = create_color_scene(color=(15, 15, 15), duration=5)
video = add_image(video, logo, position=("center", "center"))
video = add_text(video, "DAR GHIZLANE", font_size=70, color="white", position=("center", 520))
video = fade_in(video, 0.7)
video = fade_out(video, 0.7)

export_video(video, "outputs/branding_text_test.mp4", fps=24, audio=False)

print("BRANDING + TEXT PIPELINE OK")
