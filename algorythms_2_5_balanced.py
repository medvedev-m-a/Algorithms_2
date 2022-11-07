def GenerateBBSTArray(a: list) -> list:
    if len(a) == 0:
        return a

    # отсортировать массив а
    a.sort()
    node_que = [a]

    bst_array = []
    while node_que:
        curr = node_que.pop(0)
        root = center(curr)
        bst_array.append(curr[root])
        if len(curr) > 1:
            node_que.append(curr[:root])
            node_que.append(curr[root+1:])

    return bst_array


def center(a: list):
    return (len(a) - 1) // 2
