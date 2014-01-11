from multiprocessing import Pool

from sequencer import Sequencer
from source import DataSource
from scorer import Scorer
from researcher import Researcher
from accountant import Accountant

source = DataSource()
data = source.generate()

accountant = Accountant()

seq = Sequencer(data, accountant)

scorer = Scorer()

tests = range(0, 300, 4)

print "Pans\tScore\tCost"
def runTest(pans):
  researcher = Researcher(seq.sequence)
  output = researcher.run(pans=pans)

  score = scorer.score(data, output)
  print pans, '\t', score, '\t', accountant.cost

p = Pool()
p.map(runTest, tests)

#map(runTest, tests)






# Divide waiting tasks amoung machines
# Wait until they respond, or a time limit
# If the time limit is reached, return the task to the waiting list
# When the response for a task-set arrives, print it
