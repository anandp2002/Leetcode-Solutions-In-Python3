class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for char in "".join(set(s)):
            first_index=s.find(char)
            second_index=s.find(char,first_index+1)
            dist=second_index-first_index-1
            if distance[ord(char)-97]!=dist:
                return False
        return True