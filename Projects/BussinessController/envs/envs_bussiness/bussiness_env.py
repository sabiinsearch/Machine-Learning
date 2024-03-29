import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding

class BussinessEnv(gym.Env):

    def __init__(self):
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Dict({'phase':spaces.Box(low=0, high=1, shape=(4,1,3), dtype=np.float32),
                                            'vehicle':spaces.Box(low=0, high=14, shape=(29,29,2), dtype=np.float32)})
        print('Bussiness Environment initialized')

    def step(self):
        print('Step successful for Bussiness Environment!')

    def reset(self):
        print('Bussiness Environment reset')
