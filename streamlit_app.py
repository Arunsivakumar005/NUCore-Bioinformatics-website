import streamlit as st
import streamlit.components.v1 as components

# Function to load and inject CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


components.html(
    """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
            content="width=device-width,
            initial-scale=1.0">
        <script src="https://unpkg.com/htmx.org@1.9.6"></script>
        <title>NUCore IGMC Bioinformatics pipelines</title>
    </head>

    <body style="background-color: white;">
	    <header style="background-color: #4c8b41; text-align: center; padding: 20px;">
             <h1>NUCore Bioinformatics pipelines</h1>
        </header>
        <h2>Submit Your Task</h2>
        <form hx-post="/submit" hx-target="#response" hx-swap="outerHTML">
            <label>Username:</label>
            <input type="text" name="username" required>

            <br><br>
            <label>Task Type:</label>
            <select name="task_type" required>
            <option value="" disabled selected>Select a task type</option>
            <option value="task1">Bulk RNAseq</option>
            <option value="task2">Methylseq</option>
            </select>

            <br><br>
            <label>Path to BCL/Fastq files in quest:</label>
            <input type="text" name="Enter path to BCL/Fastq files" required>

            <br><br>
            <label>Output directory:</label>
            <input type="text" name="Enter path to save output" required>
            <br><br>
            <button type="submit">Submit</button>
        </form>
        <div id="response"></div>
    </body>

    </html>
    """,	
    height=600,
)
