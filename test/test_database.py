from sqlalchemy import Table, Column, Integer, String, Date
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from aiomysql.sa import create_engine
import datetime
import asyncio

metadata = MetaData()

one_level_table = Table("one_level_statistics", metadata,
                        Column('id', Integer, primary_key=True),
                        Column('data_time', Date),
                        Column('province', String),
                        Column('city', String),
                        Column('district', String),
                        Column('power_type', String),
                        Column('child_field_name', String),
                        Column('child_field_value', String),
                        Column('watch_num', Integer),
                        Column('intent_num', Integer),
                        Column('like_num', Integer),
                        Column('buy_num', Integer),
                        )

async def test_insert():
    data_values = {'data_time':datetime.datetime(2018,8,5), 'province': '广东省'.encode('utf-8 '),}
    async with create_engine(user='imei', host='192.168.2.112', password='123456',port=13306 , db='test') as engine:
        async with engine.acquire() as conn: #conn is SAConnection object
            trans = await conn.begin() # Begin a transaction and return a transaction handle
            await conn.execute(one_level_table.insert().values(**data_values ))
            res = await conn.execute(one_level_table.select())
            for i in await res.fetchall():
                print(i)
            await trans.commit() # transaction commit
        async with engine.acquire() as conn:
            res = await conn.execute(one_level_table.select())
            for i in await res.fetchall():
                print(i)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_insert())
    loop.close()
    # engine = create_engine('mysql+mysqlc onnector://:imei:123456@192.168.2.112:13306/test',encoding='utf-8', echo=True)
    # Session = sessionmaker(bind=engine)
    # one_level_table = OneLevelStatistics(data_time='2018-7-5', province='广东省', city='广州市',
    #                                      district='天河区', power_type='纯电动', child_field_name='车身类型',
    #                                      child_field_value='SUV', watch_num=12, intent_num=23)