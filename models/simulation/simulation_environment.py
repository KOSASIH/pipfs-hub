# Import necessary libraries
import gym
import pybullet as p
import time
import pybullet_data

# Define a class for simulation environments
class SimulationEnvironment:
    def __init__(self, config_path):
        # Load configuration from file
        with open(config_path) as f:
           config = json.load(f)
        self.config = config

        # Initialize the simulation environment
        self.simulation = gym.make(self.config['simulation']['name'])

    def reset(self):
        # Reset the simulation environment
        state = self.simulation.reset()
        return state

    def step(self, action):
        # Step the simulation environment
        state, reward, done, info = self.simulation.step(action)
        return state, reward, done, info

    def render(self):
        # Render the simulation environment
        self.simulation.render()

    def close(self):
        # Close the simulation environment
        self.simulation.close()

    def setup_pybullet(self):
        # Set up the PyBullet physics engine
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -10)
        p.setTimeStep(1./240.)
        p.setRealTimeSimulation(1)
