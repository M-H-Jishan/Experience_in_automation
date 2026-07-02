from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

from config import DATABASE_URI

Base = declarative_base()
engine = create_engine(DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
