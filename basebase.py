# =============================================================================
#base conversion
# =============================================================================
    
global basebase
basebase = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ~!@#$%^&*()_+[]\;',/{}|:"<>?`~""" # new base range
maxBase = len(basebase)

# =============================================================================
# shuffle basebase for extra encryption
# =============================================================================
# =============================================================================
# def shuffleBase():
#     import random
#     basebase = ''.join(random.sample(basebase,len(basebase)))
#     print(basebase)
# =============================================================================


# finding the minimum possible base
# =============================================================================
def minBase(inp):
    inp = str(inp)
    L = len(inp)
    n = basebase.index(inp[0])
    for i in range(0,L-1,1):
        if n < basebase.index(inp[i+1]):
            n = basebase.index(inp[i+1])
    return n +1

# =============================================================================
# converting n from base to nbase
# =============================================================================
def newBase(n,base, nbase,caseSEnsitive = False):
    n = str(n)
    if (caseSEnsitive == False):
        n = n.lower()
    if(base < minBase(n)):
        raise ValueError("base must be more than %s" %(minBase(n)))
    if(nbase > maxBase):
        raise ValueError("nbase must be less than %s" %(maxBase))
    # first convert form base to base 10
    m = 0
    L = len(n)
    for i in range(0,L,1):
        m += basebase.index(n[i])*(base**(L-i-1))

    # from base 10 to the nbase
    dec = ""
    while (m >= nbase):
        r = m%nbase
        m = m//nbase
        dec =  basebase[r] + dec
    dec = basebase[m] + dec
    return dec
