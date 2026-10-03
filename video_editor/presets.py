PRESETS = {
    "luxury": {
        "background": (12, 12, 12),
        "title_size": 72,
        "subtitle_size": 36,
        "ken_burns_start": 1.0,
        "ken_burns_end": 1.06,
        "fade_in": 0.8,
        "fade_out": 0.8,
    },
    "moroccan": {
        "background": (24, 16, 12),
        "title_size": 68,
        "subtitle_size": 34,
        "ken_burns_start": 1.0,
        "ken_burns_end": 1.08,
        "fade_in": 0.7,
        "fade_out": 0.7,
    },
    "ecommerce": {
        "background": (18, 18, 18),
        "title_size": 64,
        "subtitle_size": 32,
        "ken_burns_start": 1.0,
        "ken_burns_end": 1.10,
        "fade_in": 0.5,
        "fade_out": 0.5,
    },
    "tiktok": {
        "background": (10, 10, 10),
        "title_size": 62,
        "subtitle_size": 30,
        "ken_burns_start": 1.0,
        "ken_burns_end": 1.12,
        "fade_in": 0.35,
        "fade_out": 0.35,
    },
}

def get_preset(name="luxury"):
    if name not in PRESETS:
        raise ValueError(
            f"Preset inconnu : {name}. "
            f"Disponibles : {', '.join(PRESETS)}"
        )
    return PRESETS[name]
