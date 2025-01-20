# PortTracer

PortTracer is a powerful, user-friendly, and efficient port scanning tool designed to help cybersecurity professionals and enthusiasts quickly identify open ports on a target system. Developed with rich animations and multithreaded scanning capabilities, PortTracer is the perfect addition to your cybersecurity toolkit.

---

## Features

- **Fast and Efficient Scanning**: Utilizes multithreading to scan ports quickly.
- **Rich Animations**: Includes visually appealing progress bars and banners.
- **User-Friendly Interface**: Simple and intuitive input prompts.
- **Developer Information**: Showcases creator details prominently.
- **Error Handling**: Suppresses non-critical errors for a clean output.

---

## Installation

To install and use PortTracer, follow these steps:

### Prerequisites
- Python 3.6 or later

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/0xaswanth/PortTracer.git
   cd PortTracer
   ```

2. **Install Required Libraries**:
   PortTracer uses the `rich` library for animations and styled outputs. Install it using:
   ```bash
   pip install rich
   ```

3. **Run the Tool**:
   ```bash
   python porttracer.py
   ```

---

## Usage

1. Run the script:
   ```bash
   python porttracer.py
   ```
2. Enter the target IP address when prompted.
3. Specify the starting and ending ports for the scan.
4. View the results, which display all open ports.

Example:
```
Enter target IP: 45.33.32.156
Enter starting port: 1
Enter ending port: 100
Scanning 45.33.32.156 from port 1 to 100...
Open ports: 22, 80
```

---

## Tool Details

### Developer
- **Name**: Aswanth KP
- **GitHub**: [0xaswanth](https://github.com/0xaswanth)

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, make your improvements, and submit a pull request.

---

## Roadmap

Future enhancements include:
- Adding banner grabbing for open ports.
- Saving scan results to a file.
- Building a GUI for an even more user-friendly experience.

---

## Acknowledgments

Special thanks to the open-source community for inspiration and resources that helped make this project possible.

---

## Disclaimer
This tool is intended for educational and ethical purposes only. Unauthorized use of PortTracer on networks or systems you do not own or have permission to test is illegal.

---

Happy Scanning with PortTracer! 🚀

