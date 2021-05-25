"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class CustomList:
    def __init__(self, *data):
        self.head = None
        node = Item()
        for values in data:
            node.next_node = Item(value=values)
            node = node.next_node

    def append(self, value) -> None:
        new_value = Item(value)
        if self.head is None:
            self.head = new_value
        last_value = self.head
        while last_value.next_node:
            last_value = last_value.next_node
        last_value.next_node = new_value

    def add_start(self, value) -> None:
        new_node = Item(value)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node

    def remove(self, value) -> None:
        if not self.head.value:
            raise ValueError('Attribute was not found.')
        if self.head.value == value:
            self.head = self.head.next_node

        previous_node = self.head
        for node in self:
            if node.value == value:
                previous_node.next_node = node.next_node
                return
            previous_node = node

    def __getitem__(self, index):
        get_value = self.head
        value_index = 0
        while value_index <= index:
            if value_index == index:
                return get_value.value
            value_index += 1
            get_value = get_value.next_node

    def __setitem__(self, index, data) -> None:
        set_value = self.head
        value_index = 0
        while value_index < index:
            set_value = set_value.next_node
            value_index += 1
        # if not set_value:
        #     raise Exception()
        set_value.value = data

    def __delitem__(self, index) -> None:
        del_value = self.head
        value_index = 0
        while value_index <= index:
            if value_index == index:
                self.remove(del_value)
            value_index += 1
            del_value = del_value.next_node

    def find(self, value):
        if self.head.next_node is None:
            raise ValueError('Attribute was not found.')
        if self.head.value == value:
            self.head = self.head.next_node
        next_n = self.head
        while next_n.next_node is not None:
            if next_n.next_node.value == value:
                break
            next_n = next_n.next_node
        if next_n.next_node is None:
            print("Item not found in the list")
        else:
            next_n.next_node = next_n.next_node.next_node

    def clear(self) -> None:
        while self.head != None:
            temp = self.head
            self.head = self.head.next_node
            temp = None

    def __len__(self) -> int:
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node
