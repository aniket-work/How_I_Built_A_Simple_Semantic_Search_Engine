# How_I_Built_A_Simple_Semantic_Search_Engine
Build AI-Powered Legal Case Discovery for Attorneys from Scratch

## Introduction

Though we focus on the 'Law Firm' use case, the approach and design discussed in this article can be leveraged for any real-world business use case.

Our Use Case : A law firm handles thousands of cases simultaneously and needs to quickly retrieve relevant case files, previous court rulings, and client correspondence. 
What This Project Provides : Lawyers and paralegals can search using terms that may be vague or not exact, but related to ongoing cases, to prepare for court appearances, client meetings, and legal filings. This app provides all relevant files without needing exact keyword matches and without requiring any LLM setup or external API usage.


## What's This Project About?

This article is about the development of an AI-powered legal case discovery system. It showcases how a fictional law firm is leveraging artificial intelligence to revolutionize their legal research process. The system consists of two main components: a document indexer (employee_goals.py) that processes and indexes legal documents, and a user-friendly search interface (Case_Discovery.py) that allows lawyers to quickly find relevant cases based on their queries. 
The article also covers the creation of a sample dataset (cases_generator.py) to demonstrate the system's capabilities. This comprehensive approach illustrates how AI can be integrated into legal practices to enhance efficiency and accuracy in case research.

## Why Use This Project?

This article is crucial for understanding the growing importance of AI in today's business landscape. It provides a practical example of how AI can be implemented to solve real-world challenges. The fictional law firm's approach demonstrates how businesses can:
Streamline time-consuming processes like legal research
Improve accuracy in finding relevant information
Enhance decision-making by providing quick access to pertinent cases
Increase overall productivity and efficiency

## Architecture
![Design Diagram](docs/design.png)


# Tutorial: Setting Up and Running an AI-Powered Legal Case Discovery Application

## Prerequisites
- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

## Steps

1. **Virtual Environment Setup:**
   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv How_I_Built_A_Simple_Semantic_Search_Engine
     ```
   - Activate the environment:
   
     - Windows:
       ```bash
       How_I_Built_A_Simple_Semantic_Search_Engine\Scripts\activate
       ```
     - Unix/macOS:
       ```bash
       source How_I_Built_A_Simple_Semantic_Search_Engine/bin/activate
       ```

2. **Install Project Dependencies:**

   - Navigate to your project directory and install required packages using `pip`:
   
     ```bash
     pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
     
     cd path/to/your/project
     pip install -r requirements.txt
     ```

3. **Run Build AI-Powered Legal Case Discovery for Attorneys Application**

   Finally, execute the following command to start the "Build AI-Powered Legal Case Discovery for Attorneys" application:

   ```bash 
   # generate synthetic cases of our Law Firm
   python app.py
    ```
   



