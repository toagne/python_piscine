from PIL import Image
import numpy as np
from pathlib import Path

def ft_load(path: str) -> np.ndarray:
    """
    1) Loads an image from `path`.
    2) Converts it to an array.
    3) Prints the shape of the array.
    4) Prints out each pixel’s (R, G, B) tuple.
    """
    p = Path(path)
    if p.suffix not in {'.jpg', '.jpeg'}:
        raise ValueError(f"Unsupported extension {p.suffix!r}; only .jpg/.jpeg allowed.")
    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path!r}")
    arr = np.array(img)
    # print(f'The shape of image is: {arr.shape}')
    return arr