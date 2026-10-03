FORMATS = {
    "landscape": {
        "size": (1280, 720),
        "label": "16:9",
        "platforms": ["youtube", "facebook"],
    },
    "vertical": {
        "size": (720, 1280),
        "label": "9:16",
        "platforms": ["tiktok", "instagram_reels", "instagram_stories"],
    },
    "square": {
        "size": (1080, 1080),
        "label": "1:1",
        "platforms": ["instagram_feed", "facebook_feed"],
    },
}


def get_format(name="landscape"):
    if name not in FORMATS:
        raise ValueError(
            f"Format inconnu : {name}. "
            f"Disponibles : {', '.join(FORMATS)}"
        )

    return FORMATS[name]
