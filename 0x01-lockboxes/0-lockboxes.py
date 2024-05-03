#!/usr/bin/env python3
"""
    Defines 0-lockboxes module
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else False
    """
    if not boxes:
        return False

    boxesNumber = len(boxes)
    visitedBox = set()
    queue = [0]

    while queue:
        currentBox = queue.pop(0)
        visitedBox.add(currentBox)

        for key in boxes[currentBox]:
            if 0 <= key < boxesNumber and key not in visitedBox:
                queue.append(key)

    return len(visitedBox) == boxesNumber
