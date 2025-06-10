# bioreactor_sim.py
import streamlit as st
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

st.title("🧪 Bioreactor Simulation (Monod Kinetics)")

# Sliders for parameters
mu_max = st.slider("μ_max (1/h)", 0.1, 1.0, 0.4)
Ks = st.slider("K_s (g/L)", 0.01, 5.0, 0.5)
Yxs = st.slider("Y_x/s (g/g)", 0.1, 1.0, 0.5)

X0 = st.number_input("Initial Biomass X₀ (g/L)", value=0.1)
S0 = st.number_input("Initial Substrate S₀ (g/L)", value=10.0)
t_end = st.slider("Simulation Time (hours)", 5, 100, 30)

# Simulation
t = np.linspace(0, t_end, 300)

def model(y, t, mu_max, Ks, Yxs):
    X, S = y
    mu = mu_max * S / (Ks + S)
    dXdt = mu * X
    dSdt = -dXdt / Yxs
    return [dXdt, dSdt]

result = odeint(model, [X0, S0], t, args=(mu_max, Ks, Yxs))
X, S = result.T

# Plot
st.subheader("Simulation Results")
fig, ax = plt.subplots()
ax.plot(t, X, label='Biomass (X)')
ax.plot(t, S, label='Substrate (S)')
ax.set_xlabel("Time (h)")
ax.set_ylabel("Concentration (g/L)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
