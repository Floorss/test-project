class Bayes:
    def __init__(self, hypothesis, priors, observations, likelihood):
        self.hypothesis = hypothesis
        self.priors = priors
        self.observations = observations
        self.likelihood_array = likelihood_array
    
    def likelihood(self, observations, hypothesis):
        index_obs = self.observations.index(observations)
        index_hypo = self.hypothesis.index(hypothesis)
        return self.likelihood_array[index_hypo][index_obs]
    
    def norm_constant(self, observations):
        sum = 0;
        for i in self.hypothesis:
            sum += self.priors[self.hypothesis.index(i)] * self.likelihood(observations, i)
        return sum;
    
    def single_posterior_update(self, observations, priors):
        posteriors = []
        for i, hypothesis in enumerate(self.hypothesis):
            posteriors.append((self.likelihood(observations, hypothesis)*priors[i])/self.norm_constant(observations))
        return posteriors
    
if __name__ == "__main__":
    hypothesis = ["bowl1", "bowl2"]
    observations = ["chocolate", "vanilla"]
    likelihood_array= [[15/50, 35/50],[30/50, 20/50]]
    priors = [0.5, 0.5]

    b = Bayes(hypothesis, priors, observations, likelihood_array)
    l = b.likelihood("chocolate", "bowl1")
    print("likelihood(chocolate, bowl1) = %s " % l)

    n_c = b.norm_constant("vanilla")
    print("normalizing constant for vanilla: %s" % n_c)

    p_1 = b.single_posterior_update("vanilla", [0.5, 0.5])
    print("vanilla - posterior: %s" % p_1)