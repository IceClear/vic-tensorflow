from __future__ import print_function

from experiments.grid_world_exp import GridWorldExperiment
import time

n_trajectories = 3
if __name__ == "__main__":
    runner = GridWorldExperiment()
    runner.train(n_episodes=1000)  # TODO: pickle/load the results of experiment

    # x = input("Enter to proceed")
    for omega in range(runner.n_options):
        print("\noption", omega, "\n=============")
        for traj in range(n_trajectories):
            print("epsilon", runner.policy.epsilon)
            runner.rollout(omega, render=False)
            print("trajectory", traj, "final state", runner.env.state)
