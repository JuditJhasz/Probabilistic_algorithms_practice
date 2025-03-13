import random

def longest_heads_streak_single_experiment():
    streak = 0
    while random.choice(["H", "T"]) == "H":
        streak += 1
    return streak

def run_experiments(n):
    return max(longest_heads_streak_single_experiment() for _ in range(n))

def averaged_experiments(k, n):
    total_streaks = [run_experiments(n) for _ in range(k)]
    return sum(total_streaks) / k

# Example usage
n = int(input("Enter number of experiments: "))
k_option = input("Do you want to average over multiple runs? (y/n): ")
if k_option.lower() == "y":
    k = int(input("Enter number of runs for averaging: "))
    avg_streak = averaged_experiments(k, n)
    print(f"Average longest streak over {k} runs of {n} experiments each: {avg_streak:.2f}")
else:
    streak = run_experiments(n)
    print(f"Longest streak in {n} experiments: {streak}")
