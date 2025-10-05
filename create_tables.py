from aap.database import Base, engine
from aap import models

print("📌 Creating tables in resume_db ...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
