🎭 Random Joke Generator (Jocky)
Welcome to Jocky — a fun web app that fetches and displays a random joke every time you visit!
Built using Flask (Python backend), Bootstrap 5 (for styling), and a live Joke API, Jocky brings humor directly to your browser. 🌟

📸 Preview
![op1](https://github.com/user-attachments/assets/0122f1f5-2946-4110-b335-47d7d447338e)

🚀 Features
Fetches a new random joke (setup and punchline) from an API.

Stylish, animated, and mobile-responsive design with Bootstrap 5.

Background themed on Joker 🃏 to match the humor vibes!

Footer credits with ❤️ made by Shreyas Shridhar Kulkarni.

Error-handling if the API fails to fetch jokes.

🛠 Tech Stack
Backend: Python Flask

Frontend: HTML5, CSS3, Bootstrap 5

External API: Official Joke API

📂 Project Structure
plaintext

├── app.py           # Flask application
├── templates/
│   └── index.html   # Frontend HTML template
└── README.md        # Project description
🧩 How To Run Locally
Clone the repository


git clone https://github.com/yourusername/jocky-flask-app.git
cd jocky-flask-app
Create a virtual environment (optional but recommended)


python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
Install required packages


pip install flask requests
Run the application


python app.py
Open in your browser

Go to http://127.0.0.1:5000/ to see the magic!

📜 Requirements
Python 3.8+

Flask

Requests

You can install them by:


pip install -r requirements.txt
(You can create a requirements.txt with these two lines:)

nginx
Flask
requests
💡 Future Improvements
Add a "Get Another Joke" button to refresh jokes without reloading the page.

Add dark/light mode toggle.

Display multiple jokes in a carousel.

Allow users to submit their own jokes!

🎨 Special Thanks
Official Joke API

Bootstrap 5

🧑‍💻 Developed by
Shreyas Shridhar Kulkarni
Made with ❤️ in 2025!
