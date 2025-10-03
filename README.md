
---

## 💻 Java Files

### `src/main/java`
- Contains all Java classes for the **Storefront application**.
- Implements core business logic for the app.
- Follows OO principles (encapsulation, inheritance, polymorphism).
- Code style is enforced with `checkstyle.xml`.

---

## 🐍 Python Files

### `models.py`
- Defines the database models using **SQLAlchemy ORM**.
- Includes tables such as `Admin`, `Customer`, `Product`, `Order`, `Promotion`, `Payment`, `Shoppingcart`, `Wishlist`, etc.
- Relationships between tables are defined using `relationship`.

### `main.py`
- Main entry point for Python application logic.
- Handles CRUD operations for models (e.g., Admin, Product).
- Can connect to MySQL database using SQLAlchemy.

### `tests/test_models_auto.py`
- Unit tests for Python models and business logic.
- Uses **pytest**, **mocks**, and **stubs**.
- Includes:
  1. Mocked creation of Admin/Product objects.
  2. Stubbed query to prevent duplicate Admin email.
  3. Mocked test for SuperAdmin role upgrade permission.

---

## 📄 Design Documentation

### `docs/` folder
- **Figma_designs.docx**: Visual UI designs and wireframes from Figma.
- **Class_Diagrams.docx**: UML diagrams showing classes, attributes, and relationships.
- **Deployment_Diagrams.docx**: Architecture and deployment diagrams.
- **Sequence_Diagrams.docx**: UML sequence diagrams showing interactions.
- **Other_design_docs.docx**: Additional design and planning documents.

---

## ⚙️ Running Python Tests Locally

1. Install dependencies:

```bash
pip install pytest sqlalchemy
