from pathlib import Path

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def load_product_images(folder):
    folder = Path(folder)

    if not folder.is_dir():
        raise FileNotFoundError(f"Dossier produits introuvable : {folder}")

    images = sorted(
        (
            path
            for path in folder.iterdir()
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
        ),
        key=lambda path: path.name.lower(),
    )

    if not images:
        raise FileNotFoundError(
            f"Aucune image produit trouvée dans : {folder}"
        )

    return [str(path) for path in images]
