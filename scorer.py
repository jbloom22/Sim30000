class Scorer(object):
  def score(self, data, output):
    return len(set(data) - set(output))
