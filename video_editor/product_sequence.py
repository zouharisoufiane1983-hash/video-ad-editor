from pathlib import Path

from video_editor.scene_builder import build_image_scene, build_sequence


def build_product_sequence(
    images,
    total_duration=15,
    size=(1280, 720),
    transition_duration=0.6,
    ken_burns_start=1.0,
    ken_burns_end=1.08,
):
    if not images:
        raise ValueError("Aucune image produit fournie.")

    valid_images = [
        str(Path(image))
        for image in images
        if Path(image).is_file()
    ]

    if not valid_images:
        raise FileNotFoundError("Aucune image produit valide trouvée.")

    scene_count = len(valid_images)

    scene_duration = (
        total_duration + (scene_count - 1) * transition_duration
    ) / scene_count

    scenes = []

    for image in valid_images:
        scenes.append(
            build_image_scene(
                image,
                duration=scene_duration,
                size=size,
                ken_burns_start=ken_burns_start,
                ken_burns_end=ken_burns_end,
            )
        )

    return build_sequence(
        scenes,
        transition_duration=transition_duration,
    )
