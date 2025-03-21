#!/usr/bin/env python3
"""
Monte Carlo algorithm - Corrected Version
"""
import numpy as np

def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.2,
                gamma=0.99):
    """
    Monte Carlo algorithm for estimating state values.

    Parameters:
        env: Environment instance.
        V: numpy.ndarray of shape (s,) containing the value estimates.
        policy: Function that takes a state and returns an action.
        episodes: Number of episodes to train.
        max_steps: Max number of steps per episode.
        alpha: Learning rate.
        gamma: Discount factor.

    Returns:
        Updated value estimates V.
    """
    for _ in range(episodes):
        state, _ = env.reset()  # Reset environment
        episode_data = []  # Store (state, reward) tuples

        for _ in range(max_steps):
            action = policy(state)  
            next_state, reward, done, _, _ = env.step(action)  
            episode_data.append((state, reward))  

            if done:
                break  
            state = next_state  

        G = 0  
        visited_states = set()  

        for state, reward in reversed(episode_data):
            G = gamma * G + reward  

            # Convert state to a usable index if necessary
            if isinstance(state, tuple):
                state = hash(state) % len(V)  

            if state not in visited_states:  
                visited_states.add(state)
                V[state] += alpha * (G - V[state])  

    np.set_printoptions(precision=4, suppress=True)
    return V.round(4)
