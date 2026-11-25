# Mission 07 — How Computers Communicate

## 1. Task / objective
Explore fundamental computer networking principles, define key network scopes and topologies, explain packet-switched routing and client-server interactions, inspect DNS translation models and connectivity diagnostics, and trace the end-to-end multi-layer request lifecycle when opening a website in a browser.

## 2. Work completed
- Completed the core network concepts definition table with clear real-world examples.
- Documented network connectivity diagnostics (`ping`) and DNS resolution tools (`nslookup` / `dig`).
- Traced the comprehensive 6-step lifecycle of navigating to a website, correctly integrating the concepts of client, server, DNS, TCP/IP, and HTTP/HTTPS protocols.
- Ensured all outputs adhere strictly to privacy guidelines (redacting private IP addresses and home network identifiers).

## 3. Commands / tools used

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A localized computer network interconnecting devices within a limited, distinct physical area such as a residence, school laboratory, or office floor. | Home Wi-Fi network connecting laptops, smartphones, and a wireless printer. |
| **MAN (Metropolitan Area Network)** | A high-bandwidth network infrastructure spanning an entire city or large educational/corporate campus, larger than a LAN but smaller than a WAN. | Municipal cable broadband network or university multi-campus optical backbone network. |
| **WAN (Wide Area Network)** | A telecommunications or computer network spanning vast geographical boundaries, countries, or the globe, interconnecting multiple smaller networks. | The global public Internet, or an enterprise network linking offices in London, Tokyo, and New York. |
| **DNS (Domain Name System)** | The distributed naming service of the Internet that translates human-friendly alphanumeric domain names into machine-readable numeric IP addresses. | Translating `example.com` into destination IPv4 address `93.184.215.14`. |
| **Router** | An intelligent Layer 3 network hardware device that analyzes IP packet destination headers and forwards packets between different network subnets along the optimal path. | Home gateway router forwarding outbound web traffic from local LAN (`192.168.x.x`) to ISP gateway. |
| **Protocol** | An agreed-upon standardized set of formal rules and data formatting conventions governing how devices format, transmit, verify, and receive data. | Hypertext Transfer Protocol Secure (HTTPS), Transmission Control Protocol (TCP), Internet Protocol (IP). |
| **Packet switching** | A transmission methodology where continuous data streams are broken into small, individually addressed chunks ("packets") that travel independently across network paths and are reassembled at the destination. | Transferring an image or video file across the internet where packet segments take varied routing paths before arriving. |
| **Client-server** | A distributed computing architecture where service requestors ("clients") initiate requests and dedicated centralized providers ("servers") listen, process, and respond. | A web browser (client) requesting a web page from an Apache or Nginx web hosting server (server). |

---

### Task 7.2 — Observe network information

- **What a connectivity test helps you check:**
  A network connectivity test (such as `ping`) verifies whether a remote host is actively reachable across the network, measures the round-trip latency (time taken for packets to reach the destination and return in milliseconds), and reports packet loss percentages to evaluate network stability.
- **What information a DNS lookup displays:**
  A DNS lookup utility (such as `nslookup` or `dig`) displays the authoritative or non-authoritative DNS server responding to the query, the query resolution latency, and the resulting record mappings—specifically the domain's Canonical Name (CNAME), IPv4 Address (A Record), and IPv6 Address (AAAA Record).
- **DNS observation example (privacy-safe):**
  - Command: `nslookup example.com`
  - Output summary:
    - Server: Resolver Gateway (`[redacted-local-dns]`)
    - Name: `example.com`
    - Address: `93.184.215.14` (IPv4) / `2606:2800:21f:cb07:6820:80da:af6b:8b2c` (IPv6)
- **Role of DNS when entering a website name:**
  When a user enters a URL into a web browser address bar, the browser cannot send data packets using text names like `example.com`. DNS acts as the Internet's telephone directory: it intercepts the human-readable domain name, resolves it to its corresponding IP address, and returns that numeric address to the browser so direct network socket connections can be opened.

---

### Task 7.3 — What happens when you open a website?

A complete 6-step trace from URL entry to rendering:

1. **User Input and URL Parsing (Client):**
   The user types `https://example.com` into the web browser (**client**). The browser parses the URL into the **protocol** (`https`), host domain (`example.com`), and default resource path (`/`).
2. **DNS Resolution (Domain Name System):**
   The browser checks its internal cache, OS resolver cache, and queries the local recursive **DNS** resolver to translate `example.com` into the destination IP address (`93.184.215.14`).
3. **Establishing Transport Connection (TCP/TLS Handshake):**
   Using the resolved IP address, the client initiates a Transmission Control Protocol (**TCP**) three-way handshake (`SYN`, `SYN-ACK`, `ACK`) with the destination server over port 443, followed by a Transport Layer Security (**TLS**) cryptographic handshake to establish secure end-to-end encryption.
4. **Packet Routing Across Networks (Router / Packet Switching):**
   The client's network interface frames the data into IP packets. The local **router** examines the destination IP header and routes the packets hop-by-hop across intermediate Internet Service Provider (ISP) routers via **packet switching** to reach the host server.
5. **Request Processing and Response Generation (Server):**
   The remote web **server** receives the decrypted HTTP `GET /` request, validates headers, retrieves the requested HTML document, and transmits an `HTTP/1.1 200 OK` response payload containing the webpage markup back to the client.
6. **Parsing and Visual Rendering (Client Display):**
   The browser (**client**) receives the response packets, reassembles them, parses the HTML DOM tree, downloads associated CSS, JavaScript, and image assets, and paints the formatted webpage onto the user's screen.

## 5. Difficulties faced
No difficulties encountered. Diagnostics and protocol lifecycles are consistent with standard networking architecture.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Mission documentation: `mission-07-networking/README.md`
- Diagnostic reference: `nslookup example.com` resolution records.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Status: Staged and committed locally to `main`.
