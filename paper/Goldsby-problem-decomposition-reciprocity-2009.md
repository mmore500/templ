# Problem Decomposition Using Indirect Reciprocity in Evolved Populations

Goldsby
2009
created: 8-9-2017

## synopsis

Goldsby et al. take on problem decomposition.
The idea is to evolve solutions to subproblems and combine them to solve a larger problem.
Ultimately, it would be best if the evolving system were able to dynamically define subproblems (i.e. manual identification of subproblems was not necessary).
Goldsby claims that this paper is a step in that direction.

Specifically, Goldsby et al. demonstrate an evolving system where individuals display generalist behavior while evolving to solve simple problems and display specialist behavior, cooperating to form complete solutions, while evolving to solve more complex problems.
Nevertheless, problem decomposition is facilitated by manual design of cooperation mechanisms that very explicitly support a particular form of cooperation (i.e. manual identification of problem decomposition and explicit support for that decomposition).

The task that Goldsby et al. set out for Avidians is to produce a bitstring of all 1's and a bitstring of all 0's.
The complexity of the task is increased by lengthening the bitstrings that must be produced.
Individuals can produce both bitstrings themselves or specialize to produce one bitstring and exchange for the other.
Exchange is facilitated by a reputation score, which flags individuals that are freeloading off of other's bitstrings without making any contributions, and tags applied to organisms by the environment that specify which string they are best at producing.

Goldsby confirms that generalism is more effective at solving the simple task than cooperation by comparing the ability of organisms evolved in enforced cooperation and enforced generalism schemes to solve the simple task.
Enforced cooperation is realized by only allowing organisms to produce single bitstrings (so they must barter for the other).
Enforced generalism is realized by turning off the ability for organisms to exchange bitstrings.
In a similar manner, Goldsby also confirms that cooperation is more effective at solving the complex task.
At different task complexities, organisms evolved in a non-enforced regime (where generalism and cooperation are both viable strategies) match or exceed the performance of organisms evolved under both enforced generalism and enforced cooperation schemes.

## misc

The door is left open to work with more complicated problems as well evolving a reputation and tag system (instead of explicit manual definition).

Kin selection is ruled out by using a mass action replacement strategy.
