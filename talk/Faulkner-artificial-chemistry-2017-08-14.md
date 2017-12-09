# Implicit AChems

Penelope Faulkner
8-14-2017
BEACON

## synopsis

As a raw concept, a system with atomic building blocks you can throw together to produce emergent behavior.

**idea:** We can't predict without running it what the larger particles will be like.

common structure :
* `S` - set of particles
* `R` - set of interaction rules
* `A` - everything else (environment, physics, spatiality, temperature)

**question:** Can we come up with a mathematical description of what an artificial chemistry is?

types of nodes in a Metachem graph:
* transfer nodes
    * sampling nodes
* control nodes
    * action nodes
    * decision nodes
* container nodes
    * tank node (particles here can't be changed)
    * sample nodes (particles here can be changed)
    * environment node

### Penny's artificial chemistry

design philosophy: don't try to explicitly develop towards certain goals, but try to avoid decisions that would prevent that behavior from occurring

* **atoms:** hermitian matrices
* **linking:** probability of occurrence determined by eigenvalues, Jordan product forms new combined particle
  * commutative, but non-associative properties of Jordan algebra allows for isomers

### Avida as an artificial chemistry
* **atom**: singular instruction
* **particle**: genotype
* **instance**: physics of the system, state of the particle in the environment
* **environment**: grid itself, distribution of resources, events


## wrapping up
**goal:** design an observer that can recognize self-replication in artificial chemistry
* then try to understand the differences between chemistries where self-replication occurs vs not
* how to recognize self-replication at a higher level (i.e. not just molecules self-replicating)

**another goal:** make elements of artificial chemistry modular so that, for example, spatiality can be easily added to an artificial chemistry

**another goal:** define translations between artificial chemistries so that you can run two systems together

## misc
the tikZ diagrams look nice
