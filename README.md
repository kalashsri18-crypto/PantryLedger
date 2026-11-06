# PantryLedger
### Pantry Inventory, Expiry & Shopping List Manager

PantryLedger is a household inventory management project for tracking pantry items, quantities, expiry dates, and items that need restocking. Its intended workflow is simple: record what is on the shelf, keep an eye on expiry, and prepare a shopping list before supplies run out.

> **Repository description:** A pantry inventory app concept with stock tracking, expiry reminders, low-stock alerts, and shopping-list management.

## Planned product features
- Add, update, and remove pantry items
- Track quantity and measurement unit
- Record purchase and expiry dates
- Highlight items nearing expiry
- Configure low-stock thresholds
- Log consumption and adjust inventory
- Generate a shopping list from low-stock items

## Planned technology
- Python 3.10+
- Flask
- SQLite
- HTML, CSS and vanilla JavaScript
- pytest

## Intended project structure
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

## Development status
**Planning / README scaffold.** This repository currently contains the project overview only. The application, database, tests, and user interface are not implemented yet. The feature list is the intended scope.

## Data model proposal
Each pantry item should have a name, category, quantity, unit, optional expiry date, and low-stock threshold. Consumption entries should record the item, quantity used, and timestamp so that stock changes remain understandable.

## Roadmap
- [ ] Build the Flask app and SQLite schema
- [ ] Implement pantry item CRUD
- [ ] Add expiry and low-stock views
- [ ] Add consumption history
- [ ] Generate and edit shopping lists
- [ ] Add tests, sample data, and screenshots

## License
See [LICENSE](LICENSE) if a license file is added to this repository.
