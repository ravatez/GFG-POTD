class Solution:
    def minTime(self, root, target):
        # code here
        # locate node
        parent = []
        def find_target(node):
            if node:
                if node.data == target:
                    return node
                parent.append(node)
                left = find_target(node.left)
                if left:
                    return left
                right = find_target(node.right)
                if right:
                    return right
                parent.pop()
                return None
            else:
                return None
        target_node = find_target(root)
        time = 0
        if not target_node:
            return time
        next_burn = []
        if target_node.left:
            next_burn.append(target_node.left)
        if target_node.right:
            next_burn.append(target_node.right)
        burnt = {target_node.data}
        if parent:
            next_burn.append(parent[-1])
            parent.pop()
        while next_burn:
            temp = []
            for node in next_burn:
                if node:
                    burnt.add(node.data)
                    if node.left and node.left.data not in burnt:
                        temp.append(node.left)
                    if node.right and node.right.data not in burnt:
                        temp.append(node.right)
            if parent:
                temp.append(parent[-1])
                parent.pop()
            time += 1
            next_burn = temp
        return time