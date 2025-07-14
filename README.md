# Human-Like Reply Generator

This application generates human-like replies to social media posts using OpenAI's GPT-4 model. It analyzes the tone and intent of the original post to create contextually appropriate responses.

## Features

- Generates replies based on post tone and intent analysis
- Supports multiple social media platforms
- Web interface for easy testing
- API endpoint for integration with other applications
- MongoDB storage for reply history

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file with your API keys (use the provided `.env.example` as a template):
   ```
   OPENAI_API_KEY=your_openai_api_key
   MONGO_DB_URL=your_mongodb_connection_string
   ```
   
   > **IMPORTANT**: Never commit your `.env` file to version control. The `.gitignore` file is configured to exclude it.

## Usage

### Running the Application

```
python app.py
```

This will start the Flask server at http://127.0.0.1:5000/

### Web Interface

Open your browser and navigate to http://127.0.0.1:5000/ to use the web interface.

### API Usage

To generate a reply programmatically, send a POST request to the `/reply` endpoint:

```
POST /reply
Content-Type: application/json

{
  "platform": "twitter",
  "post_text": "Just launched my new website!"
}
```

Response:

```json
{
  "reply": "Congratulations on the launch! 🎉 What features are you most excited about on your new site? Would love to check it out!",
  "stored_in_database": true
}
```

## Project Structure

- `app.py`: Main Flask application
- `utils/reply.py`: OpenAI API integration for generating replies
- `utils/db.py`: MongoDB integration for storing replies
- `templates/index.html`: Web interface
- `.env`: Environment variables (API keys)

## Error Handling

The application includes comprehensive error handling for:
- Missing or invalid input data
- OpenAI API errors
- MongoDB connection issues

## Security Best Practices

### Protecting API Keys and Sensitive Data

1. **Use Environment Variables**: Store all sensitive data (API keys, database credentials) in the `.env` file.

2. **Never Commit Secrets**: The `.gitignore` file is set up to exclude the `.env` file from version control.

3. **Use .env.example**: A template file `.env.example` is provided to show the required environment variables without revealing actual values.

4. **Check Before Committing**: Always review your changes with `git diff --staged` before committing to ensure no secrets are accidentally included.

5. **Use Environment-Specific Configuration**: For different environments (development, testing, production), use different `.env` files that are not committed to the repository.

6. **Consider Using Secret Management Tools**: For production deployments, consider using secret management services provided by your hosting platform.

### What to Do If You Accidentally Commit Sensitive Data

1. **Rotate Keys Immediately**: If you accidentally push API keys or credentials to a public repository, consider them compromised and rotate them immediately.

2. **Remove from Git History**: Use tools like `git filter-branch` or BFG Repo-Cleaner to remove sensitive data from your Git history.

3. **Contact Support**: If you've pushed an OpenAI API key to a public repository, contact OpenAI support to invalidate the key.

## License

MIT