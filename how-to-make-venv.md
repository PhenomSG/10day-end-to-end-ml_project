# 🐍 Virtual Environment Methods in Python: `venv` vs `conda`

This guide compares two popular methods for creating Python virtual environments: the built-in `venv` module and Anaconda’s `conda` environments.

---

## 🔹 Method 1: `venv` (Standard Python Virtual Environment)

### ✅ Best When:
- You want **lightweight**, **built-in tools** with no extra software.
- You’re using packages available on **PyPI** via `pip`.
- You don’t need system-level (non-Python) dependencies.
- You want a quick, minimal setup for simple or mid-size projects.

### ⚙️ Setup Steps:
```bash
# Navigate to your project directory
cd path\to\your\project

# Create the virtual environment
python -m venv your-env-name

# Activate the virtual environment (on Command Prompt)
.\your-env-name\Scripts\activate

# Install Jupyter kernel support
pip install ipykernel

# Register this environment as a Jupyter kernel
python -m ipykernel install --name=your-env-name

# (Optional) List available Jupyter kernels
jupyter kernelspec list
