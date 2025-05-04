**README.md**
```markdown
# EcoAI 🌿

EcoAI is a lightweight web application that helps users estimate their daily carbon footprint and suggests practical actions to reduce it based on their lifestyle habits.

## Tech Stack
- **Frontend:** HTML, Tailwind CSS, Jinja2
- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn (Linear Regression)
- **Data Handling:** NumPy, Pickle

## Features
- User inputs: daily transport, energy usage, and meat consumption
- Predicts carbon emissions using a trained ML model
- Visual impact breakdown and dynamic recommendation cards
- Fully responsive UI with smooth scroll and sticky navbar

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/devansh-dot-t/ecoai.git
   cd ecoai
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Generate model file:
   ```bash
   python create_model.py
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000/` in your browser.

##  Project Structure
```
EcoAI/
├── app.py
├── create_model.py
├── carbon_model.pkl
├── requirements.txt
├── templates/
│   └── dashboard.html
├── utils/
│   └── carbon_predictor.py
```
