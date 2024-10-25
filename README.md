# DVWA Dictionary Attack Lab

## Objective

The objective of this lab is to demonstrate a dictionary attack on the Damn Vulnerable Web Application (DVWA). DVWA is a PHP/MySQL web application designed to aid security professionals in testing their skills and tools in a legal environment.

## Requirements

To complete this lab, you will need:

- Python programming
- DVWA
- A list of known passwords (as a TXT file)
- Apache and MySQL servers
- A Python IDE (e.g., Spyder)
- Access to either Windows or Linux operating systems

## Preparation Steps

### 1. Install Apache and MySQL Servers

- **Windows:** You can use XAMPP or WAMP.
- **Linux:** Use the package manager to install Apache and MySQL.

### 2. Download DVWA

Download the DVWA source code and place it in the web server directory.

- **Windows:** Place it in `C:\xampp\htdocs\DVWA` for XAMPP.
- **Linux:** Place it in `/var/www/html/DVWA`.

### 3. Install Python IDE

Install Spyder or any other Python IDE of your choice.

### 4. Configure DVWA, Apache, and MySQL

Follow the configuration instructions provided with DVWA to set up the application, including database setup in MySQL.

### 5. Start Apache and MySQL Servers

- **Windows:** Use the XAMPP/WAMP control panel to start the servers.
- **Linux:** Use the terminal commands:
  ```bash
  sudo systemctl start apache2
  sudo systemctl start mysql
