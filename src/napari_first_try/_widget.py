from pathlib import Path
from typing import List

import napari
from magicgui import magic_factory
from napari.layers import Image
from napari.types import ImageData, LabelsData, LayerDataTuple


@magic_factory(call_button="Add Image")
def rand_img(
    new_image: bool,
    ny: int = 64,
    nx: int = 64,
) -> LayerDataTuple:
    # If you return Image then you get a new Layer every time
    # If you return ImageData and just the np array, then you get
    # a new layer the first time, and then it's refreshed
    import numpy as np

    i = 1
    if new_image is True:
        return (
            np.random.randint(0, 256, size=(ny, nx)),
            {"name": "Random Image"},
            "image",
        )
    else:
        return (np.random.randint(0, 256, size=(ny, nx)), {}, "Random Image")


@magic_factory(
    auto_call=True,
    threshold={"widget_type": "Slider", "min": 0, "max": 2 ** 8},
)
def thresh_img(data: ImageData, threshold: int) -> LabelsData:
    # Because this returns LabelsData it makes a new layer
    # just the first time, then just changes the labeling
    # in response to the slider.
    return (data > threshold).astype(int)



def on_init(new_widget):
    """called each time widget_factory creates a new widget."""

    @new_widget.choice.changed.connect
    def _on_image_path_changed(choice):
        print(choice)


@magic_factory(widget_init=on_init, choice={"choices": ["A", "B", "C"]})
def widget_factory(
    # viewer: "napari.viewer.Viewer",
    image: ImageData,
    choice: str,
) -> "napari.types.LabelsData":
    print(choice)
    pass