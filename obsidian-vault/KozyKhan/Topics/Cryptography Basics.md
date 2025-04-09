> **February 8th, 2025**  **14:07:48** 
> **Topics:** [[
> **Tags:** #
---

**Cryptography Basics: Securing Digital Information**

  

**1. What is Cryptography?**

  

Cryptography is the **science of securing communication and data** through mathematical techniques. It ensures:

• **Confidentiality** → Only authorized users can access data.

• **Integrity** → Data remains unchanged and authentic.

• **Authentication** → Verifies the identity of users and systems.

• **Non-Repudiation** → Prevents denial of actions (e.g., digital signatures).

**2. Types of Cryptography**

  

Cryptography is classified into **three main types**:

  

**1. Symmetric Encryption (Secret Key)**

• Uses **one key** for both **encryption and decryption**.

• Fast and efficient but requires **secure key exchange**.

  

**Example: AES (Advanced Encryption Standard)**

```
Hello → (Encrypt with Key) → 🗝 → 5gH1!2x → (Decrypt with Key) → Hello
```

**Common Algorithms:**

✔ AES (128-bit, 192-bit, 256-bit) – Used in government and military.

✔ DES (outdated, replaced by AES).

✔ Blowfish (fast but less popular today).

**2. Asymmetric Encryption (Public & Private Keys)**

• Uses **two keys**:

• **Public Key** (Encrypts data, can be shared).

• **Private Key** (Decrypts data, kept secret).

• Solves key exchange problems but **slower than symmetric encryption**.

  

**Example: RSA (Rivest-Shamir-Adleman)**

```
Message → (Encrypt with Public Key) → 🔒 → Encrypted Data → (Decrypt with Private Key) → Message
```

**Common Algorithms:**

✔ **RSA** (Used in SSL/TLS for secure web connections).

✔ **ECC (Elliptic Curve Cryptography)** – More efficient than RSA.

**3. Hashing (One-Way Encryption)**

• Converts data into a **fixed-length hash**.

• **Irreversible** → Cannot decrypt back to original data.

• Used for **password storage, digital signatures, and data integrity**.

  

**Example: Hashing Passwords**

```
Password123 → (SHA-256) → a1b2c3d4e5f6g7h8i9
```

**Common Hashing Algorithms:**

✔ **SHA-256 (Secure Hash Algorithm)** – Used in Bitcoin and cybersecurity.

✔ **MD5 (Message Digest 5)** – **Not secure** (vulnerable to collisions).

✔ **Bcrypt, Argon2** – Used for secure password hashing.

**3. Cryptographic Applications**

  

**1. Secure Communication**

  

✔ **SSL/TLS (HTTPS)** – Encrypts web traffic (padlock symbol in browsers).

✔ **End-to-End Encryption (E2EE)** – Used in **WhatsApp, Signal, ProtonMail**.

  

**2. Digital Signatures & Certificates**

  

✔ Used to verify **authenticity** of emails, software, and documents.

✔ Example: **PGP (Pretty Good Privacy)** for secure email communication.

  

**3. Cryptocurrency & Blockchain**

  

✔ **Bitcoin & Ethereum** use **cryptographic hashing (SHA-256, Keccak)**.

✔ **Public-private keys** secure cryptocurrency wallets.

  

**4. Secure Password Storage**

  

✔ Websites store **hashed and salted passwords** instead of plaintext.

✔ Example:

```
"mypassword" → (Bcrypt Hash) → $2a$10$abc123...
```

**4. Attacks on Cryptography**

  

**1. Brute Force Attack**

• Tries **all possible keys** until finding the correct one.

• **Prevention:** Use **longer key sizes** (e.g., AES-256, RSA-4096).

  

**2. Man-in-the-Middle (MitM) Attack**

• Attacker **intercepts communication**.

• **Prevention:** Use **TLS/SSL encryption** and **digital certificates**.

  

**3. Quantum Computing Threat**

• **Future quantum computers** could break RSA & ECC.

• **Solution:** Research into **Post-Quantum Cryptography**.

**5. Conclusion**

  

Cryptography is the **foundation of digital security**, protecting **data, communication, and authentication**. Mastering **encryption (AES, RSA), hashing (SHA-256, Bcrypt), and security protocols (SSL/TLS, blockchain)** is essential for **modern cybersecurity**. 🚀