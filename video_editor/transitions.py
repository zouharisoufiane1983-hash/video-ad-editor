from moviepy import concatenate_videoclips, vfx


def crossfade_transition(clips, duration=0.5):
    if not clips:
        raise ValueError("Aucun clip fourni.")

    if len(clips) == 1:
        return clips[0]

    if duration <= 0:
        return concatenate_videoclips(clips, method="compose")

    prepared = [clips[0]]

    for clip in clips[1:]:
        prepared.append(
            clip.with_effects([vfx.CrossFadeIn(duration)])
        )

    return concatenate_videoclips(
        prepared,
        padding=-duration,
        method="compose",
    )
