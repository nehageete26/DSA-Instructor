# 🧠 DSA Instructor
AI-Powered Data Structures & Algorithms Learning Assistant

DSA Instructor is an interactive AI-powered web application built using Streamlit and Google Gemini (2.5 Flash) that acts as a personal mentor for learning Data Structures & Algorithms.

It provides structured explanations, Java implementations, complexity analysis, and curated learning resources — all inside a modern chat interface.

## 🚀 Overview

Learning DSA can feel overwhelming due to:

Complex theoretical explanations

Lack of structured guidance

Scattered resources

Difficulty understanding time & space complexity

DSA Instructor solves this problem by combining:

Structured AI explanations

Step-by-step problem solving

Clean Java implementations

Curated blog & YouTube recommendations

A modern, distraction-free interface

## ✨ Key Features
📖 1. Smart Concept Explanation

When a user asks about a DSA topic, the system provides:

Clear beginner-friendly explanation

Real-world examples

Time complexity analysis

Space complexity analysis

Clean Java implementation with comments

## 🧩 2. Problem Solving Mode

For coding problems, the app provides:

Step-by-step solution approach

Optimized Java code

Time complexity breakdown

Space complexity breakdown

## 📚 3. Curated Learning Resources

After explanation, the system automatically fetches:

Blogs

GeeksforGeeks

Baeldung

JavaPoint

YouTube Tutorials

Abdul Bari

William Fiset

NeetCode

Only real, working URLs are returned.

## 🎨 4. Modern UI Design

Custom dark theme

Styled hero section

Chat-style interface

Section-based response cards

Resource chips with hover effects

Clean typography

## 🔒 5. Strict DSA Mode

The assistant:

Only answers DSA-related questions

Rejects unrelated topics

Prevents misuse

Keeps focus on learning

## 🛠 Tech Stack
Layer	Technology
Frontend	Streamlit
AI Model	Google Gemini 2.5 Flash
Backend	Python
Styling	Custom CSS
State Management	Streamlit Session State

## 🏗 System Architecture

User Input
↓
Streamlit Chat Interface
↓
Gemini API Call (Main Explanation)
↓
Structured Response Rendering
↓
Second Gemini Call (Resource Extraction)
↓
Formatted Blogs & YouTube Links

## 📂 Project Structure
dsa-instructor/
│
├── app.py               # Main Streamlit application
├── README.md            # Documentation

## 📦 requirements.txt
streamlit
google-generativeai
🔑 API Key Setup (IMPORTANT)

⚠️ Never hardcode your API key in public repositories.

Step 1: Get Gemini API Key

Visit:
https://aistudio.google.com/

Step 2: Set Environment Variable
Windows (PowerShell)
setx GEMINI_API_KEY "your_api_key_here"
Mac/Linux
export GEMINI_API_KEY="your_api_key_here"
Step 3: Update app.py

Replace:

API_KEY = "your_api_key"

With:

import os
API_KEY = os.getenv("GEMINI_API_KEY")
▶️ Running the Application
streamlit run app.py

The app will open automatically in your browser.

## 💬 Example Questions

What is Binary Search Tree?

Explain Merge Sort with Java code

Solve Two Sum problem

What is Dijkstra’s Algorithm?

Implement LRU Cache in Java

Explain Time Complexity of QuickSort

## 🧠 Learning Benefits

This project helps users:

Understand DSA fundamentals

Prepare for coding interviews

Improve Java implementation skills

Learn complexity analysis

Discover trusted learning resources

## 🔐 Security Best Practices

Add this to .gitignore:

venv/
__pycache__/
.env
*.pyc

Never commit:

API keys

Environment files

Credentials

## 📈 Future Enhancements

🔐 User Authentication

🗄 Database for chat storage

📊 Progress tracking dashboard

📝 Quiz & assessment system

📈 Performance analytics

🌐 Streamlit Cloud deployment

🎯 Difficulty level selector

💾 Bookmark feature

🔄 Multi-language code support

## 🎯 Ideal Users

Computer Science students

DSA beginners

Java learners

Placement preparation students

Interview aspirants

## 💼 Resume Description

Built an AI-powered DSA Instructor web application using Streamlit and Google Gemini API that provides structured explanations, Java implementations, complexity analysis, and curated learning resources through a modern chat interface.

## ⭐ Support

If you found this project useful:

Star the repository

Share it with friends

Contribute improvements

## 👨‍💻 Author
Neha Geete 

Built with passion for AI, learning, and problem-solving.
