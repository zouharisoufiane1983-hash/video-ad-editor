from pathlib import Path

from video_editor.scenes import create_color_scene, create_image_scene
from video_editor.branding import add_image, add_text
from video_editor.effects import fade_in, fade_out, ken_burns
from video_editor.audio import load_audio, add_audio, fit_audio_to_duration
from video_editor.export import export_video
from video_editor.presets import get_preset


def create_ad(
    output,
    logo=None,
    product_image=None,
    music=None,
    title="DAR GHIZLANE",
    subtitle="Mode traditionnelle marocaine",
    duration=10,
    size=(1280, 720),
    preset="luxury",
):
    width, height = size
    style = get_preset(preset)

    if product_image and Path(product_image).is_file():
        video = create_image_scene(
            product_image,
            duration=duration,
            size=size,
        )
        video = ken_burns(
            video,
            start=style["ken_burns_start"],
            end=style["ken_burns_end"],
        )
    else:
        video = create_color_scene(
            size=size,
            color=style["background"],
            duration=duration,
        )

    if logo and Path(logo).is_file():
        video = add_image(
            video,
            logo,
            position=("center", "center"),
        )

    video = add_text(
        video,
        title,
        font_size=style["title_size"],
        color="white",
        position=("center", height - 150),
    )

    video = add_text(
        video,
        subtitle,
        font_size=style["subtitle_size"],
        color="white",
        position=("center", height - 80),
    )

    video = fade_in(video, style["fade_in"])
    video = fade_out(video, style["fade_out"])

    audio = None

    if music and Path(music).is_file():
        audio = load_audio(music)
        audio = fit_audio_to_duration(audio, duration)
        video = add_audio(video, audio)

    export_video(
        video,
        output,
        fps=24,
        audio=audio is not None,
    )

    if audio is not None:
        audio.close()

    return output
