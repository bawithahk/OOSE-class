
---

## 🐍 Python Files

### `models.py`
- Contains all database models using **SQLAlchemy ORM**.
- Models include:
  - `Admin`, `Customer`, `Product`, `Order`, `Promotion`, `Payment`, `Shoppingcart`, `Wishlist`, etc.
- Defines relationships between tables using `relationship`.

### `main.py`
- Entry point for Python application.
- Can be used to interact with the database via SQLAlchemy session.
- Example CRUD operations for `Admin` and `Product`.

### `tests/test_models_auto.py`
- Contains **unit tests** for models and business logic.
- Includes:
  1. **Mock test**: Simulates SQLAlchemy session for creating objects.
  2. **Stub test**: Simulates database queries to test duplicate admin email logic.
  3. **Mock test**: Simulates role upgrade logic ensuring only SuperAdmin can upgrade roles.
- Uses **pytest** as the testing framework.

---

## ⚙️ Running Tests Locally

1. Install dependencies:

```bash
pip install pytest sqlalchemy
