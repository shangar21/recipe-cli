from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os

engine = create_engine(f'sqlite:///{os.getcwd()}/db.sqlite')
Base = automap_base()

Base.prepare(autoload_with=engine)

Unit = Base.classes.unit
UnitConversion = Base.classes.unit_conversion
Recipe = Base.classes.recipe
Ingredient = Base.classes.ingredient

session = Session(engine)
