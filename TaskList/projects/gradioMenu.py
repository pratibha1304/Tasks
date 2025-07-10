import gradio as gr
import datetime
import requests
import os

# Task 1: Get current time
def get_time():
    return f"🕒 Current time is: {datetime.datetime.now().strftime('%H:%M:%S')}"

# Task 2: Google Search (opens browser)
def google_search(query):
    os.system(f'start https://www.google.com/search?q={query}')
    return f"🔍 Opened browser to search for: {query}"

# Task 3: Get weather data
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        return f"🌦️ Weather: {response.text}"
    except Exception as e:
        return f"❌ Failed to fetch weather: {e}"

# Task 4: Send email (mocked for demo)
def send_email(recipient, subject, body):
    return f"📧 Email sent to {recipient} with subject: {subject} (simulated)"

# UI Panel
with gr.Blocks(title="Automation Panel 🚀") as demo:
    gr.Markdown("# ⚙️ Automation Control Panel")

    with gr.Tab("🕒 Time"):
        time_output = gr.Textbox(label="Current Time")
        gr.Button("Get Time").click(get_time, outputs=time_output)

    with gr.Tab("🔍 Google Search"):
        query_input = gr.Textbox(label="Search Query")
        result = gr.Textbox(label="Status")
        gr.Button("Search").click(google_search, inputs=query_input, outputs=result)

    with gr.Tab("🌦 Weather"):
        city_input = gr.Textbox(label="City Name")
        weather_output = gr.Textbox(label="Weather Info")
        gr.Button("Get Weather").click(get_weather, inputs=city_input, outputs=weather_output)

    with gr.Tab("📧 Email Sender"):
        email_to = gr.Textbox(label="To")
        email_subject = gr.Textbox(label="Subject")
        email_body = gr.Textbox(label="Body", lines=4)
        email_status = gr.Textbox(label="Status")
        gr.Button("Send Email").click(send_email, inputs=[email_to, email_subject, email_body], outputs=email_status)

# Launch app
demo.launch()
