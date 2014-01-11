import time

class Researcher(object):
  def __init__(self, sequencer):
    self.sequencer = sequencer

  def run(self, pans=8):
    start = time.time()
    while start + (pans / 100) > time.time():
      pass

    return self.sequencer(range(0, pans))
