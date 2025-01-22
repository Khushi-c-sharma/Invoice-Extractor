# Multi-Language Invoice Extractor

## Overview
The Multi-Language Invoice Extractor is a Streamlit application designed to extract and analyze data from invoices in various languages. The app leverages Google's Gemini 1.5 Flash model to process invoice images and respond to user prompts about the uploaded invoices.

## Features
- **Upload Invoice Images**: Supports `.jpg`, `.jpeg`, and `.png` formats.
- **Multi-Language Support**: Handles invoices in different languages.
- **AI-Powered Analysis**: Uses Google's Generative AI capabilities to understand and describe invoice content.
- **Streamlit Interface**: Intuitive and interactive user interface for easy usage.

## Prerequisites
Ensure the following are installed and set up on your system:
- Python 3.8 or higher
- Required Python libraries (listed in the Installation section)
- A valid Google Generative AI API key

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with the following content:
   ```plaintext
   GOOGLE_API_KEY=your_google_api_key
   ```
   Replace `your_google_api_key` with your actual API key from Google.

## Usage
1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Open the application in your browser at `http://localhost:8501`.
3. Upload an invoice image in `.jpg`, `.jpeg`, or `.png` format.
4. Provide a prompt describing your query about the invoice.
5. Click the **Describe the invoice** button to get the AI-generated response.

## File Structure
```
.
├── app.py                 # Main application code
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md              # Documentation
```

## Key Functions
### `get_gemini_response(input, image, prompt)`
Generates a response from the Gemini model based on the provided input, image, and prompt.

- **Parameters**:
  - `input` (str): Describes the behavior of the model.
  - `image` (list): Contains details of the uploaded image in base64 format.
  - `prompt` (str): The specific question or task.

- **Returns**: The text response from the model.

### `input_image_details(uploaded_file)`
Processes the uploaded file and encodes it into a format suitable for the Gemini model.

- **Parameters**:
  - `uploaded_file`: The image file uploaded by the user.

- **Returns**: A list containing the MIME type and base64-encoded image data.

## Error Handling
The application handles errors gracefully:
- Displays an error message if no file is uploaded.
- Provides informative feedback in case of other exceptions.

## Limitations
- Requires a valid Google API key.
- Limited to `.jpg`, `.jpeg`, and `.png` file formats.

## Live Demo
This application is deployed on Render. You can access it here:
[Multi-Language Invoice Extractor](https://invoice-extractor-2wwl.onrender.com)

## Dependencies
- `streamlit`
- `python-dotenv`
- `google-generativeai`
- `Pillow`

## License
This project is licensed under the [MIT License](LICENSE).


