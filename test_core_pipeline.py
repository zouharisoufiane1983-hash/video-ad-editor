from video_editor.scenes import create_color_scene, concatenate_scenes
from video_editor.effects import fade_in, fade_out
from video_editor.export import export_video

scene1 = create_color_scene(color=(20, 20, 20), duration=2)
scene2 = create_color_scene(color=(70, 70, 70), duration=2)
scene3 = create_color_scene(color=(120, 120, 120), duration=2)

scene1 = fade_in(scene1, 0.5)
scene3 = fade_out(scene3, 0.5)

video = concatenate_scenes([scene1, scene2, scene3])
export_video(video, "outputs/core_test.mp4", fps=24, audio=False)

print("CORE PIPELINE OK")
