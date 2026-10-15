# Factorial computation: initial assessment

No computational advantage has been established. In the complete-layer triangle, one endpoint has n! paths, so outputting each word requires at least n! outputs (and n symbols each if fully written). A direct transition-sum DP uses Theta(n^3) integer additions through column n: each of Theta(k) targets in column k sums Theta(k) predecessors. Sharing the previous column total reduces this to Theta(n^2) additions/assignments if all column entries are materialized. Uniform-layer compression leaves F_k=kF_{k-1}: ordinary sequential multiplication, n-1 nontrivial multiplications. It does not constitute a new factorial algorithm.

Let b=ceil(log_2(n!))+1=Theta(n log n) for n>=2; this follows by bounding n! above by n^n and below by (floor(n/2))^(floor(n/2)). Writing the answer alone takes Omega(b) bit operations. Let M(b) bound multiplication of two b-bit integers, nondecreasing and at least linear. A conservative sequential bound is O(n M(b)); it is loose because one operand is small. A product tree has O(n) arithmetic multiplications and, under standard regularity M(t)/t nondecreasing and comparable-size padding, O(M(b) log n) bit work; each level has total operand length O(b). Storage, sieve cost and unequal operand multiplication matter.

Prime-factor decomposition uses v_p(n!)=sum_{j>=1} floor(n/p^j), followed by powering/product assembly. Prime-swing recursively splits odd parts and powers of two. GMP's manual describes its factorial algorithm and odd-part decomposition; consult the actual implementation/version before performance claims. Relevant primary sources inspected 2026-10-16:

- https://gmplib.org/manual/Factorial-Algorithm (GMP 6.3.0 manual).
- https://github.com/PeterLuschny/Fast-Factorial-Functions (author implementations).
- https://luschny.de/math/factorial/FastFactorialFunctions.htm (author explanation).

No benchmark was run; historic published timings do not predict this machine. General residue products can be compressed into factorial powers, but then standard factorial algorithms remain the appropriate computational primitive. Research takes priority over benchmarking.
