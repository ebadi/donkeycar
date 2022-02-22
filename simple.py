import gym
import numpy as np
import gym_donkeycar
import cv2
env = gym.make("donkey-warren-track-v0")

obs = env.reset()
try:
    for _ in range(1000):
        action = np.array([0.5, 0.5])  
        obs, reward, done, info = env.step(action)
        # print(obs)
        print(type(obs))
        cv2.imshow("window name", obs[:, :, ::])
        cv2.waitKey(-1)
except KeyboardInterrupt:
    pass
env.close()
