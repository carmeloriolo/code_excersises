class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hmap = dict()
        # Time Complexity O(n^2)
        for path in paths:
            splitted = path.split(' ')
            dir = splitted[0]
            files = splitted[1::]
            for f in files:
                fsplit = f.split('(')
                fcontent = fsplit[1][:-1]
                fname = fsplit[0]
                if fcontent not in hmap.keys():
                    hmap[fcontent] = ["{}/{}".format(dir, fname)]
                else:
                    hmap[fcontent].append("{}/{}".format(dir, fname))

        # Space Complexity O(n)
        return filter(lambda x: len(x) > 1, hmap.values())
