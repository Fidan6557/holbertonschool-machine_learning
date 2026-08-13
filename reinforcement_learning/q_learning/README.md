# Q-Learning

This directory contains a tabular Q-learning agent for Gymnasium's
`FrozenLake-v1` environment. The project covers environment creation,
Q-table initialization, epsilon-greedy action selection, agent training, and
greedy policy evaluation.

## Learning Objectives

By the end of this project, you should be able to explain:

- What reinforcement learning, states, actions, and rewards are
- How a Q-table represents the expected value of state-action pairs
- The difference between exploration and exploitation
- How an epsilon-greedy policy selects actions
- How the Bellman equation is used to update Q-values
- How the learning rate, discount factor, and epsilon affect training
- How to train and evaluate a Q-learning agent in Gymnasium

## Algorithm

For each transition from state `s` to state `s'` after taking action `a`, the
Q-value is updated as follows:

```text
Q(s, a) <- Q(s, a) + alpha *
           (reward + gamma * max(Q(s', a')) - Q(s, a))
```

where:

- `alpha` is the learning rate
- `gamma` is the discount factor for future rewards
- `epsilon` is the probability of choosing a random action

During training, landing in a hole receives a reward of `-1`. Epsilon decays
linearly after every episode until it reaches `min_epsilon`.

## Files

| File | Description |
| --- | --- |
| `0-load_env.py` | Creates a `FrozenLake-v1` environment with ANSI rendering. |
| `1-q_init.py` | Initializes a zero-filled Q-table from the environment's state and action spaces. |
| `2-epsilon_greedy.py` | Chooses an action using an epsilon-greedy policy. |
| `3-q_learning.py` | Trains the agent and returns the updated Q-table and reward history. |
| `4-play.py` | Runs a greedy policy and returns the total reward and rendered frames. |

## Function Reference

### `load_frozen_lake(desc=None, map_name=None, is_slippery=False)`

Creates and returns a Gymnasium Frozen Lake environment. A custom map can be
provided with `desc`, or a built-in map such as `"4x4"` or `"8x8"` can be
selected with `map_name`.

### `q_init(env)`

Returns a NumPy array of zeros with the shape
`(number_of_states, number_of_actions)`.

### `epsilon_greedy(Q, state, epsilon)`

Returns a random action with probability `epsilon`; otherwise, it returns the
action with the highest Q-value for the current state.

### `train(...)`

```python
train(
    env,
    Q,
    episodes=5000,
    max_steps=100,
    alpha=0.1,
    gamma=0.99,
    epsilon=1,
    min_epsilon=0.1,
    epsilon_decay=0.05,
)
```

Trains the agent and returns `(Q, total_rewards)`, where `Q` is the updated
Q-table and `total_rewards` contains the reward earned in each episode.

### `play(env, Q, max_steps=100)`

Runs the learned greedy policy and returns `(total_reward, rendered_outputs)`.
The rendered output list contains the initial frame and one frame after each
action.

## Requirements

- Python 3
- NumPy
- Gymnasium with the Toy Text environments

Install the dependencies with:

```bash
pip install numpy "gymnasium[toy-text]"
```

## Usage

Run the following example from this directory:

```python
load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init
train = __import__('3-q_learning').train
play = __import__('4-play').play

env = load_frozen_lake(map_name="4x4", is_slippery=False)
Q = q_init(env)
Q, rewards = train(env, Q)

total_reward, frames = play(env, Q)
print("Learned Q-table:\n", Q)
print("Total reward:", total_reward)

for frame in frames:
    print(frame)

env.close()
```

In Frozen Lake, the agent can choose one of four discrete actions:

| Value | Action |
| --- | --- |
| `0` | Move left |
| `1` | Move down |
| `2` | Move right |
| `3` | Move up |

The goal is to navigate from the starting tile (`S`) to the goal (`G`) without
falling into a hole (`H`). Frozen tiles are represented by `F`.
