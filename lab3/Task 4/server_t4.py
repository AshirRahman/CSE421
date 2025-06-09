import socket

def calculate_salary(hours_worked):
    if hours_worked <= 40:
        return hours_worked * 200
    else:
        overtime_hours = hours_worked - 40
        return 8000 + (overtime_hours * 300)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected to client at {addr}")

    # Receive data
    data = client_socket.recv(1024).decode()
    hours = int(data)

    # Calculate salary
    salary = calculate_salary(hours)

    # Send back the result
    client_socket.send(str(salary).encode())
    client_socket.close()
