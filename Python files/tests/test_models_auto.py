import pytest
from unittest.mock import MagicMock
from models import Admin

def add_admin(session, name, email, password, role):
    """Add a new admin if email is not already used."""
    existing = session.query(Admin).filter_by(email=email).first()
    if existing:
        raise ValueError("Admin with this email already exists.")
    new_admin = Admin(name=name, email=email, password=password, role=role)
    session.add(new_admin)
    session.commit()
    return new_admin


def update_admin_role(session, email, new_role):
    """Update admin role."""
    admin = session.query(Admin).filter_by(email=email).first()
    if not admin:
        raise ValueError("Admin not found.")
    admin.role = new_role
    session.commit()
    return admin


def delete_admin(session, email):
    """Delete an admin by email."""
    admin = session.query(Admin).filter_by(email=email).first()
    if not admin:
        raise ValueError("Admin not found.")
    session.delete(admin)
    session.commit()

# -------------------------------
# ✅ TEST 1 — Add Admin (uses MOCK)
# -------------------------------
def test_add_admin_success():
    mock_session = MagicMock()
    mock_session.query().filter_by().first.return_value = None  # No existing admin

    result = add_admin(mock_session, "Alice", "alice@example.com", "pass123", "Admin")

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    assert isinstance(result, Admin)
    assert result.name == "Alice"


# -------------------------------
# ✅ TEST 2 — Add Admin duplicate email (uses STUB)
# -------------------------------
def test_add_admin_duplicate_email():
    mock_session = MagicMock()
    # Stub: pretend an admin already exists
    mock_session.query().filter_by().first.return_value = Admin(name="Alice", email="alice@example.com", password="pass", role="Admin")

    with pytest.raises(ValueError, match="already exists"):
        add_admin(mock_session, "Bob", "alice@example.com", "pass123", "Admin")


# -------------------------------
# ✅ TEST 3 — Update Admin role (uses MOCK)
# -------------------------------
def test_update_admin_role_success():
    mock_session = MagicMock()
    fake_admin = Admin(name="Bob", email="bob@example.com", password="1234", role="User")

    # Stub the query to return our fake admin
    mock_session.query().filter_by().first.return_value = fake_admin

    updated = update_admin_role(mock_session, "bob@example.com", "SuperAdmin")

    assert updated.role == "SuperAdmin"
    mock_session.commit.assert_called_once()


# -------------------------------
# ✅ TEST 4 — Delete Admin (uses MOCK)
# -------------------------------
def test_delete_admin_success():
    mock_session = MagicMock()
    fake_admin = Admin(name="John", email="john@example.com", password="pass", role="Admin")

    # Stub query to return admin
    mock_session.query().filter_by().first.return_value = fake_admin

    delete_admin(mock_session, "john@example.com")

    mock_session.delete.assert_called_once_with(fake_admin)
    mock_session.commit.assert_called_once()
