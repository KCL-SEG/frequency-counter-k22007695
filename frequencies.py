"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter
def stringList (items):
    return [str(i) for i in items]


def frequencies(items):
    frequencies = {}
    items = stringList(items)
    frequencies=dict(Counter(items))
    return frequencies
