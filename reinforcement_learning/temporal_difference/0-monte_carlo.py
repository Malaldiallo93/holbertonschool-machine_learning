#!/usr/bin/env python3
"""
    Monte Carlo algorithm
"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                alpha=0.1, gamma=0.99):
    """
        Function that performs the Monte Carlo algorithm

    :param env: openAI gym environment instance
    :param V: ndarray, shape(s,), value function estimate
    :param policy: function that takes in a state and returns the next action
    :param episodes: total number of episodes to train over
    :param max_steps: max number of steps per episode
    :param alpha: learning rate
    :param gamma: discount rate

    :return: V, updated value estimate
    """
    for ep in range(episodes):
        # Reset environment
        state, _ = env.reset()

        episode_data = []
        visited_states = set()  # To track first visits

        for _ in range(max_steps):
            action = policy(state)
            next_state, reward, done, _, _ = env.step(action)  # Ensure correct unpacking
            episode_data.append((state, reward))

            if done:
                break

            state = next_state

        G = 0
        # Reverse iteration for Monte Carlo returns
        for state, reward in reversed(episode_data):
            G = gamma * G + reward
            if state not in visited_states:
                visited_states.add(state)
                V[state] += alpha * (G - V[state])

    np.set_printoptions(precision=4, suppress=True)

    return V.round(4)
