# 🔐 Password Generator

This is a simple password generator web application built with [Streamlit](https://streamlit.io/). Users can generate strong passwords with customizable options such as length, uppercase letters, and symbols.

## 🚀 Features
- Generate secure passwords
- Customize password length (4 to 50 characters)
- Option to include uppercase letters
- Option to include special symbols
- Clear password with a button

## 📌 Installation
To install the required dependencies, run:
```sh
pip install -r requirements.txt
```

## 🎮 Usage
Run the application with the following command:
```sh
streamlit run app.py
```

## 📜 Requirements
The necessary libraries are listed in `requirements.txt`. Ensure you have Python installed before proceeding.

## 🌐 Live Demo
The application is publicly available at:  
🔗 [Password Generator](https://generare-password.streamlit.app)

## 🛡️ Security Considerations
- The generated password is stored in `st.session_state` and will persist until cleared.
- It is recommended to clear the password after copying it to prevent exposure.
- HTTPS ensures secure communication when deployed online.

## 📄 License
This project is licensed under the MIT License.

