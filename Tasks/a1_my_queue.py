"""
My little Queue
"""
from typing import Any


my_queue = []  # конец очереди справа


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if my_queue:
        elem = my_queue[0]
        my_queue.pop(0)
        return elem
    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind < len(my_queue):
        return my_queue[ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_queue.clear()
    return None


if __name__ == '__main__':
    enqueue(0)
    enqueue(1)
    enqueue(2)
    print(dequeue())
    print(my_queue)
    print(peek(1))
    print(my_queue)
    print(dequeue())
    print(my_queue)
