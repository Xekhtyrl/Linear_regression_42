## 🔧 Linear Regression Project (42/ft\_linear\_regression)

**A simple machine learning algorithm using gradient descent to predict car prices based on mileage.**

---

### 🚀 Features

* Implements **simple linear regression** from scratch.
* **Gradient descent** training algorithm to optimize parameters.
* **Model persistence**: saves learned coefficients (θ₀ and θ₁) for later predictions.
* Predicts car price given mileage using a trained model.
* Optional visualization modules for cost curve and regression fit.

---

### 🔹 Project Files

* `training.py` – main training script (reads CSV, trains, saves thetas), return on a separate file the theta for the estimation
* `estimatePrice.py` – retrieve the result of the training program and predict price for a provided mileage
* `precision.py` - shows a comparative graph with the estimate linear regression and one found with sklearn lib, and calculte the r² coefficent
* `data.csv` – sample dataset of car mileage vs. price
* `README.md` – project overview and usage instructions

---

### 🧠 Concepts Covered

* Linear regression: modeling the relationship between mileage (feature) and price (target)
* Mean Squared Error (MSE) or Mean Absolute Error (MAE) as a loss function
* Gradient descent optimization
* Feature scaling (standardization) to avoid learning skewness

---

### ⚙️ Installation & Setup

Make sure you have [Python 3](https://www.python.org/) installed.

Clone the repository:

```bash
git clone https://github.com/Xekhtyrl/Linear_regression_42.git
cd Linear_regression_42
```

Install required packages:

```bash
pip3 install -r requirements.txt
```

---

### 🧪 Usage

#### Train the model:

```bash
python3 training.py
```

* Input required by the program:

  * file path for the .csv
  * learning rate
  * number of iterations for the algorithm

#### Make predictions:

```bash
python3 estimatePrice.py
```
* Input required by the program:

  * Milleage for estimation
  
Predict price for mileage using saved model.
If no mileage is given or the training program has not been run yet, the program exit with adequate message.
  
---

### 🏁 Bonus Features > Calculate Precision:

```bash
python3 precision.py
```
* Input required by the program:

  * .csv path

Require the training program to be executed before. It will give you a visual graphic with two regression
line: One red is the result of the training, the blue is the result of the sklearn method to calculate a linear regression.
The R² coefficent or the coefficent of determination will also be given in the terminal.
---

### 🌟 Why This Project Matters

* First hands‑on introduction to machine learning at 42 network.
* Reinforces Python scripting, CSV processing, basic statistics, plotting, and algorithm implementation. ([GitHub][1])

---

### 🧭 Roadmap

| Step | Description                                                 |
| ---- | ------------------------------------------------------------|
| 1️⃣  | Load and preprocess data (feature standardization)          |
| 2️⃣  | Initialize parameters θ₀ and θ₁                             |
| 3️⃣  | Train model via gradient descent until convergence          |
| 4️⃣  | Save learned θ values                                       |
| 5️⃣  | Use `estimatePrice.py` to estimate price for a new mileage  |

---

### 📄 License & Credits

This implementation follows the 42 Network project subject. Adapt freely for personal or educational use.


[4]: https://github.com/maxisimo/42-ft_linear_regression?utm_source=chatgpt.com "maxisimo/42-ft_linear_regression: 42 school project"
[5]: https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes?utm_source=chatgpt.com "About READMEs"
