import socket


def start_send_money_server():
    balance = 1000  # Initial balance
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(1)
    print("Send Money Server listening on port 5001...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    amount = float(conn.recv(1024).decode())
    if amount <= balance:
        balance -= amount
        message = f"✅ Sent KES {amount}. New balance: KES {balance}"
    else:
        message = "❌ Insufficient balance."

    conn.send(message.encode())
    conn.close()


start_send_money_server()
