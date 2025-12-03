from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydb.db', echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name str)"))
conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)
session.execute(text('INSERT INTO users (id, name) VALUES (2317, "Ramsey")'))
session.commit()