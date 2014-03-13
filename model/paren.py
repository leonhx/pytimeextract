def paren(s):
    stack = []
    lp = '([{'
    rp = ')]}'
    for c in s:
        if c in lp:
            stack.append(c)
        elif c in rp:
            if rp.index(c) == lp.index(stack[-1]):
                stack.pop()
            else:
                return False
    return not stack

def check_all(arr):
    for e in arr:
        if not paren(e):
            print e
            return False
    return True

p = paren
c = check_all
