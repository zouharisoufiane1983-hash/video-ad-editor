from moviepy import ColorClip, ImageClip, CompositeVideoClip, concatenate_videoclips


def create_color_scene(size=(1280, 720), color=(20, 20, 20), duration=3):
    return ColorClip(size=size, color=color, duration=duration)


def create_image_scene(image, duration=5, size=(1280, 720)):
    width, height = size
    video = ImageClip(image).with_duration(duration)

    scale = max(width / video.w, height / video.h)
    new_width = int(video.w * scale)
    new_height = int(video.h * scale)

    video = video.resized((new_width, new_height))
    video = video.with_position(("center", "center"))

    canvas = ColorClip(
        size=size,
        color=(15, 15, 15),
        duration=duration,
    )

    return CompositeVideoClip([canvas, video], size=size)


def create_animated_image_scene(
    image,
    duration=5,
    size=(1280, 720),
    start=1.0,
    end=1.08,
):
    width, height = size
    source = ImageClip(image).with_duration(duration)

    base_scale = max(width / source.w, height / source.h)
    base_width = int(source.w * base_scale)
    base_height = int(source.h * base_scale)

    source = source.resized((base_width, base_height))

    def scale_at(t):
        progress = min(max(t / duration, 0), 1)
        return start + (end - start) * progress

    animated = source.resized(scale_at)
    animated = animated.with_position(("center", "center"))

    canvas = ColorClip(
        size=size,
        color=(15, 15, 15),
        duration=duration,
    )

    return CompositeVideoClip(
        [canvas, animated],
        size=size,
    )


def concatenate_scenes(scenes):
    return concatenate_videoclips(scenes)
