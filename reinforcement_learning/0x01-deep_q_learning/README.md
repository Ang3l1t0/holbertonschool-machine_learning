# 0x01. Deep Q-learning

## Installing Keras-RL

```
pip install --user keras-rl
```

## Dependencies (that should already be installed)

```
pip install --user keras==2.2.5
pip install --user Pillow
pip install --user h5py
```

## Tasks

### [0. Breakout](./train.py)

Write a python script `train.py` that utilizes `keras`, `keras-rl`, and `gym` to train an agent that can play Atari’s Breakout:

- Your script should utilize `keras-rl`‘s `DQNAgent`, `SequentialMemory`, and `EpsGreedyQPolicy`
- Your script should save the final policy network as `policy.h5`

Write a python script `play.py` that can display a game played by the agent trained by `train.py`:

- Your script should load the policy network saved in `policy.h5`
- Your agent should use the `GreedyQPolicy`

---
