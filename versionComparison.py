'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
'''
def compareVersion(version1, version2):

    # if len(version1.split(".")) > len(version2.split(".")):
    #     return 1

    v1 = [int(v) for v in version1.split(".")]
    v2 = [int(v) for v in version2.split(".")]

    for i in range(max(len(v1), len(v2))):
        m = v1[i] if i < len(v1) else 0
        n = v2[i] if i < len(v2) else 0
        if m > n:
            return 1
        elif m < n:
            return -1

    return 0