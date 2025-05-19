def rabin_karp(text: str, pattern: str) -> int:
    """
    Return the index of the first occurrence of `pattern` in `text`,
    or -1 if not found. Uses a rolling hash (Rabin–Karp).
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1

    # Choose a base and a modulus
    B = 256                   # number of possible characters (e.g. extended ASCII)
    M = 2**61 - 1             # a large Mersenne prime for fast mod

    # Precompute B^(m-1) % M for use in removing the leading char
    B_m1 = pow(B, m-1, M)

    # Compute hash(pattern) and hash(text[0:m])
    h_pat = 0
    h_txt = 0
    for i in range(m):
        h_pat = (h_pat * B + ord(pattern[i])) % M
        h_txt = (h_txt * B + ord(text[i])) % M

    # If first window matches, double-check to avoid collision
    if h_txt == h_pat and text[:m] == pattern:
        return 0

    # Slide the window over text
    for i in range(1, n - m + 1):
        # Remove leading char, add trailing char
        leading = ord(text[i-1]) * B_m1
        h_txt = (h_txt * B - leading + ord(text[i+m-1])) % M

        # Python’s % can return negative, force positive
        if h_txt < 0:
            h_txt += M

        # On hash match, verify by direct comparison
        if h_txt == h_pat and text[i:i+m] == pattern:
            return i

    return -1
