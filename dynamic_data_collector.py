# We need pandas to arrange our collected data into clean tables
import pandas as pd
# This helps Python connect and talk directly to the mail server
import smtplib
# We use this to grab only the file name from any folder path
import os
# These packages help us build the email and format the attachment correctly
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
# This library helps us design and generate a clean PDF document
from fpdf import FPDF

# Email sender settings
sender_email = "samsonkolawumi@gmail.com"
sender_password = "YOUR_APP_PASSWORD_HERE"
smtp_server = "smtp.gmail.com"
smtp_port = 465 # Port 465 is explicitly used for secure SSL to bypass network blocks


# This function collects the student details from the terminal
def collect_data():
    # .title() is a built-in string method that changes the first letter of each word to uppercase
    print("\nplease enter your information".title())
    

    # input() is a built-in function that pauses the program to collect keyboard text typed by the user.
    data = {
        "Full Name": input("Full Name: "),
        "Address": input("Address: "),
        "Cohort": input("Cohort: "), 
        "Phone Number": input("Phone Number: "),
        "Email": input("Email: "),
        "Passcode": input("Passcode: "),
        "Course": input("Course: ")        
    }
    return data # return stops the function execution and passes the collected data dictionary out


# This function saves the student data as a CSV file
def save_to_csv(data, filename="user_data.csv"):
    # pd.DataFrame() converts our python dictionary into a structured row-and-column table
    df = pd.DataFrame([data])
    # .to_csv() is a pandas method that writes the table directly into a physical CSV file on disk
    df.to_csv(filename, index=False)
    # f"..." is an f-string used to dynamically insert variable values directly inside text
    print(f"Data saved locally as {filename}")
    return filename # Sends the written file path back to the main program flow


# This function saves the student data as an Excel file
def save_to_excel(data, filename="user_data.xlsx"):
    df = pd.DataFrame([data])
    # .to_excel() converts and writes our pandas table directly into a Microsoft Excel workbook
    df.to_excel(filename, index=False)
    print(f"Data saved locally as {filename}")
    return filename


# This function saves the student data inside a PDF document
def save_to_pdf(data, filename="user_data.pdf"):
    pdf = FPDF() # Initializes a fresh FPDF class object to start designing the document
    pdf.add_page() # Opens a blank page for drawing
    
    # Helvetica works on all systems without font missing errors
    pdf.set_font("Helvetica", size = 12)

    # .cell() draws a rectangle box to hold and position text cleanly on the PDF canvas
    pdf.cell(200, 10, txt="User Information registration", ln=True, align="C")
    pdf.ln(10) # .ln() is a line break method that acts like pressing 'Enter' to create space

    # .items() is a dictionary method that unpacks the dictionary into key-value pairs for the loop
    # for key, value in ... is a loop that runs repeatedly until it extracts all information from the dictionary
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln = True)

    pdf.output(filename) # .output() writes all designed visual elements into a real PDF file on the disk
    print(f"Data Saved locally as {filename}")
    return filename


# This function handles the attachment packaging and email dispatch
def send_email (recipent_email, file_path):
    print(f"Preparing to send email to {recipent_email} with attachment {file_path}")

    # Set up the email container for holding text and files together
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipent_email
    msg['Subject'] = "Your registration Data"

    # Define the body message
    body = "Hello,\n\nPlease find your requested registration data attached to this email.\n\nBest regards,\nSamson O.\nRevenue Systems Architect"
    # msg.attach() binds the plain text message to the main email container
    msg.attach(MIMEText(body, 'plain'))

    # We use try-except to prevent the script from crashing if the file is missing or locked
    try:
        # open() is a built-in function that opens files. "rb" means read-binary mode so the file content does not scatter.
        # with open(...) as ... closes the file automatically once reading is finished to prevent memory leaks.
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream') # Creates a raw container for carrying attachments
            part.set_payload(attachment.read()) # .read() extracts the raw binary content of the file
            # Convert binary data to base64 text so the email server can carry it
            encoders.encode_base64(part)

            # os.path.basename() extracts only the raw file name (e.g. user_data.csv) from a long folder path
            # .add_header() configures the meta-tags of the file so the recipient's mail client knows the file name
            part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
            
            # Attach the file to the main email message
            msg.attach(part)
    except Exception as e: # Catch any error that happens inside the try block
        print (f"Failed to attach file: {e}")
        return # Exit the function early because we cannot send an empty email
    

    # We use try-except here to catch any internet or SMTP network errors
    try:
        # Connect to Google's SMTP server using SMTP_SSL for direct port 465 encryption
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # .login() authenticates your sender email using your 16-character secure Google App Password
        server.login(sender_email, sender_password)
        # .as_string() compiles the whole structured email object (from, to, body, attachment) into a plain text message
        text = msg.as_string()
        # .sendmail() executes the dispatch of the formatted text stream over the established socket connection
        server.sendmail(sender_email, recipent_email, text)
        # .quit() closes the SMTP server connection cleanly to free up network ports
        server.quit() 
        print(f"Email sent successfully to {recipent_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


# The main engine that coordinates everything step-by-step
def main():
    # 1. Collect student details (Successfully collects all 7 fields)
    user_data = collect_data()

    # 2. Show the export menus
    print("\n--- Export Options ---")
    print("Available formats: 'pdf', 'csv', 'spreadsheet' (or 'excel')")

    file_path = ""
    
    # 3. Validation loop to make sure the user inputs the correct option
    # while True creates an infinite loop that runs until we manually stop it with a 'break'
    while True:
        # .strip() removes accidental space bar presses, and .lower() converts all text to lowercase
        choice = input("Type the format to convert to: ").strip().lower()
        
        # We run the specific function based on what the user types
        if choice == 'pdf':
            file_path = save_to_pdf(user_data)
            break # break is a control flow statement that exits the loop immediately after saving the file
        elif choice == 'csv':
            file_path = save_to_csv(user_data)
            break # Exits the loop after successful CSV generation
        elif choice in ['spreadsheet', 'excel']: # in checks if the user's input matches any item in the list
            file_path = save_to_excel(user_data)
            break # Exits the loop after successful Excel generation
        else:
            # Keeps asking if the user types rubbish
            print("Invalid choice. Please select 'pdf', 'csv', 'spreadsheet' or 'excel', and try again.")

    # 4. Extract email and send the attached document
    # .get() is a dictionary method that safely pulls the value of "Email" without crashing if the key doesn't exist
    user_email = user_data.get("Email")
    # if checks if the variable contains a valid string (true) or if it is empty (false)
    if user_email:
            send_email(user_email, file_path)
    else:
            print("No email address provided. Cannot Send email.")
        
# This standard python syntax ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main() # Triggers the orchestrator function to start running the entire program flow
