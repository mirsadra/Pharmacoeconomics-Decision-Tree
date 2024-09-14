# Pharmacoeconomics Decision Tree Model

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.18%2B-013243.svg?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.1%2B-11557c.svg?logo=Plotly&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-2.4%2B-FFA500.svg?logo=GraphQL&logoColor=white)
![GitHub stars](https://img.shields.io/github/stars/mirsadra/Pharmacoeconomics-Decision-Tree?style=social)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

A Python-based tool for building and analyzing decision trees in pharmacoeconomics.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Examples](#examples)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## Introduction

**Pharmacoeconomics Decision Tree Model** is a tool designed to help healthcare professionals, researchers, and students perform cost-effectiveness analysis using decision tree models. It allows users to build customizable decision trees, calculate expected costs and utilities, and visualize the results.

Decision trees are a fundamental tool in pharmacoeconomics for evaluating the economic outcomes of different healthcare interventions. This project aims to make decision tree modeling accessible, even for those with minimal programming experience.

## Features

- **Easy-to-use Classes**: Simplified classes for decision and chance nodes.
- **Cost-Effectiveness Analysis**: Calculate expected costs, utilities, and Incremental Cost-Effectiveness Ratios (ICERs).
- **Visualization**: Visualize decision trees using simple plotting functions.
- **Extensibility**: Modular code that can be extended for more complex analyses.

## Requirements

- **Python 3.6 or higher**

### Python Packages

- `numpy`
- `pandas`
- `matplotlib`
- `networkx`
- `scipy`

You can install these packages using `pip`. Instructions are provided in the [Installation](#installation) section.

## Installation

### 1. Clone the Repository

First, you need to download the project files from GitHub.

```bash
git clone https://github.com/yourusername/Pharmacoeconomics-Decision-Tree.git
```

Alternatively, you can download the ZIP file from the GitHub repository and extract it to your desired location.

### 2. Navigate to the Project Directory

```bash
cd Pharmacoeconomics-Decision-Tree
```

### 3. Install the Required Packages
It's recommended to use a virtual environment to avoid conflicts with other Python projects.

Using `virtualenv` (Optional but Recommended)

```bash
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment named 'venv'
virtualenv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Install Dependencies

Install the required Python packages using the requirements.txt file.

```bash
pip install -r requirements.txt
```

If you encounter any issues, you can install the packages individually:

```bash
pip install numpy matplotlib networkx
```

## Usage

### Quick Start

Follow these steps to run a basic example of the decision tree model.

#### 1. Open the Example Notebook

An example Jupyter Notebook is provided to demonstrate how to use the tool.

```bash
jupyter notebook examples/example_usage.ipynb
```

If you don't have Jupyter Notebook installed, you can install it using:

```bash
pip install notebook
```

#### 2. Run the Notebook Cells
- Open example_usage.ipynb in Jupyter Notebook.
- Run each cell one by one by clicking on the cell and pressing Shift + Enter.
- The notebook includes explanations and outputs to help you understand each step.

## Examples
Below is a basic example of how to use the tool in a Python script.

#### Example: Evaluating Treatment Options
```python
# Import the necessary classes
from src.decision_tree import DecisionNode, ChanceNode
from src.analysis import calculate_icer
from src.visualization import plot_decision_tree

# Create the decision node
treatment_decision = DecisionNode('Treatment Decision')

# Option A: Medication
medication = ChanceNode('Medication', probability=1.0, cost=1500, utility=0)
# Outcomes for Medication
success_med = ChanceNode('Success', probability=0.6, cost=0, utility=0.9)
failure_med = ChanceNode('Failure', probability=0.4, cost=3000, utility=0.4)
medication.add_next_node(success_med)
medication.add_next_node(failure_med)

# Option B: Surgery
surgery = ChanceNode('Surgery', probability=1.0, cost=5000, utility=0)
# Outcomes for Surgery
success_surg = ChanceNode('Success', probability=0.8, cost=0, utility=0.95)
failure_surg = ChanceNode('Failure', probability=0.2, cost=8000, utility=0.3)
surgery.add_next_node(success_surg)
surgery.add_next_node(failure_surg)

# Add options to the decision node
treatment_decision.add_branch(medication)
treatment_decision.add_branch(surgery)

# Calculate expected values
cost_med, utility_med = medication.expected_values()
cost_surg, utility_surg = surgery.expected_values()

print(f"Medication - Expected Cost: ${cost_med:.2f}, Expected Utility: {utility_med:.2f}")
print(f"Surgery - Expected Cost: ${cost_surg:.2f}, Expected Utility: {utility_surg:.2f}")

# Calculate ICER
icer_value = calculate_icer(cost_med, utility_med, cost_surg, utility_surg)
print(f"ICER of Surgery over Medication: ${icer_value:.2f} per additional utility")

# Visualize the decision tree
plot_decision_tree(treatment_decision)
```

#### Explanation
- Decision Node: Represents a point where a decision is made (e.g., choosing between treatments).
- Chance Node: Represents a point where an outcome is determined by chance (e.g., success or failure of a treatment).
- Expected Values: The average cost and utility considering the probabilities of different outcomes.
- ICER: Incremental Cost-Effectiveness Ratio, used to compare the cost-effectiveness of two interventions.

## Project Structure
Here's an overview of the project's directory structure:
```bash
Pharmacoeconomics-Decision-Tree/
├── src/
│   ├── decision_tree.py       # Core classes for building the decision tree
│   ├── analysis.py            # Functions for economic analysis
│   └── visualization.py       # Functions for visualizing the decision tree
├── examples/
│   └── example_usage.ipynb    # Jupyter Notebook with example usage
├── tests/
│   └── test_decision_tree.py  # Unit tests for the decision tree module
├── docs/
│   └── documentation.md       # Detailed documentation (optional)
├── README.md                  # This file
├── requirements.txt           # List of required Python packages
├── LICENSE                    # License information
└── .gitignore                 # Files and folders to be ignored by Git
```

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or need further assistance, feel free to reach out:
- Email: miirsadra@gmail.com
- GitHub Issues: [Create an issue](https://github.com/mirsadra/Pharmacoeconomics-Decision-Tree/issues)


**Additional Tips for Beginners**

- **Python Basics**: If you're new to Python, consider completing a basic tutorial or course to familiarize yourself with the language.
- **Understanding Decision Trees**: Research the fundamentals of decision tree analysis in pharmacoeconomics to get the most out of this tool.
- **Ask for Help**: Don't hesitate to reach out via email or GitHub issues if you run into problems.

---

**Frequently Asked Questions**

1. **I get an ImportError when running the code. What should I do?**

   Make sure all the required packages are installed and that you're running the script from the project directory. If you're using a virtual environment, ensure it's activated.

2. **How do I install Python and pip?**

   - **Windows**: Download the installer from [python.org](https://www.python.org/downloads/windows/) and follow the instructions. Make sure to check the box that says "Add Python to PATH."
   - **macOS**: Python 2.7 comes pre-installed. For Python 3, use Homebrew (`brew install python3`) or download from [python.org](https://www.python.org/downloads/mac-osx/).
   - **Linux**: Use your package manager (`sudo apt-get install python3` for Debian-based systems).

3. **Can I use this tool for other types of decision trees?**

   Yes, the tool is designed to be flexible and can be adapted for various decision tree analyses beyond pharmacoeconomics.

4. **I found a bug. How can I report it?**

   Please open an issue on the GitHub repository with details about the bug and steps to reproduce it.

---

Thank you for choosing the **Pharmacoeconomics Decision Tree Model** for your analysis needs. 

We hope this tool assists you in making informed decisions in healthcare economics.

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/miirsadra)
