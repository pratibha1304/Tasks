import os
import sys

def search_google():
    from googlesearch import search
    query = input("Enter search query: ")
    print("\nTop 5 search results:")
    for url in search(query, num_results=5):
        print(url)

def send_email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = input("Your Gmail address: ")
    app_password = input("App password (not regular password): ")
    receiver_email = input("Receiver email: ")
    subject = input("Email subject: ")
    body = input("Message body: ")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

def download_website():
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    url = input("Enter website URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    filename = "downloaded_site.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"Saved HTML to {filename}")

def create_digital_image():
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new('RGB', (400, 200), color='lightblue')
    d = ImageDraw.Draw(img)
    text = input("Enter text to write on image: ")
    d.text((100, 90), text, fill=(0, 0, 0))
    img.save('custom_image.png')
    print("Image saved as custom_image.png")

def swap_faces():
    print("This requires face1.jpg, face2.jpg and shape_predictor_68_face_landmarks.dat")
    print("Please run face_swap.py separately.")
    os.system("python3 face_swap.py")

def post_to_linkedin():
    print("LinkedIn API requires OAuth access token and developer setup.")
    print("Please use the LinkedIn API code provided in earlier steps.")

def post_to_twitter():
    print("Twitter API requires authentication keys.")
    print("Please run your tweepy-based script with keys set up.")

def post_to_facebook():
    print("Facebook Graph API requires a page access token.")
    print("Please use the earlier code or setup before calling this.")

def post_to_instagram():
    print("Instagram API requires a business account and Facebook Graph access.")
    print("Use the code shown earlier in this session to automate posting.")

def show_menu():
    print("\n" + "="*40)
    print("        🔧 PYTHON TASK CENTER")
    print("="*40)
    print("1. Search Google")
    print("2. Send Email")
    print("3. Download Website Data")
    print("4. Create Custom Digital Image")
    print("5. Swap Faces in Two Images")
    print("6. Post on LinkedIn")
    print("7. Post on Twitter (X)")
    print("8. Post on Facebook")
    print("9. Post on Instagram")
    print("0. Exit")
    print("="*40)

while True:
    show_menu()
    choice = input("Choose an option (0-9): ")

    match choice:
        case "1": search_google()
        case "2": send_email()
        case "3": download_website()
        case "4": create_digital_image()
        case "5": swap_faces()
        case "6": post_to_linkedin()
        case "7": post_to_twitter()
        case "8": post_to_facebook()
        case "9": post_to_instagram()
        case "0":
            print("Goodbye! 👋")
            sys.exit()
        case _:
            print("Invalid choice. Please enter a number from 0–9.")
