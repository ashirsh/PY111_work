"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


p_queue = []  # ends from the right side


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    p_queue.append((elem, priority))
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if p_queue:
        pq = sorted(p_queue, key=lambda x: x[1])
        return pq.pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    pq = list(filter(lambda x: x[1] == priority))
    if ind < len(pq):
        return pq[ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    p_queue.clear()
    return None
