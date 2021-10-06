class Trie:
    def __init__(self, ):
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
            node = node.children
        return True
    
    def delete(self, s):
        def rec(node, s, i):
            if i == len(s):
                node.is_end == False
                return len(node.children) == 0
            else:
                may_i_del = rec(node.childern[s[i]], s, i + 1)
                if may_i_del:
                    del node.childeren[s[i]]
                return len(node.children) == 0 and may_i_del and not node.is_end
        if self.search(s):
            rec(self, s, 0)
    
    def get_strings(self):
        def rec(node, string, strings):
            if len(node.children) == 0:
                strings.append("".join(string))
                return
            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, strings) 
                string.pop()
        
        strings = []
        rec(self, [], strings)
        return strings
    def prefix(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return 
            node = node.children[ch]
        return [prefix + word for word in node.get_strings()]

if __name__ == "__main__":
    t = Trie()
    while True:
        try:
            print("INput: ")
            i = int(input())
            if i not in range(1, 5+1):
                raise KeyError
        except:
            print("correct input [1 2 3 4 5]")
            i = int(input())
        if i == -1:
            break
        
        if i == 1:
            print("insert")
            for _ in range(int(input("opc: "))):
                t.insert(input(f"{_}: "))
        if i == 4:
            print("all: ")
            print(t.get_strings())
        if i == 5:
            print("serch engine")
            print(t.prefix(input("prefix: ")))