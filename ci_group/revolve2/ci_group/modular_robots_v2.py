"""Standard modular robots."""
import numpy as np
from pyrr import Vector3

from revolve2.modular_robot.body import RightAngles
from revolve2.modular_robot.body.v2 import ActiveHingeV2, BodyV2, BrickV2


def all() -> list[BodyV2]:
    """
    Get a list of all standard module robots.

    :returns: The list of robots.
    """
    return [
        gecko_v2(),
    ]


def get(name: str) -> BodyV2:
    """
    Get a robot by name.

    :param name: The name of the robot to get.
    :returns: The robot with that name.
    :raises ValueError: When a robot with that name does not exist.
    """
    match name:
        case "gecko":
            return gecko_v2()
        case _:
            raise ValueError(f"Robot does not exist: {name}")


def gecko_v2() -> BodyV2:
    """
    Sample robot with new HW config.

    :returns: the robot
    """
    body = BodyV2()

    body.core_v2.right_face.bottom = ActiveHingeV2(0.0)
    body.core_v2.right_face.bottom.attachment = BrickV2(0.0)

    body.core_v2.left_face.bottom = ActiveHingeV2(0.0)
    body.core_v2.left_face.bottom.attachment = BrickV2(0.0)

    body.core_v2.back_face.bottom = ActiveHingeV2(np.pi / 2.0)
    body.core_v2.back_face.bottom.attachment = BrickV2(-np.pi / 2.0)
    body.core_v2.back_face.bottom.attachment.front = ActiveHingeV2(np.pi / 2.0)
    body.core_v2.back_face.bottom.attachment.front.attachment = BrickV2(-np.pi / 2.0)
    body.core_v2.back_face.bottom.attachment.front.attachment.left = ActiveHingeV2(0.0)
    body.core_v2.back_face.bottom.attachment.front.attachment.right = ActiveHingeV2(0.0)
    body.core_v2.back_face.bottom.attachment.front.attachment.left.attachment = BrickV2(
        0.0
    )
    body.core_v2.back_face.bottom.attachment.front.attachment.right.attachment = (
        BrickV2(0.0)
    )

    return body


def darts_robot() -> BodyV2:
    """
    Sample robot with new HW config.

    :returns: the robot
    """
    bounding_box = Vector3([0.35, 0.15, 0.35])
    body = BodyV2(RightAngles.DEG_270, bounding_box=bounding_box)

    body.core_v2.right_face.middle = ActiveHingeV2(0.0)
    body.core_v2.right_face.middle.attachment = ActiveHingeV2(0.0)
    body.core_v2.right_face.middle.attachment.attachment = ActiveHingeV2(0.0)
    body.core_v2.right_face.middle.attachment.attachment.attachment = ActiveHingeV2(0.0)
    body.core_v2.right_face.middle.attachment.attachment.attachment.attachment = ActiveHingeV2(0.0)
    lower_part = body.core_v2.right_face.middle.attachment.attachment.attachment.attachment.attachment = ActiveHingeV2(0.0)

    lower_part.attachment = BrickV2(0.0)

    return body