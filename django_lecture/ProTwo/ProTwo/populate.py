import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User

from faker import Faker

fake = Faker()

def popul(N=5):
    for _ in range(N):
        fn = fake.first_name()
        ln = fake.last_name()
        em = fake.email()
        f = User.objects.get_or_create(first_name=fn , last_name=ln, email=em)[0]
        f.save()


if __name__ == '__main__':
    print('populating db')
    popul(20)
    print('done populatiing')