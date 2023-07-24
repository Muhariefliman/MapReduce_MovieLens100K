
from mrjob.job import MRJob, MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [MRStep(mapper = self.map_ratings, reducer = self.reduce_ratings)]
    
    def map_ratings(self, key, value):
        (userId, movieId, rating, timestamp) = value.split('\t')
        yield rating, 1
    
    def reduce_ratings(self, key, value):
        yield key, sum(value)
    
RatingsBreakdown.run()


























