import webbrowser

crush_name = input("Enter your crush's name: ")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Special Message</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }}
        .message-box {{
            text-align: center;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .message-box h1 {{
            color: #ff6f61;
        }}
        .message-box p {{
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="message-box">
        <h1>Hey {crush_name}!</h1>
        <p>Just wanted to let you know that you're amazing and I've been thinking about you.</p>
        <p>You make the world a better place just by being in it.</p>
        <p>Hope you have a fantastic day!</p>
    </div>
</body>
</html>
"""

# Save the HTML content to a file
with open("special_message.html", "w") as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open("special_message.html")
