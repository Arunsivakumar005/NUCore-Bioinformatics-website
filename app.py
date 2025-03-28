from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def form():
    print("Form page accessed")
    return render_template_string("""
        <header>
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
    """)

@app.route('/submit', methods=['POST'])
def submit():
    # Get the input values from the form
    username = request.form['username']
    task_type = request.form['task_type']
    path_bcl = request.form['Enter path to BCL/Fastq files']
    output_dir = request.form['Enter path to save output']
    
    # Debug print
    print(f"Received form data: Username={username}, Task Type={task_type}, Path to BCL={path_bcl}, Output Dir={output_dir}")
    
    # Create the Nextflow command dynamically
    nextflow_command = f"""
    nextflow run nf-core/rnaseq \\
    --input {path_bcl} \\
    --outdir {output_dir} \\
    --genome GRCh38 \\
    -profile singularity
    """
    
    # Execute the Nextflow command
    result = subprocess.run(nextflow_command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Return the success message
        return f"Job submitted successfully! <pre>{result.stdout}</pre>"
    else:
        # Return the error message
        return f"Error executing Nextflow: <pre>{result.stderr}</pre>"

if __name__ == '__main__':
    app.run(debug=True)

