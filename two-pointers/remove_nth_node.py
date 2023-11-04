from typing import Optional, TypeVar

from toolbox.linked_list.node import Node, build

T = TypeVar('T')


def move_fast_pointer(ll: Node[T], nth: int) -> Optional[Node[T]]:
    fast = ll

    i = 0
    while fast is not None and i < nth:
        fast = fast.next
        i += 1

    return fast


def remove_nth_node(ll: Node[T], nth: int) -> Optional[Node[T]]:
    slow = ll
    fast = move_fast_pointer(ll, nth)

    if fast is None:
        return ll.next

    while not fast.is_tail():
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return ll


if __name__ == '__main__':

    ll = build([2, 4, 6, 8, 10, 20])

    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 1).print()
    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 2).print()
    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 3).print()
    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 4).print()
    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 5).print()
    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 6).print()
    remove_nth_node(build([2, 4, 6, 8, 10, 20]), 7).print()

