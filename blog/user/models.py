import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from db import Base, init_db
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Index
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Users(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True, nullable=False)  # 用户名
    password = Column(String(150), index=True, nullable=False)  # 密码
    c_time = Column(DateTime, nullable=False, default=datetime.datetime.now)  # 创建时间
    email = Column(String(50), nullable=False)  # 邮箱
    gender = Column(Integer, default=1)   # 性别 1表示男 2表示女
    age = Column(Integer, default=0)  # 年龄
    hometown = Column(String(50))  # 家乡, 可以为空


class OperationDB:
    def __init__(self):
        engine = create_engine('mysql+pymysql://root:199199@127.0.0.1:3306/blog?charset=utf8')
        self.Connection = sessionmaker(bind=engine)
        self.conn = scoped_session(self.Connection)

    def add_one(self, param):
        """添加一条数据"""
        self.conn.add(param)
        self.conn.commit()
        self.close()

    def add_many(self, params):
        """添加多条数据"""
        self.conn.add_all(params)
        self.conn.commit()
        self.close()

    def delete_data(self, table, param=None):
        """删除数据"""
        if param:
            self.conn.query(table).filter(param).delete()
        else:
            self.conn.query(table).delete()
        self.conn.commit()
        self.close()

    def close(self):
        self.conn.close()

    def query_all(self, table, param=None):
        """查询里面的数据"""
        print(param, 44444444444444444)
        if param is None:
            data_list = self.conn.query(table).all()
            return data_list
        else:
            print(123123123)
            data_list = self.conn.query(table).filter(param).all()
            print(data_list, 2222222222222222)
            return data_list


if __name__ == '__main__':
    init_db()
    # a = OperationDB()
    # b = a.conn.query(Users).filter(Users.username=='admin1111').all()
    # print(b[0].username)