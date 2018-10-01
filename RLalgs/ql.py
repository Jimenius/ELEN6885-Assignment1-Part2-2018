import numpy as np
from RLalgs.utils import epsilon_greedy
import random

def QLearning(env, num_episodes, gamma, lr, e):
    """
    Implement the Q-learning algorithm following the epsilon-greedy exploration. Update Q at the end of every episode.

    Inputs:
    

    Outputs:
    Q: numpy.ndarray
    """

    Q = np.zeros((env.nS, env.nA))
    
    ############################
    # YOUR CODE STARTS HERE

    # YOUR CODE ENDS HERE
    ############################

    return Q