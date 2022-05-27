from RBTreeClasses import RBTreeClass


def load_dictionary(file):
    d_tree = RBTreeClass.RBTree()
    try:
        with open(file, "r") as fd:
            for line in fd:
                line = line.strip()
                d_tree.insert(line)
    except FileNotFoundError:
        return None
    return d_tree
