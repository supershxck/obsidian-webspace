> **February 8th, 2025**  **15:19:35** 
> **Topics:** [[
> **Tags:** #
---

**Logic and Proofs in Discrete Mathematics**

  

**1. What is Logic?**

  

Logic is the **foundation of mathematical reasoning** and is used to **analyze, construct, and validate arguments**. It involves the use of **symbols, statements, and rules** to determine the truth of expressions.

  

**Why is Logic Important?**

  

✔ **Used in computer science** – Essential for algorithms, AI, and programming.

✔ **Foundation of mathematical proofs** – Ensures correctness of theorems.

✔ **Forms basis for digital circuits** – Boolean logic is used in computers.

✔ **Improves reasoning skills** – Helps in problem-solving and decision-making.

**2. Propositional Logic**

  

**1. What is a Proposition?**

  

A **proposition** is a **statement that is either true (T) or false (F)**.

  

✔ **Examples:**

• “2 + 2 = 4” (**True**)

• “The sun is a planet” (**False**)

  

✔ **Non-Propositions:**

• “How are you?” (Not a statement)

• “x + 2 = 5” (Depends on x, not a fixed truth value)

**2. Logical Operators**

|**Operator**|**Symbol**|**Meaning**|**Example**|
|---|---|---|---|
|**Negation**|¬P|NOT P|¬(True) = False|
|**Conjunction**|P ∧ Q|AND|True ∧ False = False|
|**Disjunction**|P ∨ Q|OR|True ∨ False = True|
|**Implication**|P → Q|If P then Q|True → False = False|
|**Biconditional**|P ↔ Q|P if and only if Q|True ↔ True = True|

✔ **Example: Truth Table for AND (∧)**

|**P**|**Q**|**P ∧ Q**|
|---|---|---|
|T|T|T|
|T|F|F|
|F|T|F|
|F|F|F|

✔ **Example: Truth Table for OR (∨)**

|**P**|**Q**|**P ∨ Q**|
|---|---|---|
|T|T|T|
|T|F|T|
|F|T|T|
|F|F|F|

**3. Logical Equivalences**

  

Logical equivalences are **statements that have the same truth values** in all possible cases.

  

✔ **Important Logical Laws:**

|**Law**|**Formula**|
|---|---|
|**Identity Law**|P ∨ False = P, P ∧ True = P|
|**Domination Law**|P ∨ True = True, P ∧ False = False|
|**Idempotent Law**|P ∨ P = P, P ∧ P = P|
|**Double Negation**|¬(¬P) = P|
|**De Morgan’s Laws**|¬(P ∧ Q) = ¬P ∨ ¬Q, ¬(P ∨ Q) = ¬P ∧ ¬Q|
|**Implication Law**|P → Q = ¬P ∨ Q|

✔ **Example: Using De Morgan’s Law**

```
¬(P ∧ Q) = ¬P ∨ ¬Q
```

✔ **Example: Converting Implication**

```
P → Q = ¬P ∨ Q
```

**4. Predicate Logic (First-Order Logic)**

  

Predicate Logic extends propositional logic by **introducing variables and quantifiers**.

  

✔ **Example of a Predicate Statement:**

```
P(x): x is an even number
```

✔ **Quantifiers:**

|**Symbol**|**Meaning**|**Example**|
|---|---|---|
|**Universal Quantifier**|∀x (For all x)|∀x P(x): “All x are even”|
|**Existential Quantifier**|∃x (There exists an x)|∃x P(x): “There is at least one even x”|

✔ **Example: Translating Statements to Logic**

• “All humans are mortal.”

```
∀x (Human(x) → Mortal(x))
```

  

• “Some numbers are even.”

```
∃x (Even(x))
```

**5. Methods of Proof**

  

Mathematical proofs are **structured arguments** used to demonstrate the truth of a statement.

  

**1. Direct Proof**

  

A direct proof shows that **if P is true, then Q must also be true**.

  

✔ **Example:** Prove that if n is even, then n² is even.

  

✔ **Proof:**

• Let n = 2k (definition of even numbers).

• Then n² = (2k)² = 4k² = 2(2k²), which is **even**.

**2. Proof by Contrapositive**

  

Proves P → Q by proving ¬Q → ¬P.

  

✔ **Example:** Prove that if n² is odd, then n is odd.

  

✔ **Proof:**

• Assume n is even (n = 2k).

• Then n² = 4k², which is **even**.

• Since n² is not odd, n must be **odd**.

**3. Proof by Contradiction**

  

Assumes the **opposite of the statement** and derives a contradiction.

  

✔ **Example: Proof that √2 is irrational**

• Assume √2 **is rational**, so √2 = p/q (where p and q are integers with no common factors).

• Squaring both sides: 2 = p² / q² → p² = 2q², so p² is even.

• Since p² is even, p must be even, so p = 2k.

• Substituting: (2k)² = 2q² → 4k² = 2q² → q² = 2k², so q is even.

• Since p and q are both even, they share a common factor (2), which contradicts our assumption.

• ∴ **√2 is irrational**.

**4. Proof by Induction**

  

Used for proving statements about **natural numbers**.

  

✔ **Example: Prove that the sum of the first n positive integers is**:

```
1 + 2 + ... + n = n(n+1)/2
```

✔ **Proof (Induction):**

1. **Base Case (n = 1)**:

```
1 = 1(1+1)/2 = 1
```

✅ Holds true.

  

2. **Inductive Step (n = k to n = k+1)**:

Assume 1 + 2 + ... + k = k(k+1)/2.

1. Prove for n = k + 1:

```
(1 + 2 + ... + k) + (k+1) = (k(k+1)/2) + (k+1)
```

Simplifies to:

```
(k+1)(k+2)/2
```

✅ Matches formula, so **proof is complete**.

**6. Applications of Logic and Proofs**

|**Field**|**Application**|
|---|---|
|**Computer Science**|Algorithm design, AI, formal verification|
|**Mathematics**|Theorem proving, set theory|
|**AI & Machine Learning**|Logical reasoning, rule-based systems|
|**Cybersecurity**|Cryptographic proofs|
|**Software Engineering**|Testing, debugging, verifying correctness|

✔ **Example: Boolean Logic in Programming**

```
if not (A and B):
    print("Condition met")
```

✔ **Example: AI Decision Making Using Logic**

```
mortal(X) :- human(X).
human(socrates).
?- mortal(socrates).  // True
```

**7. Conclusion**

  

Logic and proofs **form the backbone of mathematics and computer science**. Understanding **propositional logic, predicate logic, proof techniques, and logical equivalences** is essential for **algorithms, programming, AI, and cybersecurity**. 🚀