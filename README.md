# 📦 Prism Viewer Application - Submission

## 📝 Overview

This project is the **Prism Viewer Application**, built for the screening task. It allows users to view 3D models of rectangular prisms, calculate their surface area and volume, and display the model in a 3D viewer. The application is packaged using Conda and PIP, and includes unit tests for verifying functionality.

## 🏗️ Project Structure

```
prism_viewer_submission/
├── README.md              # This file
├── test_prism_calculator.py # Unit tests for surface area and volume calculations
├── setup.py               # PIP packaging file
├── meta.yaml              # Conda recipe for packaging
├── prism_viewer-1.0-py39_0.tar.bz2 # Conda package
├── report.docx            # Methodology report
├── src/
│   ├── main.py            # Main application file with PyQt5 interface
│   ├── draw_rectangular_prism.py # 3D rendering logic
│   ├── prism_calculator.py # Calculation logic for surface area and volume
│   └── prisms.db          # SQLite database with prism dimensions
```

## 🚀 Installation Instructions

### Conda Installation

1. Install the Conda package from the local build:

```bash
conda install <path-to-your-package>/prism_viewer-1.0-py39_0.tar.bz2
```

Make sure to replace `<path-to-your-package>` with the actual path where the `tar.bz2` file is located.

### PIP Installation

1. Install the application via PIP by running:

```bash
pip install .
```

## 🖥️ Running the Application

Once installed, run the application with:

```bash
prism-viewer
```

The application will open a GUI window with options to select a rectangular prism and display its 3D model.

## 🔍 Running Unit Tests

To run the unit tests and verify the correctness of the calculations, run:

```bash
python -m unittest test_prism_calculator.py
```

## 📑 Deliverables Overview

- **Unit Test Code**: Unit tests for surface area and volume calculations in `test_prism_calculator.py`.
- **Conda Recipe**: `meta.yaml` for building the Conda package.
- **PIP Project**: `setup.py` for packaging with PIP.
- **Conda Package**: The built package `prism_viewer-1.0-py39_0.tar.bz2`.
- **Report**: A methodology report (`report.docx`) describing the approach, testing strategies, and challenges faced.

## 🛠️ Methodology

The details of the methodology, tests chosen, and challenges encountered during packaging (with Conda) are documented in the `report.docx` file.

## 📝 References

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [pythonocc-core Documentation](http://www.pythonocc.org/)

---

This concludes the **Prism Viewer Application** submission for the screening task. Thank you for the opportunity!
```

### What it Contains:
- **Project Overview**: A concise explanation of what the application does.
- **Installation Instructions**: Steps for installing with both Conda and PIP.
- **Running Instructions**: How to run the application and unit tests.
- **Deliverables**: Clear explanation of what is included in the submission.
- **Methodology Reference**: Points to the report (`report.docx`) where the methodology is detailed.
