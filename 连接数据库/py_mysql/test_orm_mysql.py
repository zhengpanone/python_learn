# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

engine = create_engine('mysql://root:root@localhost:3306/news?charset=utf8')

Base = declarative_base()
Session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(200), )
    types = Column(String(10), nullable=True)
    is_vaild = Column(Boolean)


class OrmTest:
    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = News(
            title='标题',
            content='内容·',
            types='类型',
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        return self.session.query(News).get(1)

    def get_more(self):
        return self.session.query(News).filter_by(title='1')

    def update_data(self):
        obj = self.session.query(News).get(1)
        obj.title = "修改"
        self.session.add(obj)
        self.session.commit()
        return obj

    def delete_data(self):
        data = self.session.query(News).get(2)
        self.session.delete(data)
        self.session.commit()


def main():
    obj = OrmTest()
    # result = obj.add_one()
    # print(result.id)
    '''
    result = obj.get_one()
    if result:
        print("ID:{0}=>{1}".format(result.id, result.title))
    else:
        print("Not exist")
        '''
    """
    result = obj.get_more()
    print(result.count())
    for r in result:
        print(r.title)
        """
    print(obj.update_data())
    print(obj.delete_data())


if __name__ == "__main__":
    # News.metadata.create_all(engine)
    main()
