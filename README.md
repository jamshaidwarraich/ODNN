# A Data-Driven Approach to Hepatitis C Forecasting Using Machine Learning and Epidemiological Models

This repository accompanies the article **"A Data-Driven Approach to Hepatitis C Forecasting Using Machine Learning and Epidemiological Models."**

It contains:
1. An Oscillatory Deep Neural Network (ODNN) implementation using `neurodiffeq` for a compartmental HCV model.
2. A classical 4th-order Runge–Kutta (RK4) implementation of the same model.
3. Comparison utilities and plotting scripts.

> Note: If you use this repository for your research, please cite it (see Citation section).

## 📦 Installation

```bash
# 1) Clone and enter the project
git clone https://github.com/YourUsername/HCV-Forecasting-ML-Epi.git
cd HCV-Forecasting-ML-Epi

# 2) Install dependencies
pip install -r requirements.txt
```

## ▶️ Quickstart

```bash
# ODNN training & plots
python src/odnn_solver.py

# RK4 simulation & plots
python src/rk4_solver.py

# Side-by-side comparison & error plots
python src/comparison.py
```

## 📁 Project Structure

```
HCV-Forecasting-ML-Epi/
├─ src/
│  ├─ odnn_solver.py      # ODNN via neurodiffeq (training + solution + plots)
│  ├─ rk4_solver.py       # RK4 integrator + plots
│  └─ comparison.py       # ODNN vs RK4 comparison and error plots
├─ requirements.txt
├─ LICENSE
├─ README.md
└─ example_run.py
```

## 🧪 Reproducibility Notes
- Set random seeds in PyTorch/NumPy for deterministic runs if needed.
- Training time depends on hardware and `max_epochs` in `odnn_solver.py`.

## 📝 Data Availability Statement (template)
All code used in this study is available at **GitHub** (https://github.com/YourUsername/HCV-Forecasting-ML-Epi) and
archived at **Zenodo** (DOI: 10.5281/zenodo.xxxxxxx).

## 📜 Citation (template)
```bibtex
@software{Mannan2025-HCV-ODNN,
  author  = {Abdul Mannan},
  title   = {A Data-Driven Approach to Hepatitis C Forecasting Using Machine Learning and Epidemiological Models},
  year    = {2025},
  url     = {https://github.com/YourUsername/HCV-Forecasting-ML-Epi},
  doi     = {10.5281/zenodo.xxxxxxx}
}
```

## 🔒 License
Released under the MIT License. See [LICENSE](LICENSE).
