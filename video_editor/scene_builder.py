from video_editor.scenes import (
    create_animated_image_scene,
    create_color_scene,
)
from video_editor.transitions import crossfade_transition


def build_image_scene(
    image,
    duration,
    size=(1280, 720),
    ken_burns_start=1.0,
    ken_burns_end=1.08,
):
    return create_animated_image_scene(
        image,
        duration=duration,
        size=size,
        start=ken_burns_start,
        end=ken_burns_end,
    )


def build_color_scene(
    duration,
    size=(1280, 720),
    color=(15, 15, 15),
):
    return create_color_scene(
        size=size,
        color=color,
        duration=duration,
    )


def build_sequence(
    scenes,
    transition_duration=0.5,
):
    if not scenes:
        raise ValueError("Aucune scène fournie.")

    return crossfade_transition(
        scenes,
        duration=transition_duration,
    )
