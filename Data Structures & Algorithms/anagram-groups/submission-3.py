class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}#here dictionary or defualt dict can be used..as you wish..while defaultdict would create a list automatically even if the content doesnt exist
        for word in strs:
            key="".join(sorted(word))
            if key not in group:
                group[key]=[]
            group[key].append(word)

        return list(group.values())
