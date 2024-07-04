#!/usr/bin/python3
"""
Module for canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = boxes[0]

    for key in keys:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
