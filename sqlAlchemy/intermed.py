from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, Select
from toignore import password

engine = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost:5432/sqltut', echo=True)


meta = MetaData()

# Table(tablename, metadata, *columns, **kwargs)
people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)
meta.create_all(engine)

conn = engine.connect()

''' 
insert() construct can be used to insert single or multiple records 

insert_query = people.insert().values(id=1, name="John Doe", age=28)
insert_query2 = insert(people).values(id=2, name="Jane Smith", age=34) # equivalent way

'''
insert_query = people.insert().values([
    {"id": 6, "name": "John Doe", "age": 28},
    {"id": 4, "name": "Jane Smith", "age": 34},
    {"id": 5, "name": "Sam Brown", "age": 45}
])
# result = conn.execute(insert_query)
# gives result in order 6, 4, 5

# select_query = Select(people).where(people.c.id.in_([4,5,6]))
# result = conn.execute(select_query)

query = Select(people).order_by(people.c.id)
result = conn.execute(query)
for row in result.fetchall():
    print(row)

conn.commit()