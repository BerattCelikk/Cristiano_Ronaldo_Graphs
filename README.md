<div align="center">

# ⚽ CR7 Analytics: Quantitative Sports Visualization
### *A Data-Driven Exploration of Career Metrics and Performance Patterns through Statistical Plotting*

---

[![Overview](https://img.shields.io/badge/📖_Overview-blue?style=for-the-badge)](#-project-overview)
[![Key Features](https://img.shields.io/badge/✨_Key_Features-6f42c1?style=for-the-badge)](#-key-features)
[![Tech Stack](https://img.shields.io/badge/🛠️_Tech_Stack-success?style=for-the-badge)](#-tech-stack)
[![Architecture](https://img.shields.io/badge/🏗️_Architecture-orange?style=for-the-badge)](#-technical-architecture)
[![Installation](https://img.shields.io/badge/🚀_Quick_Start-red?style=for-the-badge)](#-getting-started)
[![Contact](https://img.shields.io/badge/📩_Contact-lightgrey?style=for-the-badge)](#-contact)

---

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557C?style=flat-square)](https://matplotlib.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Codiom](https://img.shields.io/badge/Powered_By-Codiom-FF4B4B?style=flat-square)](https://codiom.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-4caf50?style=flat-square)](https://opensource.org/licenses/MIT)

**Transforming raw career statistics into high-fidelity visual intelligence.**

</div>

---

## 📖 Project Overview

The **CR7 Analytics Project** is a sophisticated data visualization framework designed to analyze the career progression of Cristiano Ronaldo. Developed as a specialized data science asset within the **Codiom** initiative, this repository utilizes **Python** to decode complex sports metrics into actionable visual insights.

As a Software Engineering student at Istanbul Aydın University, I architected this project to demonstrate the power of **Exploratory Data Analysis (EDA)** and visual storytelling in the realm of high-performance sports analytics.

---

## ✨ Key Features

* **📊 Temporal Performance Mapping:** Line graphs and area charts visualizing goal scoring trends across multiple seasons.
* **🔍 Distribution Analysis:** Comprehensive breakdown of goals by competition type, opponent strength, and match location.
* **📈 Career Trajectory Modeling:** Comparative analysis of performance metrics during different club tenures (Manchester United, Real Madrid, Juventus, Al-Nassr).
* **🛠️ Automated Data Cleaning:** Integrated Python scripts to preprocess and normalize raw career statistics for accurate plotting.
* **🎨 High-Fidelity Visuals:** Utilizing **Seaborn** and **Matplotlib** to create publication-quality charts with customized aesthetics.

---

## 🛠️ Tech Stack

| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Development** | **Python 3.9+** | Core logic and data processing orchestration. |
| **Data Engine** | **Pandas / NumPy** | Statistical aggregation and dataset manipulation. |
| **Visualization** | **Matplotlib / Seaborn** | Generating high-resolution graphs and statistical plots. |
| **Data Format** | **CSV / JSON** | Managing structured sports datasets. |
| **Version Control** | **Git / GitHub** | Management of source code and visualization assets. |

---

## 🏗️ Technical Architecture

The system utilizes a structured **Visualization Pipeline**, ensuring that raw data is mathematically validated before being rendered.



### Mathematical Validation

To analyze efficiency, the engine calculates key performance indicators (KPIs) such as the **Scoring Rate ($SR$):**

$$SR = \frac{\text{Total Goals}}{\text{Total Matches Played}}$$

By applying rolling averages, the framework mitigates seasonal noise to highlight the true performance trend over a 20-year span.

---

## 📂 Project Structure

```bash
.
├── 📁 data/                 # Raw and processed career datasets
├── 📄 analysis.py           # Statistical aggregation and KPI calculation
├── 📄 visualization.py      # Core plotting logic and style configurations
├── 📁 output/               # High-resolution exported graphs (.png, .pdf)
├── 📄 requirements.txt      # Dependency manifest
└── 📄 README.md             # Documentation Hub
```

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone [https://github.com/BerattCelikk/Cristiano_Ronaldo_Graphs.git](https://github.com/BerattCelikk/Cristiano_Ronaldo_Graphs.git)
cd Cristiano_Ronaldo_Graphs

# Initialize virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```

### 2. Dependency Injection

```bash
pip install -r requirements.txt
```

### 3. Execution
To generate the full analytics suite:
```bash
python visualization.py

```


## 🗺️ Roadmap

- [ ] Interactive Dashboard: Transitioning to Streamlit or Plotly for real-time interactive charting.
- [ ] Machine Learning Integration: Predicting future scoring trends based on historical aging curves.
- [ ] Comparative Analytics: Adding automated comparison modules with other elite athletes.
- [ ] Social Media Integration: Automated API to post daily statistical insights to X (Twitter).

---

<div align="center" id="contact">

Architected with precision by Berat Erol Çelik Founder of Codiom

Software Engineering @ Istanbul Aydın University

</div>


















