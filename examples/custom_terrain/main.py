"""Main script for the example."""


from pyrr import Quaternion, Vector3
from revolve2.ci_group.simulation_parameters import make_standard_batch_parameters
from revolve2.experimentation.logging import setup_logging
from revolve2.experimentation.rng import make_rng_time_seed
from revolve2.modular_robot import ModularRobot
from revolve2.modular_robot.brain.cpg import BrainCpgNetworkNeighborRandom
from revolve2.modular_robot_simulation import Terrain, simulate_scenes, ModularRobotScene
from revolve2.simulation.scene import Pose, Color, AABB
from revolve2.simulation.scene.geometry import GeometryPlane, GeometryBox
from revolve2.simulation.scene.geometry.textures import Texture
from revolve2.simulators.mujoco_simulator.textures import Checker
from revolve2.ci_group.modular_robots_v2 import gecko_v2

from simulation.revolve2.simulation.scene.geometry.textures import MapType
from simulators.mujoco_simulator.revolve2.simulators.mujoco_simulator import LocalSimulator


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
                texture=Texture(
                    primary_color=Color(100, 150, 0, 50)
                ),
                aabb=AABB(Vector3([1.0, 1.0, 0.15]))
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
    body = gecko_v2()
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
