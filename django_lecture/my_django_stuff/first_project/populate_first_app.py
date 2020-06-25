import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker
fake_gen = Faker()
topics = ['Search','Social','Marketplace','News','Game']

def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    print('abcdef : ',Topic.objects.get_or_create(top_name=random.choice(topics))[1])
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        wbpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(names=wbpg,date=fake_date )[0]


if __name__ == '__main__':
    print('populating script')
    # populate(20)
    # print(add_topic())
    print('populating complete')
    print(WebPage.objects.all())
