# Nuclear-Reactor-Physics-Simulations
This repository contains basic Python scripts developed to simulate fundamental concepts of Nuclear Physics and Reactor Engineering. The goal is to demonstrate the application of computational methods (even if they are basics) to solve physical problems and analyze data.

## Projects Included
### 1. Binding Energy Calculator
* **Description:** Calculates the mass defect and binding energy per nucleon for various isotopes, visualizing the curve of nuclear stability.

### 2. Reactor SCRAM & Transients Simulation
* **Description:** Models the thermodynamic response of a PWR reactor coolant system during a power excursion.
* **Features:** Includes an automated protection logic that triggers a SCRAW (reactor trip) when the temperature thresholds are exceeded.
* **Key Skills:** Control logic loops, Time-dependent simulation.

### 3. Monte Carlo Radioactive Decay Simulation
* **Description:** Simulates the stochastic nature of radioactive decay for a population of atoms.
* **Method:** Uses basic random number generation to model the probability of decay per time step (usually called $\lambda$), comparing the discrete results with the analytical exponential law $N(t) = N_0 e^{-\lambda t}$.
* **Key skills:** Monte Carlo methods, Statistical analysis, Matplotlib visualization.

  ## Tech Stack
  * **Language:** Python 3.13.9
  * **Libraries:** 'matplotlib', 'numpy', 'random'
 
  — — —
  *Author: Daniel Fernández García — Physics Student*
