# Nigerian Restaurant & Menu Generator 🇳🇬

Welcome to the **Nigerian Restaurant & Menu Generator**! This Streamlit-based application helps you discover traditional Nigerian restaurant names and their special delicacies based on the tribe you select. Whether you're a food enthusiast, a restaurateur, or just curious about Nigerian cuisine, this app is your go-to tool for generating authentic restaurant names and menus.

---

## Features

- **Tribe Selection**: Choose from over 50 Nigerian tribes to generate a restaurant name and menu tailored to their cuisine.
- **AI-Powered Suggestions**: Uses the **Groq API** and **LLaMA3-8b** model to generate creative and culturally relevant restaurant names and menu items.
- **User-Friendly Interface**: Built with **Streamlit**, the app is easy to use and visually appealing.
- **Customizable Outputs**: Get a fancy restaurant name and a list of recommended dishes in seconds.

---

## How It Works

1. **Select a Tribe**: Choose a Nigerian tribe from the dropdown menu in the sidebar.
2. **Generate Restaurant Name**: The app suggests a culturally relevant and fancy restaurant name.
3. **Get Menu Recommendations**: Based on the restaurant name, the app generates a list of traditional dishes for the selected tribe.

---

## Installation

To run this app locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Groq API key (stored in `.env` file)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nigerian-restaurant-generator.git
   cd nigerian-restaurant-generator
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open the app in your browser after running the Streamlit command.
2. Select a Nigerian tribe from the dropdown menu in the sidebar.
3. View the generated restaurant name and recommended menu items on the main page.

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Groq](https://groq.com/) for the powerful LLM API.
- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework.
- Nigerian tribes and their rich culinary heritage for inspiring this project.

---

Feel free to explore the app and enjoy discovering the flavors of Nigeria! 🍛✨
