# AI Resume Builder

An intelligent resume builder powered by Gemini AI. Create ATS-friendly resumes, cover letters, and portfolio websites in minutes.

## Features

- **AI-Powered Writing**: Generates professional content for resumes and cover letters.
- **ATS Optimized**: Templates designed to pass Applicant Tracking Systems.
- **Web Portfolio**: Automatically generates a personal portfolio website.
- **Export to PDF**: Easy downloading of your documents.

## Deployment

You can deploy this application for free on Render.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/vikash0885/ai-resume-builder)

### Setup Instructions

1.  Click the "Deploy to Render" button above.
2.  Sign in with your GitHub account.
3.  In the deployment setup, you will be asked for Environment Variables.
4.  Enter your secrets:
    *   `GEMINI_API_KEY`: Your Google Gemini API Key.
    *   `MONGODB_URL`: Your MongoDB connection string.

## Local Development

1.  Clone the repository.
2.  Install dependencies: `pip install -r backend/requirements.txt`
3.  Run the server: `uvicorn backend.app.main:app --reload`
