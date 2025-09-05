MLA202 Reinforcement Learning
Kinley Dorji
03240367
MLA202

#Reflection
#A brief summary of the tasks you completed?
#answer:In compliance with Exercise 1, I modified the given FrozenLake code and printed the action space and observation space.   In exercise 2, I created an outside loop to execute the code a thousand times.   I used a while loop because we know how many times the loop will run.   Additionally, I created a variable called num_episode to record which track the function is executing on.   I have also removed time to speed up the code env.render(), print(), and sleep().

#The answers to the questions from Exercise 1 about the CartPole environment's action and observation spaces.
#answer:# The four continous space are:
#1.Cart position : How far the cart is from centre.
#2.Cart velocity: How fast the cart is moving either left or right.
#3.Pole angle : How titled the pole is .
#4.Pole angular velocity: How fast the pole is rotating.

#The final average reward you calculated for the random agent in Exercise 2.
#answer:![alt text](<Screenshot (32).png>)
# Total reward is 47

#A section on challenges: What was the most difficult part of this practical for you? (e.g., setting up the environment, understanding the step function's return values, structuring the loops).
#ANSWER: The hardest part of this practical was understanding the step() function's return values and using them in the loop. I wasn't sure how to handle the information, truncation, termination, reward, and observation values, so at first the episode flowed badly. Making sure the loop ended at the right time was another difficult task. In order to see how each value behaved, I fixed this by reading the handbook, looking over the examples, and printing the results.

#A section on key takeaways: What is the most important or surprising thing you learned?
# ANSWER; The most important thing I learnt from this practical was how the step() method controls the agent-environment interaction.   I was astounded by the volume of information that was returned in a single call and the role that each element plays in managing the episode.   Another unexpected finding was that, even after 1000 iterations of the while loop, the average total reward stayed low.   It showed me that the agent does not automatically improve with more runs and that proper learning strategies are needed to achieve better results.
