
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Admin, Customer, Product, Promotion, Promotionproduct  # add more if needed

# -------------------------------
# 1️. Connect to MySQL
# -------------------------------
DATABASE_URL = "mysql+mysqlconnector://root:Derrick123!@localhost/my_erd_db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Ensure tables exist (optional if already created)
Base.metadata.create_all(engine)
print("Connected to database and ORM session ready\n")


# -------------------------------
# 2️. Show clean Admin table
# -------------------------------
print("Current Admin table:")
admins = session.query(Admin).all()
for a in admins:
    print(a.adminID, a.name, a.email, a.role)
print("\n")

# -------------------------------
# 3. CREATE a new Admin
# -------------------------------
new_admin = Admin(name="Bawi Thang", email="thangb44@gmail.com", password="1234@", role="SuperAdmin")
session.add(new_admin)
session.commit()
print(f"Inserted Admin ID: {new_admin.adminID}\n")

# -------------------------------
# 4️. READ all Admins
# -------------------------------
admins = session.query(Admin).all()
print("All admins in database:")
for a in admins:
    print(a.adminID, a.name, a.email, a.role)
print("\n")

# -------------------------------
# 5️. UPDATE Admin role
# -------------------------------
admin_bawi = session.query(Admin).filter_by(email="thangb44@gmail.com").first()

if admin_bawi:
    admin_bawi.role = "Admin"  # update existing
else:
    admin_bawi = Admin(name="Bawi Thang", email="thangb44@gmail.com", password="1234@", role="Admin")
    session.add(admin_bawi)

session.commit()
print(f"Admin {admin_bawi.name} is now {admin_bawi.role}")

# -------------------------------
# 6️⃣ DELETE Bawi Thang
# -------------------------------
admin_bawi = session.query(Admin).filter_by(email="thangb44@gmail.com").first() 
if admin_bawi:
    session.delete(admin_bawi)
    session.commit()
    print("Deleted Bawi Thang from database\n")
else:
    print("Admin not found, nothing to delete.")



