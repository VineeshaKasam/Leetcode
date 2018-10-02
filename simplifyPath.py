'''
Given an absolute path for a file (Unix-style), simplify it.
'''

def simplifyPath(path):
    words = [word for word in path.split("/") if word != '.' if word != ""]
    mystack = []

    for s in words:
        if s == "..":
            if len(mystack) > 0: mystack.pop()
        else:
            mystack.append(s)

    result = "/" + "/".join(mystack)
    return result