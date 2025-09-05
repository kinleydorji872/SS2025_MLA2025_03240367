import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

print(f"Action Space: {env.action_space}")
print(f"Observation Space: {env.observation_space}")

# --- THE MAIN LOOP ---

# 1. RESET the environment
# This function is called at the beginning of every new episode.
# It returns the initial observation and some optional info.
observation, info = env.reset()

# Initialize variables to track the episode's progress
terminated = False
truncated = False
total_reward = 0.0

# The loop continues as long as the episode is not finished.
while not terminated and not truncated:
    # 2. RENDER the environment (optional)
    # This displays the current state in the popup window.
    env.render()

    # 3. CHOOSE an action
    # For now, we select a completely random action from the action space.
    action = env.action_space.sample()
    print(f"Taking action: {action} (0:L, 1:D, 2:R, 3:U)")

    # 4. STEP the environment
    # This is the most important function. It executes the chosen action.
    # It returns five crucial pieces of information:
    #   next_observation: The agent's new location.
    #   reward: The reward obtained from the last action. For FrozenLake, this is 1.0 if we reach the goal 'G', and 0.0 otherwise.
    #   terminated: A boolean. True if the episode ended because of a terminal state (reaching 'G' or falling in 'H').
    #   truncated: A boolean. True if the episode ended for another reason (e.g., a time limit was reached).
    #   info: A dictionary for debugging info, which we can ignore for now.
    next_observation, reward, terminated, truncated, info = env.step(action)

    # Update our tracking variables
    total_reward += reward
    observation = next_observation
1
    # Add a small delay to make the visualization easier to follow
time.sleep(5)

# After the loop, the episode is finished.
print(f"\nEpisode finished! Total Reward: {total_reward}")

# 5. CLOSE the environment
# This is important for cleaning up resources, especially the rendering window.
env.close()

#Answer these questions in comments in your code:
#What type of space is the action space? How many actions are there?
#ANSWER; It is discrete(2) and only two action space (1:right,0:left)

#What type of space is the observation space? The output is Box(4,). This represents a continuous space with 4 numbers. Based on the problem, what could these four numbers possibly represent?
# ANSWER: The four continous space are:
#1.Cart position : How far the cart is from centre.
#2.Cart velocity: How fast the cart is moving either left or right.
#3.Pole angle : How titled the pole is .
#4.Pole angular velocity: How fast the pole is rotating.

#Run the random agent for one episode. What does the reward seem to represent in this environment? (Hint: you get a reward for every step the pole remains balanced)
# ANSWER; For every epsiode when the pole is balance, the reward of one point is given.
#reward=1
#total_reward + = reward
