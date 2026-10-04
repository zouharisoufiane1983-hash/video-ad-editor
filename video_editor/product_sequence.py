from pathlib import Path

from video_editor.scene_builder import build_image_scene, build_sequence


def build_product_sequence(
    images,
    total_duration=None,
    size=(1280, 720),
    transition_duration=0.6,
    ken_burns_start=1.0,
    ken_burns_end=1.08,
    product_durations=None,
    seconds_per_product=7.0,
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

    if product_durations is not None:
        if len(product_durations) != scene_count:
            raise ValueError(
                f"Il faut {scene_count} durees, une par produit."
            )

        requested_durations = [float(duration) for duration in product_durations]

        if any(duration <= 0 for duration in requested_durations):
            raise ValueError("Chaque duree produit doit etre superieure a 0.")

        scene_durations = [
            duration + transition_duration if index < scene_count - 1 else duration
            for index, duration in enumerate(requested_durations)
        ]

    elif total_duration is not None:
        scene_duration = (
            total_duration + (scene_count - 1) * transition_duration
        ) / scene_count
        scene_durations = [scene_duration] * scene_count

    else:
        requested_durations = [float(seconds_per_product)] * scene_count
        scene_durations = [
            duration + transition_duration if index < scene_count - 1 else duration
            for index, duration in enumerate(requested_durations)
        ]

    scenes = []

    for image, scene_duration in zip(valid_images, scene_durations):
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


def calculate_auto_duration(
    product_count,
    seconds_per_product=7.5,
    min_duration=5.0,
    max_duration=60.0,
):
    if product_count <= 0:
        raise ValueError("Le nombre de produits doit être supérieur à 0.")

    duration = product_count * seconds_per_product

    return max(min_duration, min(max_duration, duration))
