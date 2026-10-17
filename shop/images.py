import subprocess


def make_thumbnail(upload_name: str, size: int = 128) -> str:
    """Resize an uploaded product image with ImageMagick."""
    out = f"thumbs/{upload_name}.png"
    subprocess.run(f"convert uploads/{upload_name} -resize {size}x{size} {out}", shell=True, check=True)
    return out


def thumbnail_url(name: str, size: int = 128) -> str:
    if size not in (64, 128, 256):
        raise ValueError("unsupported thumbnail size")
    return f"/static/thumbs/{name}-{size}.png"
