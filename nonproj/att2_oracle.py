#!/usr/bin/env python
# encoding: utf-8


class AttOracle(object):

    def __init__(self, heads):
        self.heads = heads
        self.no_children = [0 for i in range(len(heads))]
        for h in heads[1:]:
            self.no_children[h] += 1

    def is_proj(self):
        stack = []
        buffer = [i for i in range(len(self.heads))]
        buffer.reverse()
        children = [0 for i in range(len(self.heads))]

        while True:
            if len(stack) == 1 and len(buffer) == 0:
                return True

            if len(stack) >= 1 and children[stack[-1]] == self.no_children[stack[-1]]:
                if len(stack) >= 2 and self.heads[stack[-1]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-1]
                    continue

            if len(stack) >= 2 and children[stack[-2]] == self.no_children[stack[-2]]:
                if self.heads[stack[-2]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-2]
                    continue

            if len(buffer) > 0:
                stack.append(buffer.pop())
                continue

            return False

    def is_att2(self):
        stack = []
        buffer = [i for i in range(len(self.heads))]
        buffer.reverse()
        children = [0 for i in range(len(self.heads))]

        while True:
            if len(stack) == 1 and len(buffer) == 0:
                return True

            if len(stack) >= 1 and children[stack[-1]] == self.no_children[stack[-1]]:
                if len(stack) >= 2 and self.heads[stack[-1]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 3 and self.heads[stack[-1]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-1]
                    continue

            if len(stack) >= 2 and children[stack[-2]] == self.no_children[stack[-2]]:
                if self.heads[stack[-2]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-2]
                    continue

            if len(stack) >= 3 and children[stack[-3]] == self.no_children[stack[-3]]:
                if self.heads[stack[-3]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-3]
                    continue

            if len(buffer) > 0:
                stack.append(buffer.pop())
                continue

            return False

    def is_var1(self):
        stack = []
        buffer = [i for i in range(len(self.heads))]
        buffer.reverse()
        children = [0 for i in range(len(self.heads))]

        while True:
            if len(stack) == 1 and len(buffer) == 0:
                return True

            if len(stack) >= 1 and children[stack[-1]] == self.no_children[stack[-1]]:
                if len(buffer) >= 1 and self.heads[stack[-1]] == buffer[-1]:
                    children[buffer[-1]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 2 and self.heads[stack[-1]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 3 and self.heads[stack[-1]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-1]
                    continue

            if len(stack) >= 2 and children[stack[-2]] == self.no_children[stack[-2]]:
                if self.heads[stack[-2]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-2]
                    continue

                if len(stack) >= 3 and self.heads[stack[-2]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-2]
                    continue

            if len(stack) >= 3 and children[stack[-3]] == self.no_children[stack[-3]]:
                if self.heads[stack[-3]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-3]
                    continue

                if self.heads[stack[-3]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-3]
                    continue

            if len(buffer) > 0:
                stack.append(buffer.pop())
                continue

            return False

    def is_var2(self):
        stack = []
        buffer = [i for i in range(len(self.heads))]
        buffer.reverse()
        children = [0 for i in range(len(self.heads))]

        while True:
            if len(stack) == 1 and len(buffer) == 0:
                return True

            if len(stack) >= 1 and children[stack[-1]] == self.no_children[stack[-1]]:
                if len(buffer) >= 1 and self.heads[stack[-1]] == buffer[-1]:
                    children[buffer[-1]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 2 and self.heads[stack[-1]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 3 and self.heads[stack[-1]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-1]
                    continue

            if len(stack) >= 2 and children[stack[-2]] == self.no_children[stack[-2]]:
                if len(buffer) >= 1 and self.heads[stack[-2]] == buffer[-1]:
                    children[buffer[-1]] += 1
                    del stack[-2]
                    continue

                if self.heads[stack[-2]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-2]
                    continue

                if len(stack) >= 3 and self.heads[stack[-2]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-2]
                    continue

            if len(stack) >= 3 and children[stack[-3]] == self.no_children[stack[-3]]:
                if len(buffer) >= 1 and self.heads[stack[-3]] == buffer[-1]:
                    children[buffer[-1]] += 1
                    del stack[-3]
                    continue

                if self.heads[stack[-3]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-3]
                    continue

                if self.heads[stack[-3]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-3]
                    continue

            if len(buffer) > 0:
                stack.append(buffer.pop())
                continue

            return False

    def is_var3(self):
        stack = []
        buffer = [i for i in range(len(self.heads))]
        buffer.reverse()
        children = [0 for i in range(len(self.heads))]

        while True:
            if len(stack) == 1 and len(buffer) == 0:
                return True

            if len(stack) >= 1 and children[stack[-1]] == self.no_children[stack[-1]]:
                if len(buffer) >= 1 and self.heads[stack[-1]] == buffer[-1]:
                    children[buffer[-1]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 2 and self.heads[stack[-1]] == stack[-2]:
                    children[stack[-2]] += 1
                    del stack[-1]
                    continue

                if len(stack) >= 3 and self.heads[stack[-1]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-1]
                    continue

            if len(stack) >= 2 and children[stack[-2]] == self.no_children[stack[-2]]:
                if len(buffer) >= 1 and self.heads[stack[-2]] == buffer[-1]:
                    children[buffer[-1]] += 1
                    del stack[-2]
                    continue

                if self.heads[stack[-2]] == stack[-1]:
                    children[stack[-1]] += 1
                    del stack[-2]
                    continue

                if len(stack) >= 3 and self.heads[stack[-2]] == stack[-3]:
                    children[stack[-3]] += 1
                    del stack[-2]
                    continue

            if len(buffer) > 0:
                stack.append(buffer.pop())
                continue

            return False
