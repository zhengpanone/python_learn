# -*- coding: utf-8 -*-
from datetime import datetime

from mongoengine import connect, Document, StringField, IntField, EmbeddedDocument, FloatField, ListField, \
    EmbeddedDocumentField, DateTimeField, DynamicDocument

connect('student')


class Grade(EmbeddedDocument):
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOICES = {
    ('male', "男"),
    ('female', "女")
}


# class Student(Document):
class Student(DynamicDocument):
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade = ListField(EmbeddedDocumentField(Grade))
    create = DateTimeField(default=datetime.now())

    meta = {
        'collection': 'students'
    }

    def get_one(self):
        return self.objects.first()

    def get_more(self):
        return self.objects.all()

    def get_one_from_oid(self, oid):
        return self.objects.filter(id=oid).first()

    def update_one(self):
        return self.objects.filter(sex='male').update_one(inc__age=1)

    def update_more(self):
        return self.objects.filter(sex='male').update(inc__age=1)

    def delete_one(self):
        return self.objects.filter(sex='male').first().delete()

    def delete_more(self):
        return self.objects.filter(sex='male').delete()

    def add_one(self):
        self.name = "张三"
        self.age = 18
        self.sex = 'male'
        self.save()
        return self


def main():
    obj = Student()
    obj.add_one()
    return obj


if __name__ == '__main__':
    main()
