def canUnlockAll(boxes):
    """
    This script contains a function that determines if all the box
    in an array of boxes can be opened.
    """
    boxLen = len(boxes)
    # I will set the total number of unlocked boxes
    # to be just one, which is the first
    unlocked_boxes = set([0])
    # I will set the keys to the first box as 0
    keys = [0]

    while keys:
        # Get the current key (which is the index of the box we're looking at)
        current_key = keys.pop()
        # Iterate over all keys found in the current box
        for key in boxes[current_key]:
            # Check if the key corresponds to a new
            # box and is within length range
            if key not in unlocked_boxes and key < boxLen:
                # Mark the box as unlocked
                unlocked_boxes.add(key)
                # Add the new key to the list of keys to be processed
                keys.append(key)
