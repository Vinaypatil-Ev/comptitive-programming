class Trie:
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
        return True if node.is_end else False
    def delete(self, s):
        def delete_wrap(node, s, n):
            if n == len(s):
                node.is_end = False
                return len(node.children) == 0
            else:
                may_i_delete = delete_wrap(node.children[s[n]], s, n + 1)
                if may_i_delete:
                    del node.children[s[n]]
                return may_i_delete and not node.is_end and len(node.children) == 0
        
        if self.search(s):
            delete_wrap(self, s, 0)
        else:
            raise NameError(f"\"{s}\" not found")
        
    def get_strings(self):
        def find_strings(node, string, strings):
            if node.is_end:
                strings.append("".join(string))
            for ch in node.children:
                string.append(ch)
                node = node.children[ch]
                find_strings(node, string, strings)
                string.pop()
        
        strings = []
        find_strings(self, [], strings)
        return strings
            
if __name__ == "__main__":
    t = Trie()
    t.insert("vinay")
    t.insert("vinaysunil")
    t.insert("vinaysunilpatil")
    # t.insert("linaysunilpatil")
    # print(t.children)
    # print(t.search("vina"))
    # t.delete("jiji")
    x = t.get_strings()
    print(x)

