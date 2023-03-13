from random import randrange

import faker


def gen_fake_data():
    fk = faker.Faker()
    return [[fk.name(), fk.phone_number(), randrange(1, 9)] for _ in range(100)]
