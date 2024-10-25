# DVWA Dictionary Attack 

## Objective

The objective of this tool is to demonstrate a dictionary attack on the Damn Vulnerable Web Application (DVWA). 
DVWA is a PHP/MySQL web application designed to aid security professionals in testing their skills and tools in a legal environment.

## Requirements

To complete this, you will need:

- Python programming
- DVWA
- A list of known passwords (as a TXT file)
- Apache and MySQL servers
- A Python IDE (e.g., Spyder)
- Access to either Windows or Linux operating systems

## Preparation Steps

1. **Install Apache and MySQL Servers**
   - **Windows:** You can use XAMPP or WAMP.
   - **Linux:** Use the package manager to install Apache and MySQL.

2. **Download DVWA**
   - Download the DVWA source code and place it in the web server directory.
     - **Windows:** Place it in `C:\xampp\htdocs\DVWA` for XAMPP.
     - **Linux:** Place it in `/var/www/html/DVWA`.

3. **Install Python IDE**
   - Install Spyder or any other Python IDE of your choice.

4. **Configure DVWA, Apache, and MySQL**
   - Follow the configuration instructions provided with DVWA to set up the application, including database setup in MySQL.

5. **Start Apache and MySQL Servers**
   - **Windows:** Use the XAMPP/WAMP control panel to start the servers.
   - **Linux:** Use the terminal commands:
     ```bash
     sudo systemctl start apache2
     sudo systemctl start mysql
     ```

6. **Check Access to DVWA**
   - Open your web browser and navigate to `http://localhost/DVWA/login.php` to ensure that DVWA is accessible.

7. **Write Your Dictionary Attack in Python**
   - Using Spyder, write your dictionary attack script. Ensure you include the necessary libraries such as `requests` and `BeautifulSoup`.

8. **Execute Your Attack**
   - Run your script to perform the dictionary attack on the DVWA login page. make sure all files are in teh same directory

## Demonstration Steps

### Windows Instructions

1. **Download and Install XAMPP:**
   - Go to the [XAMPP website](https://www.apachefriends.org/index.html) and download the installer.
   - Follow the installation prompts to install XAMPP.

2. **Download DVWA:**
   - Download the DVWA zip file from the [DVWA GitHub repository](https://github.com/digininja/DVWA).
   - Extract the contents and place the `DVWA` folder in `C:\xampp\htdocs\`.

3. **Open XAMPP Control Panel:**
   - Launch the XAMPP Control Panel.
   - Start the Apache and MySQL services by clicking their respective "Start" buttons.

4. **Access DVWA:**
   - Open a web browser and navigate to `http://localhost/DVWA/setup.php`.
   - Follow the instructions to set up the DVWA database.

5. **Open Spyder:**
   - Launch Spyder or your preferred Python IDE.
   - Write your Python script for the dictionary attack.

6. **Run Your Attack:**
   - Execute your script to perform the dictionary attack on the DVWA login page.
   - Monitor the output for successful login attempts.

### Linux Instructions

1. **Install Apache and MySQL:**
   - Open a terminal and run the following commands:
     ```bash
     sudo apt-get update
     sudo apt-get install apache2 mysql-server
     ```

2. **Download DVWA:**
   - Clone the DVWA repository or download the zip file:
     ```bash
     cd /var/www/html/
     sudo git clone https://github.com/digininja/DVWA.git
     ```
   - Ensure the permissions are set correctly:
     ```bash
     sudo chown -R www-data:www-data DVWA/
     ```

3. **Start Apache and MySQL:**
   - Run the following commands to start the servers:
     ```bash
     sudo systemctl start apache2
     sudo systemctl start mysql
     ```

4. **Access DVWA:**
   - Open a web browser and navigate to `http://localhost/DVWA/setup.php`.
   - Follow the instructions to set up the DVWA database.

5. **Open Spyder:**
   - Launch Spyder or any other Python IDE.
   - Write your Python script for the dictionary attack.

6. **Run Your Attack:**
   - Execute your script to perform the dictionary attack on the DVWA login page.
   - Monitor the output for successful login attempts.

## Conclusion

Once you have completed the above steps, you will successfully demonstrate a dictionary attack on the DVWA, reinforcing your understanding of web application security testing.
This tool has been developed by the inspiration from https://github.com/Antu7 -- Thank you. 
