# The use of information theory in evolutionary biology

Adami
2012
created: 8-9-2017

## synopsis

The use of information theory in evolutionary biology is illustrated using a pair of examples: one drawn from genetics the other drawn from neuroscience.

In the first example, the information content of two loci are estimated over a hierarchical set of clades.
Adami models each loci as a set of independent random variables where each, when sampled, describes the base pair present at a particular position in the gene.
The distributions of these random variables is estimated using genetic data of members of that clade.
This construction allows the entropy of each loci to be calculated at as the sum of entropy over each random variable (the entropy of which is calculated using Shannon's equation).
Because the distributions of these random variables were estimated from empirical data, a correction is applied to the calculated entropy.
The information of the loci is given as the difference between the maximum possible entropy of the loci and the calculated entropy.

In the second example, a pair of metrics to assess the information processing properties of the brain are developed.
The first metric, "predictive information," abstracts sensor states and the motor states are as random variables.
The shared entropy between the sensor states at time t and the motor states at time t + 1 is calculated as a metric of brain functionality and, in a restricted set of circumstances, is found to be related to fitness.
Thus, "predictive information" measures the how tightly behavior is tied to environmental cues.
In contrast, the second family of metrics measures the interaction between individual processing elements of the brain.
The metric "integration" is the shared entropy between individual processing elements in a brain network.
This is calculated by subtracting the total entropy of the network from the sum of entropy of each processing element.
Two more metrics, "stochastic interaction" and "synergistic information" make similar measurements, but take into account the immediately prior state of the network.
"Synergistic information" calculates the difference between network and node-summed shared entropy between the current state and the immediately prior state.
"Stochastic interaction" calculates the difference between network and node-summed total entropy of the current state given the immediately prior state.
This second family of metrics, related to "integrative information," is thought to better describe the ability of a brain to construct "abstract representations of the world" and, therefore, make longer term predictions about the environment (i.e. more than just one time step).

Adami claims that evolution represents the accumulation of information about the environment into the genotype.
From this perspective, brains represent a mechanism for acquiring (and exploiting) environmental information over the course of an individual lifetime.

## misc

Now I'm starting to understand why Adami works with Markov brains.
The states of these brains are super explicit.
