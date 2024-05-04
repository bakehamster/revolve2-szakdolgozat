import numpy as np
from typing import List
from scipy.spatial.transform import Rotation as R

class DeformableBody:
    def __init__(self, initial_pose: np.ndarray, mass: float, material_properties: dict):
        self.initial_pose = initial_pose
        self.mass = mass
        self.material_properties = material_properties
        self.nodes = []  # List of nodes defining the geometry
        self.elements = []  # List of elements connecting nodes

    def add_node(self, position: np.ndarray):
        self.nodes.append(position)

    def add_element(self, node_indices: List[int]):
        self.elements.append(node_indices)

    def calculate_inertia_tensor(self):
        # Calculate the inertia tensor based on the geometry of the deformable body

        inertia_tensor = np.zeros((3, 3))

        for element in self.elements:
            # Get the nodes of the element
            node_positions = [self.nodes[i] for i in element]

            # Calculate the centroid of the element
            centroid = np.mean(node_positions, axis=0)

            # Calculate the moment of inertia of the element around its centroid
            element_inertia = self.calculate_element_inertia(node_positions, centroid)

            # Translate the element's inertia to the global coordinate system
            inertia_tensor += self.translate_inertia_to_global(element_inertia, centroid)

        return inertia_tensor

    def calculate_element_inertia(self, node_positions: List[np.ndarray], centroid: np.ndarray):
        # Calculate the moment of inertia of an element around its centroid
        # This is a simplified calculation, actual deformation effects may require more complex models

        element_inertia = np.zeros((3, 3))

        for node_position in node_positions:
            # Calculate the distance of the node from the centroid
            r = node_position - centroid

            # Use the parallel axis theorem to calculate the moment of inertia
            element_inertia[0, 0] += self.mass * (r[1]**2 + r[2]**2)
            element_inertia[1, 1] += self.mass * (r[0]**2 + r[2]**2)
            element_inertia[2, 2] += self.mass * (r[0]**2 + r[1]**2)

        return element_inertia

    def translate_inertia_to_global(self, element_inertia: np.ndarray, centroid: np.ndarray):
        # Translate the inertia of an element to the global coordinate system
        # by considering its position relative to the global frame

        rotation_matrix = R.from_euler('xyz', self.initial_pose[3:]).as_matrix()
        translation_matrix = np.eye(3)
        translation_matrix[:3, 3] = self.initial_pose[:3]

        global_inertia = rotation_matrix @ element_inertia @ rotation_matrix.T
        global_inertia += np.linalg.norm(centroid) ** 2 * np.eye(3) * self.mass

        return global_inertia

# Example usage:
initial_pose = np.array([0, 0, 0, 0, 0, 0])  # Initial pose (position and orientation)
mass = 1.0  # Mass of the deformable body
material_properties = {'young_modulus': 1e6, 'poisson_ratio': 0.3}  # Material properties

deformable_body = DeformableBody(initial_pose, mass, material_properties)

# Add nodes and elements to define the geometry of the deformable body
deformable_body.add_node(np.array([0, 0, 0]))
deformable_body.add_node(np.array([1, 0, 0]))
deformable_body.add_node(np.array([1, 1, 0]))
deformable_body.add_element([0, 1, 2])

# Calculate the inertia tensor of the deformable body
inertia_tensor = deformable_body.calculate_inertia_tensor()
print("Inertia Tensor:")
print(inertia_tensor)
