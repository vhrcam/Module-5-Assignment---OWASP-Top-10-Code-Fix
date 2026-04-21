1. Broken Access Control

The vulnerability is that the application allows users to access any profile by changing the userId in the request. There is no authentication or authorization check, which creates an Insecure Direct Object Reference (IDOR). The fix is to enforce authentication and only allow access to the logged-in user’s own ID using session data. This prevents users from accessing other users’ data.
OWASP: https://owasp.org/Top10/A01_2021-Broken_Access_Control/

2. Cryptographic Failures

The issue is the use of weak hashing algorithms like MD5 or SHA1, which are outdated and vulnerable to brute force and collision attacks. Passwords can be easily cracked if exposed. The fix is to use a strong adaptive hashing algorithm like BCrypt or Argon2 with salting. This makes passwords computationally expensive to crack and significantly improves security.
OWASP: https://owasp.org/Top10/A02_2021-Cryptographic_Failures/

3. Injection

The vulnerability occurs because user input is directly concatenated into SQL queries, allowing attackers to manipulate queries (SQL injection). The fix is to use prepared statements or parameterized queries, which separate code from data and prevent malicious input from altering the query structure.
OWASP: https://owasp.org/Top10/A03_2021-Injection/

4. Insecure Design

The flaw is that password resets can be performed without verifying user identity, meaning anyone can reset any account password. The fix is to implement secure design practices such as token-based password reset verification sent to the user’s email. This ensures only the legitimate user can reset their password.
OWASP: https://owasp.org/Top10/A04_2021-Insecure_Design/

5. Software and Data Integrity Failures

The issue is loading external scripts without verifying their integrity. If the external source is compromised, malicious code can run in the application. The fix is using Subresource Integrity (SRI) hashes to ensure files have not been tampered with before execution.
OWASP: https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/

6. Server-Side Request Forgery (SSRF)

The vulnerability allows users to make the server request arbitrary URLs, including internal systems. This can expose internal services or cloud metadata. The fix is to validate and restrict allowed domains or use a whitelist so the server only makes requests to trusted sources.
OWASP: https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery/

7. Identification and Authentication Failures

The issue is insecure password handling, often involving plaintext storage or weak comparison methods. This allows attackers to easily compromise accounts. The fix is to use secure password hashing algorithms like BCrypt and proper password verification methods instead of direct comparison.
OWASP: https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

8. Software and Data Integrity Failures (Supply Chain Risk)

The vulnerability is relying on external CDNs without verifying file integrity. If the CDN is compromised, attackers can inject malicious scripts. The fix is using Subresource Integrity (SRI) and trusted sources to ensure scripts are not modified.
OWASP: https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/

9. Server-Side Request Forgery (SSRF)

This occurs when user-controlled input determines server-side HTTP requests, allowing attackers to reach internal or restricted systems. The fix is to validate URLs, enforce allowlists, and block internal IP ranges.
OWASP: https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery/

10. Identification and Authentication Failures

The vulnerability is weak authentication where passwords are directly compared or stored insecurely. This makes accounts easy to compromise. The fix is to store hashed passwords using secure algorithms like BCrypt and verify using secure comparison functions.
OWASP: https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/
