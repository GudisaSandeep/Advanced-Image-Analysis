# Gemini Pro Vision Image Analysis Project

## Overview

The **Gemini Pro Vision Image Analysis Project** is a Streamlit web application that leverages Google AI's Generative Model to analyze images and generate text based on user prompts. The application features a modern, responsive front-end built with Bootstrap, providing an engaging and user-friendly experience.

## Features

- **Image Upload**: Users can upload JPEG or PNG images.
- **Prompt Input**: Users can enter a text prompt to guide the content generation.
- **Content Generation**: The app generates text based on the uploaded image and prompt using Google AI's Generative Model.
- **Responsive Design**: The application is built with Bootstrap for a responsive and attractive UI.

## Technologies Used

- **Backend**: Streamlit
- **Frontend**: Bootstrap
- **Image Processing**: Pillow
- **AI Integration**: Google Generative AI
- **Environment Management**: Python-dotenv

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/GudisaSandeep/Advanced-Image-Analysis
   cd Advanced-Image-Analysis



## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**

   ```sh
    git clone https://github.com/GudisaSandeep/Advanced-Image-Analysis
   ```

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Google API key:

   ```plaintext
   API_KEY=your_google_api_key
   ```

5. **Run the Flask Application**

   ```sh
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Open the Application**: Navigate to `http://127.0.0.1:5000/` in your web browser.
2. **Upload an Image**: Use the file uploader to select an image file (JPEG or PNG).
3. **Enter a Prompt**: Provide a text prompt in the input field.
4. **Generate Content**: Click the "Generate!" button to process the image and prompt. The generated text will be displayed below the form.

## Development

To contribute to this project:

1. **Fork the Repository** on GitHub.
2. **Clone Your Fork** locally.
3. **Create a New Branch** for your feature or bug fix:

   ```sh
   git checkout -b feature/your-feature
   ```

4. **Make Changes** and commit them:

   ```sh
   git add .
   git commit -m "Add your feature or fix"
   ```

5. **Push to Your Fork** and create a pull request:

   ```sh
   git push origin feature/your-feature
   ```

   Go to the original repository on GitHub and create a pull request from your fork.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Streamlit**: The web framework used for building the application.
- **Bootstrap**: Provides the responsive design.
- **Google AI**: For the generative model.
- **Pillow**: For image processing.

## Contact

For any questions or feedback, please contact [gudisasandeep141312@gmial.com](mailto:gudisasandeep141312@gmail.com).

## Future Enhancements

- **Extended Image Formats**: Support for additional image formats.
- **Advanced AI Features**: Integration with more advanced AI models for enhanced content generation.
- **User Authentication**: Add user login and management features.



