class WordDictionary:

    def __init__(self):
        self.node = {}

    def addWord(self, word: str) -> None:
        ro = self.node
        for i in word:
            if i not in ro:
                ro[i] = {}
            ro = ro[i]
        # this tells that this is the end to the word
        ro['*'] = ''

    def search(self, word: str) -> bool:
        def dfs(index, node):

            # Reached the end of the search word
            if index == len(word):
                return '*' in node

            ch = word[index]

            # Wildcard: try every child
            if ch == '.':
                for key in node:
                    if key == '*':
                        continue
                    if dfs(index + 1, node[key]):
                        return True
                return False

            # Normal character
            if ch not in node:
                return False

            return dfs(index + 1, node[ch])

        return dfs(0, self.node)
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)