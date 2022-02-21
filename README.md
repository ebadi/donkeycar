```
git clone https://github.com/DLR-RM/stable-baselines3.git
git clone https://github.com/DLR-RM/rl-baselines3-zoo.git
git checkout feat/offline-RL
https://github.com/tawnkramer/gym-donkeycar.git

python3.8 -m venv env
source env/bin/activate

git clone https://github.com/autorope/donkeycar.git
donkeycar$ pip3.8 install -e .[pc]

donkey createcar --path /home/wave/DonkeyCar/mysim
cd /home/wave/DonkeyCar/mysim

myconfig.py
DONKEY_GYM = True
DONKEY_SIM_PATH = "/home/wave/DonkeyCar/DonkeySimLinux/donkey_sim.x86_64"
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"


cd mysim
python3.8 manage.py drive
donkey train --tub ./data --model models/mypilot.h5
python3.8 manage.py drive --model=models/mypilot.h5



git clone https://github.com/tawnkramer/gym-donkeycar.git
pip3.8 install -e .


sudo apt-get install python3.8
sudo apt-get install python3.8-venv

pip3.8 install   Cython
python3.8  -m venv env
source env/bin/activate

install tensorflow-gpu==2.2.0
pip3.8  install numpy
pip3.8  install pybind11
pip3.8  install wheel
pip3.8 install  stable-baselines3
pip3.8 install sb3-contrib
pip3.8 install pyyaml
pip3.8 install seaborn
pip3.8 install  tempita
pip3.8 install  pythran
pip3.8 install  optuna
pip3.8 install  zmq
pip3.8 install  gym_donkeycar
pip3.8 install  tensorboard
pip3.8 install https://github.com/Stable-Baselines-Team/stable-baselines3-contrib
pip3.8 install opencv-python
pip3.8 install scikit-build
pip3.8 install pygame
pip3.8 install imgaug
pip3.8 install torchvision
pip3.8 install joblib
pip3.8 install  pkgconfig
sudo apt-get install libatlas-base-dev
```


```
(env) wave@wave:~/DonkeyCar/aae-train-donkeycar$ python3.8 record_data.py 
# update ~/DonkeyCar/aae-train-donkeycar/config.py:

CAMERA_HEIGHT = 120
CAMERA_WIDTH = 160

# training auto encoder
(env) wave@wave:~/DonkeyCar/aae-train-donkeycar$ python3.8 -m ae.train_ae --n-epochs 100 --batch-size 8 --z-size 32 -f logs/carracing_2/ --verbose 0
(env) wave@wave:~/DonkeyCar/aae-train-donkeycar$ python3.8 -m ae.train_ae -ae logs/ae-32_1643370355_best.pkl -f logs/dataset_mountain/

# Training RL
export AE_PATH=/home/wave/DonkeyCar/aae-train-donkeycar/logs/ae-32_1643370355_best.pkl
python3.8 train.py --algo tqc --env donkey-mountain-track-v0 --eval-freq -1 --save-freq 20000

```

https://www.youtube.com/watch?v=ngK33h00iBE


