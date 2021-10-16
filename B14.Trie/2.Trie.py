class Trie():
    def __init__(self):
        self.is_end = False
        self.children = {}
    def insert(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True
    def search(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
    def delete(self, s):
        def rec(node, s, i):
            if i == len(s):
                node.is_end = False
                return len(node.children) == 0
            else:
                conti_del = rec(node.children[s[i]], s, i + 1)
                if conti_del:
                    del node.children[s[i]]
                return len(node.children) == 0 and not node.is_end and conti_del
        if self.search(s):
            rec(self, s, 0)
    def retrive_all(self):
        def rec(node, string, strings):
            if node.is_end:
                strings.append("".join(string))
            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, strings)
                string.pop()
        strings = []
        rec(self, [], strings)
        return strings
    
    
if __name__ == "__main__":
    t = Trie()
    n = int(input())
    for _ in range(n):
        t.insert(input())
    cop = int(input())
    for _ in range(cop):
        op, n = list(map(int, input().split()))
        if op == 3:
            for i in t.retrive_all():
                print(i)
        else:
            for _ in range(n):
                if op == 1:
                    print(t.search(input()))
                if op == 2:
                    t.delete(input())
            
            