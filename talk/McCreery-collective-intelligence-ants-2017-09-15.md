# Collective intelligence in ants: group decisions and strategy

Helen McCreery
9-15-2017
MSU BEACON

## synopsis

Motivation: how does complexity and patterns emerge from groups?

Cooperative transport.
This is a hard task! (for bot ants and people).
It is a classic problem in robotics.

The ants need to make a collective decision about which direction to move the grasshopper.
Most ant species can't do this very well.
The ants will need to navigate around obstacles, as well.
They need to make another decision about travel direction.

What individual-level traits promote group consensus?
  1. behavioral rules
    * do workers behave differently in groups?
    * can groups following simple behavioral rules reach consensus? how simple is too simple?
    * what minimum information is required?
  2. persistence

Problem solving: what strategy, if any, do groups use to navigate obstacles?

To model behavioral rules, consider three "teams":
  * left
  * right
  * disengaged
Ants can move from left and right to disengaged, from disengaged to left or right.

strategies:
  * uninformed: same behavior regardless
  * oblivious: less likely to give up if the group is successful
  * informed: give up if your directionis unpopular

Informed ants more likely to reach consensus.
Ants just need to know if they are algined with the majority.

Theory predicts individual persistence promotes group coordination.
Are more persistent species more coordinated?
Two types of persistence considered: total engagement effort (proportion of time spent actively trying to move the object) and local engagement time (average length of pulling bouts).

Coordination measures: sinuosity (total path length divided by displacement) and proportion of successful moving attempts.

By adding fake ants with infinite persistence (weighted string), high persistence seems to reduce sinuosity.

Simple vs robust strategies:
  * simple follow perimiter until can go towards nest (gets stuck at concave obstacles)
  * robust follow perimeter until it's possible to go towards nest and youy are closer to nest than before

The crazy ants succeed at the concave obstacle, but it takes some time.
Earlier: spend most of the time at the wall closest to the nest.
Later: started exploring more of the space.
The ants move further backwards the longer they have been stuck.
The ants are moving to a more robust strategy the longer they've been stuck.

## misc

Helen is a new postdoc at MSU.
This work was done for her dissertation at UC Boulder.
Helen's website is [www.helenmccreery.com](www.helenmccreery.com).
Her email is hmccreery@gmail.com.

## questions

Did how well-informed ants were in behavioral rule choice affect the frequency at which a left or a right choice was ultimately made?
