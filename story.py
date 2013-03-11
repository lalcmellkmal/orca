#!/usr/bin/env python2
from random import choice, randint
from collections import Iterable

"""
Whales vomit sharks which leave the ocean to form sharknadoes which tear across the landscape and the sharks vomit dolphins that fly around and rape people, and the rape causes those people to vomit bees
"""

actors = ['whales', 'sharks', 'dolphins', 'bees', 'bears', 'people']

def As_that_TV_B(As, TV, B):
    return [As, 'that', TV, B]

def As_TV_B(As, TV, B):
    return [As, TV, B]

def Os_which_then_B(Os, B):
    which = 'which'
    return [Os, choice([which, [which, 'then']]), B]

def exit(place):
    return [choice(['leave', 'exit']), place]

def burst_out_action(victim):
    if victim in ('whales', 'sharks', 'dolphins'):
        return exit('the ocean')
    if victim == 'people':
        return 'get in airplanes and fly away'
    if victim == 'bears':
        return exit('the wilderness')
    return 'explode outward'

def form_chimeras(species):
    singular = 'human' if species[-6:] == 'people' else species[:-1]
    if d(2) == 1:
        suffix = 'adoes' if singular[-1] == 'n' else 'nadoes'
    else:
        if singular == 'human':
            singular = 'man'
        suffix = 'quakes'
    return [choice(['form', 'become']), singular + suffix]

def A_in_order_to_B(A, B):
    return [A, 'to', B]

def devastation_by(group):
    desc = choice(['tear across', 'rip across', 'tear up', 'rip up', 'destroy'])
    return [desc, choice(['the landscape', 'cities', 'roads', 'fields'])]

def ITS_HAPPENING():
    instigator = choice(actors)
    victim = choice(actors)

    gtfo = burst_out_action(victim)
    mutants = form_chimeras(victim)
    damage = devastation_by(mutants)
    collateral = Os_which_then_B(mutants, damage)
    andThen = A_in_order_to_B(gtfo, collateral)

    accost = choice(['rape', 'savage', 'conquer', 'maul'])
    if instigator == victim:
        victim = ['more', victim]
    instigate = [instigator, accost, victim]
    story = Os_which_then_B(instigate, andThen)

    pp(story)

def d(n):
    return randint(1, n)

def pp(obj):
    if isinstance(obj, basestring):
        print obj,
    elif isinstance(obj, Iterable):
        for o in obj:
            pp(o)
    else:
        assert False, "Don't know how to prettify " + obj

if __name__ == '__main__':
    ITS_HAPPENING()
