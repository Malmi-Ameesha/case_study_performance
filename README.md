# 📞 Call Center Performance Simulation – Case Study

## 📘 Overview
This project is a **simulation-based case study** designed to analyze the performance of a **call center system** using **Python and SimPy**.  
It models how the number of available agents affects customer wait time, queue length, and agent utilization.  
The goal is to understand the **trade-off between customer satisfaction and resource efficiency**.

---


## 🧠 Simulation Details
The simulation uses **SimPy (Discrete-Event Simulation)** and models:
- **Random call arrivals** (following an exponential distribution)
- **Service times** (randomly distributed around an average of 5 minutes)
- **Queue management** using a resource pool for available agents

### Parameters
| Parameter | Description | Default |
|------------|-------------|----------|
| `SIM_TIME` | Total simulation duration | 480 minutes (8 hours) |
| `arrival_rate` | Average interval between incoming calls | 1 every 5 minutes |
| `service_time_mean` | Average duration to handle a call | 5 minutes |
| `num_agents` | Number of available agents | 3, 4, and 6 (scenarios) |

---

## 🚀 Running the Simulation
### **Requirements**
Install dependencies:
 ```sh
   pip install simpy matplotlib numpy
   ```
Run the Simulation:
 ```sh
  python main.py
   ```
