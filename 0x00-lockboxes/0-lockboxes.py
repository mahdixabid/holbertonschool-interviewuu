#!/usr/bin/python3



def canUnlockAll(boxes):
    box = []
    for x in range(len(boxes)):
        box.append(False)
    box[0] = True
    box_key = [0]

    for j in box_key:
        for i in boxes[j]:
            if (i not in box_key and i < len(boxes)):
                box[i] = True
                box_key.append(i)
    for k in range(0, len(boxes)):
        if k not in box_key:
            return False
    return True
