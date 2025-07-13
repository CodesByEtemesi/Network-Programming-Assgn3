import socket


def send_money():
    amount = input("Enter amount to send: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5001))
        s.send(amount.encode())
        result = s.recv(1024).decode()
        print("Server:", result)


def buy_airtime():
    amount = input("Enter airtime amount to buy: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5002))
        s.send(amount.encode())
        result = s.recv(1024).decode()
        print("Server:", result)


# Client Menu
print("====== M-PESA SIMULATOR ======")
print("1. Send Money")
print("2. Buy Airtime")
choice = input("Select option: ")

if choice == '1':
    send_money()
elif choice == '2':
    buy_airtime()
else:
    print("Invalid choice.")
