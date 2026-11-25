#!/usr/bin/env python3
"""Reproduce the illustrative lifetime-limited linewidth calculation."""

import argparse
import math


def positive_finite(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("expected a finite positive number")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lifetime-ms", type=positive_finite, nargs="+",
                        default=[0.1, 1.0, 10.0])
    parser.add_argument("--hypothetical-shift-hz", type=positive_finite, default=0.01)
    args = parser.parse_args()
    print(f"Illustrative inputs. Hypothetical shift: {args.hypothetical_shift_hz:g} Hz")
    print("Lifetime (ms)\tFWHM (Hz)\tFWHM / hypothetical shift")
    for lifetime_ms in args.lifetime_ms:
        linewidth_hz = (1000 / (2 * math.pi)) / lifetime_ms
        print(f"{lifetime_ms:g}\t{linewidth_hz:.6g}\t"
              f"{linewidth_hz / args.hypothetical_shift_hz:.6g}")


if __name__ == "__main__":
    main()
