from random import randint

class DataSource(object):
  def __init__(self):
    pass

  def generate(self):
    return [randint(0, 100) for i in range(0, 500)]
