import time

# Sample game tree (replace with actual tree from your assignment if different)
def input_game_tree():
    tree = {}
    root = None
    print("Enter nodes and their children. Type 'done' when finished.")
    while True:
        parent = input("Enter parent node (or 'done'): ").strip()
        if parent.lower() == 'done':
            break
        if root is None:
            root = parent  # First entered node is root
        children = input(f"Enter children of {parent} (comma-separated, numbers for leaves): ").strip().split(',')

        # Convert numbers to int for leaves
        children = [int(child.strip()) if child.strip().isdigit() or (child.strip()[0] == '-' and child.strip()[1:].isdigit())
                    else child.strip() for child in children]

        tree[parent] = children
    return root, tree


# Node counter

class Counter:
    def __init__(self):
        self.count = 0

# Question 1: Minimax algorithm
def minimax(node, depth, is_maximizing, tree, counter):
    counter.count += 1
    if isinstance(tree[node][0], int):  # Leaf node
        return max(tree[node]) if is_maximizing else min(tree[node])

    if is_maximizing:
        best = float('-inf')
        for child in tree[node]:
            val = minimax(child, depth + 1, False, tree, counter)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for child in tree[node]:
            val = minimax(child, depth + 1, True, tree, counter)
            best = min(best, val)
        return best

# Question 2: Alpha-beta pruning algorithm
def alpha_beta_minimax(node, depth, alpha, beta, is_maximizing, tree, counter):
    counter.count += 1
    if isinstance(tree[node][0], int):
        return max(tree[node]) if is_maximizing else min(tree[node])

    if is_maximizing:
        best = float('-inf')
        for child in tree[node]:
            val = alpha_beta_minimax(child, depth + 1, alpha, beta, False, tree, counter)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in tree[node]:
            val = alpha_beta_minimax(child, depth + 1, alpha, beta, True, tree, counter)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    print("=== Game Tree Input ===")
    root, tree = input_game_tree()

    # Minimax
    counter_minimax = Counter()
    start = time.perf_counter()
    result_minimax = minimax(root, 0, True, tree, counter_minimax)
    end = time.perf_counter()
    duration_minimax = (end - start) * 1000
    print("\nMinimax Result:", result_minimax)
    print("Minimax Nodes Visited:", counter_minimax.count)
    print("Minimax Time: {:.6f} ms".format(duration_minimax))

    # Alpha-beta pruning
    counter_ab = Counter()
    start = time.perf_counter()
    result_ab = alpha_beta_minimax(root, 0, float('-inf'), float('inf'), True, tree, counter_ab)
    end = time.perf_counter()
    duration_ab = (end - start) * 1000
    print("\nAlpha-Beta Result:", result_ab)
    print("Alpha-Beta Nodes Visited:", counter_ab.count)
    print("Alpha-Beta Time: {:.6f} ms".format(duration_ab))