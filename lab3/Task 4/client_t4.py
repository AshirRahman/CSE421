import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Input hours
hours_worked = int(input("Enter number of hours worked: "))
client_socket.send(str(hours_worked).encode())

# Receive salary
salary = client_socket.recv(1024).decode()
print(f"Calculated salary: Tk {salary}")

client_socket.close()
