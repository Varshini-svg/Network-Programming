# safe_stress_test.py
import threading
import socket
import time

target = '127.0.0.1'  # localhost (safe)
port = 8080           # test server port

def attack():
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            s.close()
    except Exception as e:
        print("Error:", e)

# Run multiple threads
for i in range(20):  # smaller thread count for local testing
    thread = threading.Thread(target=attack)
    thread.start()

print("Started stress test on local server...")
time.sleep(10)  # run for 10s
print("Test complete.")
