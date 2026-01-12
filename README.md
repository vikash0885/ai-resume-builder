# AI Resume Builder

An intelligent resume builder powered by Gemini AI. Create ATS-friendly resumes, cover letters, and portfolio websites in minutes.

## Features

- **AI-Powered Writing**: Generates professional content for resumes and cover letters.
- **ATS Optimized**: Templates designed to pass Applicant Tracking Systems.
- **Web Portfolio**: Automatically generates a personal portfolio website.
- **Export to PDF**: Easy downloading of your documents.

## Deployment

You can deploy this application for free on Vercel.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvikash0885%2Fai-resume-builder&env=GEMINI_API_KEY,MONGODB_URL)

### Setup Instructions

1.  Click the "Deploy with Vercel" button above.
2.  Sign in with GitHub.
3.  Vercel will ask for Environment Variables (`GEMINI_API_KEY`, `MONGODB_URL`).
4.  Enter your keys and click Deploy.

## Local Development

1.  Clone the repository.
2.  Install dependencies: `pip install -r backend/requirements.txt`
3.  Run the server: `uvicorn backend.app.main:app --reload`
