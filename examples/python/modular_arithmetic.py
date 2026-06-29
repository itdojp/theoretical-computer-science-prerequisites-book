from __future__ import annotations


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (g, x, y) such that ax + by = g = gcd(a,b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a: int, n: int) -> int:
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % n


def toy_rsa_roundtrip(message: int, p: int = 5, q: int = 11, e: int = 3) -> tuple[int, int]:
    """Educational toy RSA. Do not use for real cryptography."""
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    cipher = pow(message, e, n)
    plain = pow(cipher, d, n)
    return cipher, plain


if __name__ == "__main__":
    print("gcd(84, 30)=", gcd(84, 30))
    print("inverse of 7 mod 26=", mod_inverse(7, 26))
    print("toy RSA roundtrip:", toy_rsa_roundtrip(12))
