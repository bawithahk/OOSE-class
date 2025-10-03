import pytest
from unittest.mock import MagicMock
from models import Base, Admin, Product
from sqlalchemy.orm import Session

# -------------------------------
# Helper: generate fake objects for models
# -------------------------------
def create_stub_admin(email="stub@test.com"):
    # Stub admin to simulate an existing entry
    return Admin(name="StubAdmin", email=email, password="stub123", role="Admin")

def generate_test_objects(model_class, admin_id=None):
    if model_class.__name__ == "Admin":
        return Admin(name="TestAdmin", email="test@test.com", password="pass", role="Admin")
    elif model_class.__name__ == "Product":
        return Product(
            adminID=admin_id or 1,
            name="TestProduct",
            price=100.0,
            category="Electronics",
            stockQuantity=10
        )
    else:
        return None

# -------------------------------
# 1. Test: Basic creation with mock session
# -------------------------------
@pytest.mark.parametrize("model_class", [Admin, Product])
def test_model_creation_mock(model_class):
    fake_session = MagicMock(spec=Session)

    if model_class.__name__ == "Product":
        obj = generate_test_objects(model_class, admin_id=1)
    else:
        obj = generate_test_objects(model_class)

    fake_session.add(obj)
    fake_session.commit()

    # Assertions to ensure mock was called
    fake_session.add.assert_called_once_with(obj)
    fake_session.commit.assert_called_once()
    assert obj is not None

# -------------------------------
# 2️. Test: Duplicate Admin email (stub)
# -------------------------------
def test_admin_duplicate_email_stub():
    class StubQuery:
        def filter_by(self, **kwargs):
            return self
        def first(self):
            return create_stub_admin()  # simulate existing admin

    class StubSession:
        query = lambda self, model: StubQuery()
        add = lambda self, obj: None
        commit = lambda self: None

    session = StubSession()

    # Simulated business logic
    existing = session.query(Admin).filter_by(email="stub@test.com").first()
    with pytest.raises(ValueError):
        if existing:
            raise ValueError("Admin with this email already exists")
        admin = Admin(name="TestAdmin2", email="stub@test.com", password="pass", role="Admin")
        session.add(admin)
        session.commit()

# -------------------------------
# 3️. Test: Upgrade role requires SuperAdmin (mock)
# -------------------------------
def test_upgrade_role_mock():
    fake_session = MagicMock()
    admin = Admin(name="Charlie", email="charlie@test.com", password="1234", role="Admin")
    super_admin = Admin(name="Super", email="super@test.com", password="1234", role="SuperAdmin")
    normal_admin = Admin(name="Normal", email="normal@test.com", password="1234", role="Admin")

    # Attempt upgrade by non-SuperAdmin -> should fail
    with pytest.raises(PermissionError):
        if normal_admin.role != "SuperAdmin":
            raise PermissionError("Only SuperAdmin can upgrade roles")
        admin.role = "SuperAdmin"
        fake_session.commit()

    # Upgrade by SuperAdmin
    if super_admin.role == "SuperAdmin":
        admin.role = "SuperAdmin"
        fake_session.commit()

    assert admin.role == "SuperAdmin"
    fake_session.commit.assert_called_once()
