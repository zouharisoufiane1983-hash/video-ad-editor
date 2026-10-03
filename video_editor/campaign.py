from pathlib import Path

from video_editor.product_sequence import build_product_sequence
from video_editor.branding import add_image, add_text
from video_editor.effects import fade_in, fade_out
from video_editor.audio import load_audio, fit_audio_to_duration, add_audio
from video_editor.export import export_video
from video_editor.presets import get_preset
from video_editor.formats import get_format
from video_editor.product_loader import load_product_images


def create_campaign(
    output,
    products,
    logo=None,
    music=None,
    title="DAR GHIZLANE",
    subtitle="L'élégance marocaine au quotidien",
    duration=15,
    size=None,
    preset="luxury",
    transition_duration=0.6,
    format_name="landscape",
):
    if not products:
        raise ValueError("Aucun produit fourni.")

    if isinstance(products, (str, Path)):
        products = load_product_images(products)

    if size is None:
        size = get_format(format_name)["size"]

    width, height = size
    style = get_preset(preset)

    valid_products = [
        str(Path(product))
        for product in products
        if Path(product).is_file()
    ]

    if not valid_products:
        raise FileNotFoundError("Aucun produit valide trouvé.")

    video = build_product_sequence(
        valid_products,
        total_duration=duration,
        size=size,
        transition_duration=transition_duration,
        ken_burns_start=style["ken_burns_start"],
        ken_burns_end=style["ken_burns_end"],
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
        position=("center", height - 160),
    )

    video = add_text(
        video,
        subtitle,
        font_size=style["subtitle_size"],
        color="white",
        position=("center", height - 85),
    )

    video = fade_in(video, style["fade_in"])
    video = fade_out(video, style["fade_out"])

    audio = None

    if music and Path(music).is_file():
        audio = load_audio(music)
        audio = fit_audio_to_duration(audio, video.duration)
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
