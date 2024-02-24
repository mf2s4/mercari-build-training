def wordPattern(pattern: str, s: str) -> bool:
        words = list(s.split(" "))
        hash_map = {}
        if len(pattern) != len(words): 
            return False

        for i in range(len(words)):
            if pattern[i] not in hash_map:
                if words[i] in hash_map.values():
                    return False
                hash_map[pattern[i]] = words[i]
            elif pattern[i] in hash_map and hash_map[pattern[i]] != words[i]:
                return False
        return True