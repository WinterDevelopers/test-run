import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings')

import django
django.setup()
# fake pop

import random
from demoapp.models import Topic, AccessRecord, WebPage
from faker import Faker


fake = Faker()
topics = ['search', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name= webpg, date=fake_date)[0]

if __name__ =='__main__':
    print('populating Script')
    populate(20)
    print('populating complete!')
