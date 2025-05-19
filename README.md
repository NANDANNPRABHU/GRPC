# GRPC

A Python-based gRPC implementation demonstrating client-server communication using Protocol Buffers.

## Overview

This project showcases a basic gRPC setup with Python, illustrating how to define services and exchange messages between a client and a server.

## Features

- **gRPC Server**: Handles incoming RPC calls and processes client requests.
- **gRPC Client**: Sends requests to the server and receives responses.
- **Protocol Buffers**: Defines the structure of the messages exchanged.
- **Docker Support**: Includes configurations for containerizing the application.

## Project Structure

```
GRPC/
├── .devcontainer/           # Development container configurations
├── server_client/           # Contains server and client implementations
│   ├── server.py            # gRPC server implementation
│   ├── client.py            # gRPC client implementation
│   └── ...                  # Additional related files
├── get_node_info.py         # Script to retrieve node information
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Prerequisites

- Python 3.7 or higher
- `pip` package manager

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NANDANNPRABHU/GRPC.git
   cd GRPC
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the gRPC server**:

   Navigate to the `server_client` directory and run:

   ```bash
   python server.py
   ```

   The server will start and listen for incoming RPC calls.

2. **Run the gRPC client**:

   In a new terminal window, navigate to the `server_client` directory and execute:

   ```bash
   python client.py
   ```

   The client will send a request to the server and display the response.

## Docker Support

To run the application using Docker:

1. **Build the Docker image**:

   ```bash
   docker build -t grpc-app .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 50051:50051 grpc-app
   ```

   This will start the server inside a Docker container, exposing port 50051.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
