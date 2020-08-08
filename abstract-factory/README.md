
# Incorrect: kingdom

Creation of KingdomFactory interface, which is composed of
a bunch of interfaces: Castle, King, Army.

Incorrect because we are interested in creating factory that
creates related objects.  Also interested in creating a factory
of factories.

# creation of related objects

1. define an interface for a factory for the creation of related interfaces
1. specify concrete related types when you implement this factory

# FactoryMaker

1. abstracting factory
1. abstracting kingdom

# TODO
interface segregation
- breaking a problem into as many sub interfaces as possible
