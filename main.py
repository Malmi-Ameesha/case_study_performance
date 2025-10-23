import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
RANDOM_SEED = 42
SIM_TIME = 480  # minutes (8 hours)
arrival_rate = 1 / 5  # average 1 call every 5 minutes
service_time_mean = 5  # average service time = 5 minutes
num_agents_list = [3, 4, 6]  # 3 scenarios

# Results storage
results = {}

# Define Call Center
class CallCenter:
    def __init__(self, env, num_agents):
        self.env = env
        self.agents = simpy.Resource(env, num_agents)
        self.wait_times = []
        self.queue_lengths = []

    def handle_call(self, name, service_time):
        arrival_time = self.env.now
        self.queue_lengths.append(len(self.agents.queue))
        with self.agents.request() as request:
            yield request
            wait = self.env.now - arrival_time
            self.wait_times.append(wait)
            yield self.env.timeout(random.expovariate(1 / service_time))

# Generate calls
def call_generator(env, call_center, arrival_rate, service_time):
    i = 0
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        i += 1
        env.process(call_center.handle_call(f"Call {i}", service_time))

# Run simulation
def run_simulation(num_agents):
    env = simpy.Environment()
    cc = CallCenter(env, num_agents)
    env.process(call_generator(env, cc, arrival_rate, service_time_mean))
    env.run(until=SIM_TIME)

    avg_wait = np.mean(cc.wait_times)
    max_queue = max(cc.queue_lengths) if cc.queue_lengths else 0
    agent_util = (sum(cc.wait_times) / (SIM_TIME * num_agents)) * 100

    results[num_agents] = {
        "Average Wait Time": avg_wait,
        "Max Queue Length": max_queue,
        "Agent Utilization (%)": agent_util
    }

# Run all scenarios
for agents in num_agents_list:
    run_simulation(agents)

# Print results
for k, v in results.items():
    print(f"\nScenario with {k} agents:")
    print(v)



