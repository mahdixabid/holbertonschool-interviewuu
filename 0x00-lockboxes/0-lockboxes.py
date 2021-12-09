#!/usr/bin/python3
"""checking all locked boxes"""


def canUnlockAll(boxes):
    u = [0]
    if len(boxes) == 0:
        return True
    for box in u:
        for key in boxes[box]:
            if key not in u:
                if key < len(boxes):
                    u.append(key)

    if len(u) == len(boxes):
        return True
    return False
