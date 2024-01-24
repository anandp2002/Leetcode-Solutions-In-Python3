class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        word_to_morse={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        res=[]
        for word in words:
            morse=""
            for char in word:
                morse+=word_to_morse[char]
            res.append(morse)
        return len(set(res))            