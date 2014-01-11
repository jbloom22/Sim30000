class Sequencer(object):
  def __init__(self, data, accountant):
    self.data = data
    self.accountant = accountant

  def sequence(self, people): 
    self.accountant.account(len(people))

    return [self.data[person] for person in people]
