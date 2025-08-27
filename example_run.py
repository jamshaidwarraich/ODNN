from src.odnn_solver import neural_network_solution
from src.rk4_solver import RK4_SEIR
import matplotlib.pyplot as plt

# Parameters
params = (0.2, 0.40, 0.6, 0.2, 0.5, 0.35, 0.1, 0.5, 0.3, 0.6, 0.3, 0.4, 0.1, 0.02)
initial_conditions = [20, 6, 2, 6, 4, 3]
t_max = 10.0
dt = 0.1

# Get ODNN solution
ts, S, F, B, H, C, R = neural_network_solution()

# Get RK4 solution
t_rk, y_rk = RK4_SEIR(*params, t_max, dt, initial_conditions)

# Simple overlay for S
plt.figure()
plt.plot(ts, S, label='S (ODNN)')
plt.plot(t_rk, y_rk[:,0], '--', label='S (RK4)')
plt.xlabel('Time in months'); plt.ylabel('State variable')
plt.legend(); plt.tight_layout(); plt.show()
