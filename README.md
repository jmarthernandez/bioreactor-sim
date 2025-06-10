# Bioreactor Simulator (Monod Kinetics)

This is a simple batch bioreactor simulation using Monod kinetics. It lets you explore how biomass and substrate concentrations evolve over time based on adjustable growth parameters.

The app is built with Streamlit and runs entirely in the browser.

## Features

- Simulates biomass and substrate in batch culture
- Adjustable parameters:
  - Maximum growth rate (μ_max)
  - Substrate saturation constant (K_s)
  - Yield coefficient (Y_x/s)
  - Initial biomass and substrate levels
  - Simulation time
- Interactive plot of biomass and substrate over time

## Run Locally

```bash
pip install -r requirements.txt
streamlit run bioreactor_sim.py
```
