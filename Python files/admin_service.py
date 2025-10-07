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
