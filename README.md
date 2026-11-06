<div align="center">

# 🥫 PantryLedger

### Pantry Inventory, Expiry & Shopping List Manager

Know what you have, what is expiring, and what needs to be restocked.

![Status](https://img.shields.io/badge/Status-Implemented-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask&logoColor=white)

</div>

---

## 📌 Overview

**PantryLedger** is a Flask + SQLite household inventory app for tracking pantry items, quantities, expiry dates, low-stock levels, and shopping needs. Its intended workflow is simple: record what is on the shelf, monitor expiry dates, and prepare a shopping list before essentials run out.

> **Current status:** Implemented with inventory CRUD, stock consumption, low-stock restock suggestions, and a manual shopping list.

## ✨ Features

- ➕ Add, update, and remove pantry items
- 📦 Track quantity and measurement units
- 📅 Record purchase and expiry dates
- ⏰ Highlight items nearing expiry
- 🚨 Configure low-stock thresholds
- 🧾 Log consumption and update inventory
- 🛒 Generate a shopping list from low-stock items

## 🛠️ Tech Stack

| Technology | Intended use |
|---|---|
| Python 3.10+ | Core programming language |
| Flask | Web application |
| SQLite | Local data storage |
| HTML, CSS, JavaScript | User interface |
| pytest | Automated testing |

## 🧱 Data Model

Each pantry item is expected to include:
- Item name and category
- Quantity and measurement unit
- Optional purchase and expiry dates
- Low-stock threshold

Consumption records should capture the item, quantity used, and timestamp so inventory changes can be tracked.

## 🗺️ Roadmap

- [ ] Set up Flask application and SQLite schema
- [ ] Implement pantry item management
- [ ] Add expiry-date and low-stock views
- [ ] Build consumption history
- [x] Generate low-stock suggestions and manage shopping list
- [ ] Add tests, sample data, and screenshots

## 🚀 Getting Started

```bash
git clone https://github.com/kalashsri18-crypto/PantryLedger.git
cd PantryLedger
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Run tests with `pytest -q`.

## 📁 Project Structure

```text
.
├── app.py
├── requirements.txt
├── templates/
├── static/
├── tests/
├── .gitignore
├── LICENSE
└── README.md
```

## 👨‍💻 Author

**Kalash Srivastava**  
[GitHub](https://github.com/kalashsri18-crypto) · [LinkedIn](https://www.linkedin.com/in/kalash-srivastava-b6592a3b3) · [Email](mailto:kalashsri18@gmail.com)

---

<div align="center">
  Documentation and project direction by Kalash
</div>
