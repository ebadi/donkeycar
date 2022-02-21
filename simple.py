import gym
import numpy as np
import gym_donkeycar

env = gym.make("donkey-warren-track-v0")

obs = env.reset()
try:
    for _ in range(100):
        action = np.array([0.0, 0.5])  
        obs, reward, done, info = env.step(action)
        print(obs)
except KeyboardInterrupt:
    pass
env.close()
