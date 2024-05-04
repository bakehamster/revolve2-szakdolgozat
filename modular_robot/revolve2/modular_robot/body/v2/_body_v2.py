from pyrr import Vector3

from .. import RightAngles
from ..base._body import Body
from ._core_v2 import CoreV2


class BodyV2(Body):
    """Body of a V1 modular robot."""

    _core: CoreV2

    def __init__(self, rotation: float | RightAngles = RightAngles.DEG_0, bounding_box: Vector3 | None = None) -> None:
        """Initialize the Body."""
        super().__init__(CoreV2(rotation, bounding_box))

    @property
    def core_v2(self) -> CoreV2:
        """
        Get the specific v2 core of the body.

        :return: The v2 core.
        """
        return self._core
