import pytest
from unittest.mock import MagicMock
from admin_service import add_admin, update_admin_role, delete_admin
from models import Admin


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
