from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def init_db():
    #  创建表
    engine = create_engine(
        'mysql+pymysql://root:199199@127.0.0.1:3306/blog?charset=utf8',
        max_overflow=2,  # 超出连接池数量最多再创建2个
        pool_size=5,  # 连接池数量
        pool_timeout=30,  # 池中没有线程最大等待时间
        pool_recycle=-1,  # 多久之后对线程中线程进行一次回收(重置)
    )

    Base.metadata.create_all(engine)

