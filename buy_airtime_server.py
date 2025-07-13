import socket


def start_airtime_server():
    balance = 1000  # Initial balance
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5002))
    server_socket.listen(1)
    print("Buy Airtime Server listening on port 5002...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    amount = float(conn.recv(1024).decode())
    if amount <= balance:
        balance -= amount
        message = f"✅ Bought airtime worth KES {amount}. New balance: KES {balance}"
    else:
        message = "❌ Insufficient balance."

    conn.send(message.encode())
    conn.close()


start_airtime_server()
