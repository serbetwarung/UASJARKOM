UAS – Komunikasi & Jaringan Komputer

Magister Terapan – Semester Gasal 2025/2026
Politeknik Elektronika Negeri Surabaya (PENS)
Dosen: Ferry Astika Saputra

Repository ini berisi implementasi UAS untuk mata kuliah Komunikasi & Jaringan Komputer, berdasarkan Socket Programming Assignment dari buku:

Computer Networking: A Top-Down Approach, 9th Edition — Kurose & Ross.

Tugas terdiri dari:

Assignment 1

Web Server single-client

Web Server multi-client (concurrent/threaded)

Assignment 2

UDP Ping (client and server)

Perhitungan RTT & packet loss

📁 Struktur Direktori
UASJARKOM/
│
├── Assignment1/
│   ├── index.html
│   ├── webserver_single.py
│   └── webserver_multi.py
│
├── Assignment2/
│   ├── udp_client.py
│   └── udp_server.py
│
└── README.md

🚀 Assignment 1 — Web Server
1A — Single Client Web Server

File: Assignment1/webserver_single.py

Web server sederhana yang menangani satu request setiap kali.

▶️ Cara menjalankan:
cd Assignment1
python webserver_single.py


Lalu akses di browser:

http://localhost:8080/index.html

1B — Multi Client Web Server (Concurrent)

File: Assignment1/webserver_multi.py
Menggunakan multithreading untuk melayani beberapa client sekaligus.

▶️ Cara menjalankan:
python webserver_multi.py


Test dengan membuka beberapa tab ke:

http://localhost:8080/index.html

📡 Assignment 2 — UDP Ping

Assignment ini mensimulasikan komunikasi UDP:

Server menerima pesan ping dan secara acak membuang sebagian paket.

Client mengirim ping sebanyak 10 kali dan mengukur RTT per paket.

▶️ Menjalankan UDP Server
cd Assignment2
python udp_server.py


Server akan listen pada port 12000.

▶️ Menjalankan UDP Client

Di terminal baru:

python udp_client.py


Client akan menampilkan log:

Reply diterima + RTT

Timeout (packet loss)

📊 Contoh Hasil Output UDP Ping
Reply: PING 1 | RTT = 0.000000 s
Reply: PING 2 | RTT = 0.000000 s
Reply: PING 3 | RTT = 0.000929 s
Request timed out
Request timed out
Reply: PING 7 | RTT = 0.000000 s
Reply: PING 8 | RTT = 0.000000 s
Request timed out
Reply: PING 10 | RTT = 0.000000 s


Dari hasil tersebut:

7 ping sukses

3 ping timeout

Packet loss = sekitar 30%
