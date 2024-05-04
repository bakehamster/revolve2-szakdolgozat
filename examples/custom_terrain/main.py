"""Main script for the example."""


from pyrr import Quaternion, Vector3

from revolve2.ci_group.revolve2.ci_group.modular_robots_v2 import darts_robot
from revolve2.modular_robot_simulation.revolve2.modular_robot_simulation import Terrain
from revolve2.simulation.revolve2.simulation.scene import Pose, Color
from revolve2.simulation.revolve2.simulation.scene.geometry import GeometryPlane, GeometryBox, GeometryCylinder
from revolve2.simulation.revolve2.simulation.scene.geometry.textures import MapType
from revolve2.simulators.mujoco_simulator.revolve2.simulators.mujoco_simulator.textures import Checker, Flat


def make_custom_terrain() -> Terrain:
    """
    Create a custom terrain.

    :returns: The created terrain.
    """
    # A terrain is a collection of static geometries.
    # Here we create a simple terrain uses some boxes.
    return Terrain(
        static_geometry=[
            GeometryPlane(
                pose=Pose(position=Vector3(), orientation=Quaternion()),
                mass=0.0,
                size=Vector3([20.0, 20.0, 0.0]),
                texture=Checker(
                    primary_color=Color(170, 170, 180, 255),
                    secondary_color=Color(150, 150, 150, 255),
                    map_type=MapType.MAP2D,
                ),
            ),
            GeometryBox(
                pose=Pose(position=Vector3([0.0, 4.1, 0.5]), orientation=Quaternion.from_x_rotation(-90)),
                mass=0.0,
                texture=Flat(
                    primary_color=Color(100, 150, 0, 50)
                ),
                aabb=AABB(Vector3([1.0, 1.0, 0.15]))
            ),
            GeometryCylinder(
                pose=Pose(position=Vector3([0.0, 4, 0.515]), orientation=Quaternion.from_x_rotation(-90)),
                mass=0.0,
                texture=Flat(
                    primary_color=Color(0, 255, 0, 255)
                ),
                size=Vector2((1, 0.025))
            )
        ]
    )


def main() -> None:
    """Run the simulation."""
    # Set up logging.
    setup_logging()

    # Set up the random number generator.
    rng = make_rng_time_seed()

    # Create a robot
    body = darts_robot()
    brain = BrainCpgNetworkNeighborRandom(body=body, rng=rng)
    robot = ModularRobot(body, brain)

    # Create the scene.
    scene = ModularRobotScene(terrain=make_custom_terrain())
    scene.add_robot(robot, pose=Pose(Vector3([0.0, 0.0, 0.0])))

    # Simulate the scene.
    simulator = LocalSimulator()
    simulate_scenes(
        simulator=simulator,
        batch_parameters=make_standard_batch_parameters(),
        scenes=scene,
    )


if __name__ == "__main__":
    main()
