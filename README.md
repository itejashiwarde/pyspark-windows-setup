# Complete PySpark Installation Guide on Windows 10/11

Beginner-friendly installation guide | Python 3.11 | Java 17 | PySpark 4.0.2 | Git | VS Code

This guide will help you install and configure PySpark on Windows from scratch. Follow each step in order. No previous programming experience is required.

## 1. Software requirements

| Software | Version |
| --- | --- |
| Python | 3.11.x (guide tested with 3.11.9) |
| Java JDK | 17 |
| PySpark | 4.0.2 |
| Py4J | 0.10.9.9 (installed automatically) |
| Git | Latest |
| VS Code | Latest |

## 2. Install Python 3.11

Step 1: Open CMD or PowerShell.

Step 2: Run:

```cmd
winget install -e --id Python.Python.3.11
```

If prompted to accept agreements, type `Y` and press Enter.

Step 3: Close and reopen your terminal.

Step 4: Verify:

```cmd
py -3.11 --version
```

Expected output:

```text
Python 3.11.9
```

> Note: Winget installs the latest available Python 3.11 release, which may be newer than 3.11.9. Any 3.11.x works for this guide. For exactly 3.11.9, download it from the [official Python 3.11.9 page](https://www.python.org/downloads/release/python-3119/).

Step 5: If `python` is not recognized, use `py -3.11` instead (as shown above). To fix the `python` command permanently, add Python to your PATH and disable the Windows Python App Execution Aliases (Settings → Apps → Advanced app settings → App execution aliases).

## 3. Install Java JDK 17

Step 1: Run:

```cmd
winget install -e --id EclipseAdoptium.Temurin.17.JDK
```

Step 2: Reopen CMD.

Step 3: Verify:

```cmd
java -version
```

Expected: Java 17.

Step 4: Find Java:

```cmd
where java
```

Step 5: Configure `JAVA_HOME`:

- Search for Environment Variables in Windows.
- Open Edit the system environment variables, then click Environment Variables.
- Under System variables, click New.
- Set the variable name to `JAVA_HOME`.
- Set the value to your actual JDK installation folder.

Example:

```text
C:\Program Files\Eclipse Adoptium\jdk-17.0.x.x-hotspot
```

Do not include `\bin\java.exe`.

Step 6: Add this entry to your system `Path`:

```text
%JAVA_HOME%\bin
```

Step 7: Close and reopen CMD, then verify:

```cmd
echo %JAVA_HOME%
java -version
```

## 4. Install and configure Git

Git is required to upload your PySpark project to GitHub.

Step 1: Check whether Git is already installed:

```cmd
git --version
```

If you see a version number, Git is already installed. Skip to Step 5.

Step 2: If Git is not recognized, install it:

```cmd
winget install -e --id Git.Git
```

Step 3: Close and reopen CMD, PowerShell or VS Code.

Step 4: Verify:

```cmd
git --version
```

Expected:

```text
git version 2.x.x
```

Step 5: Configure your Git username and email.

Use your own GitHub username and registered email address:

```cmd
git config --global user.name "Your GitHub Username"
git config --global user.email "your-email@example.com"
```

Verify:

```cmd
git config --global --list
```

## 5. Install Visual Studio Code

Step 1: [Download Visual Studio Code](https://code.visualstudio.com/download).

Step 2: Install it using the Windows installer.

Step 3: Open VS Code.

Step 4: Install these extensions:

- Python (Microsoft)
- Python Debugger (Microsoft)

Step 5: Open your project folder using `File → Open Folder`.

## 6. Upgrade pip

Open CMD or the VS Code terminal and run:

```cmd
python -m pip install --upgrade pip
```

If `python` does not work, use:

```cmd
py -3.11 -m pip install --upgrade pip
```

## 7. Create your PySpark project

We will use this folder throughout the guide:

```text
%USERPROFILE%\pyspark_projects
```

On most machines this is `C:\Users\<your-username>\pyspark_projects`. You can use any folder you like.

Step 1: Open CMD (these commands use CMD syntax).

Step 2: Create the folder:

```cmd
mkdir %USERPROFILE%\pyspark_projects
```

Step 3: Navigate into it:

```cmd
cd %USERPROFILE%\pyspark_projects
```

Step 4: Open the folder in VS Code:

```cmd
code .
```

## 8. Create a Python virtual environment

A virtual environment keeps your PySpark dependencies separate from other Python projects.

Step 1: Open the VS Code terminal (`Ctrl + ~`).

Step 2: Create the environment:

```cmd
py -3.11 -m venv .venv
```

Step 3: Activate it:

```cmd
.venv\Scripts\activate
```

You should see:

```text
(.venv) C:\Users\<your-username>\pyspark_projects>
```

> PowerShell error: "running scripts is disabled on this system"?
> Either switch the terminal to Command Prompt, or run this once and try again:
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```

Step 4: Upgrade pip:

```cmd
python -m pip install --upgrade pip
```

Step 5: Tell VS Code to use this environment:

Press `Ctrl + Shift + P` → Python: Select Interpreter → choose the one inside `.venv`. Without this, VS Code may run a different Python.

## 9. Install PySpark 4.0.2

Step 1: Make sure your virtual environment is activated.

Step 2: Install PySpark:

```cmd
python -m pip install pyspark==4.0.2
```

Step 3: Verify:

```cmd
python -c "import pyspark; print(pyspark.__version__)"
```

Expected:

```text
4.0.2
```

Py4J is installed automatically as a dependency.

## 10. Create your first PySpark application

Step 1: In VS Code, create a file named `first_spark.py`.

Step 2: Paste this code:

```python
import os
import sys

# Configure Python for Spark workers
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("FirstSparkApplication") \
    .master("local[*]") \
    .getOrCreate()

# Sample data
data = [
    (1, "Tejas"),
    (2, "Rahul"),
    (3, "Amit")
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["id", "name"]
)

# Display DataFrame
df.show()

# Stop Spark
spark.stop()
```

Step 3: Save the file.

Step 4: Run:

```cmd
python first_spark.py
```

Expected output:

```text
+---+-----+
| id| name|
+---+-----+
|  1|Tejas|
|  2|Rahul|
|  3| Amit|
+---+-----+
```

Success! Your first PySpark application is running.

## 11. Create requirements.txt

In VS Code, create a file named `requirements.txt` and add:

```text
pyspark==4.0.2
```

Anyone downloading your project can install the dependency with:

```cmd
python -m pip install -r requirements.txt
```

## 12. Create .gitignore

Create a file named `.gitignore` and add:

```gitignore
.venv/
__pycache__/
*.py[cod]
.idea/
.vscode/
.env

# Files Spark creates locally
spark-warehouse/
metastore_db/
derby.log
```

This prevents unnecessary local files from being uploaded to GitHub.

## 13. Upload your project to GitHub

Step 1: [Create a new GitHub repository](https://github.com/new) named:

```text
pyspark-windows-setup
```

Step 2: Create a `README.md` in your project folder (you can paste this guide into it).

Step 3: Open the VS Code terminal and navigate to your project:

```cmd
cd %USERPROFILE%\pyspark_projects
```

Step 4: Initialize Git:

```cmd
git init
```

Step 5: Add your files:

```cmd
git add .
```

Step 6: Commit:

```cmd
git commit -m "Initial PySpark Windows setup"
```

Step 7: Set the main branch:

```cmd
git branch -M main
```

Step 8: Connect your GitHub repository. Replace `<your-username>` with your own GitHub username:

```cmd
git remote add origin https://github.com/<your-username>/pyspark-windows-setup.git
```

Step 9: Push your project:

```cmd
git push -u origin main
```

If GitHub asks you to authenticate, follow the browser sign-in instructions.

Your project is now on GitHub!

## 14. Common errors and solutions

| Error | Solution |
| --- | --- |
| Python not found | Use `py -3.11` or fix Python PATH |
| Java not recognized | Configure `JAVA_HOME` and Path, then reopen the terminal |
| Git not recognized | Install Git and reopen the terminal |
| Cannot run program python3 | Configure `PYSPARK_PYTHON` using `sys.executable` (see Section 10) |
| `.venv\Scripts\activate` blocked in PowerShell | Use CMD, or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Missing winutils.exe warning | Harmless for basic operations like `df.show()`. Writing Parquet/CSV locally may fail without `HADOOP_HOME` and `winutils.exe` set up |
| PySpark module not found | Activate `.venv`, install PySpark, and select the `.venv` interpreter in VS Code |
| Git push rejected | Run `git pull origin main --rebase`, resolve any conflicts, then push again |

> Important: Spark 4.0.2 supports Java 17 and Python 3.9 or later. Java 17 and Python 3.11 are suitable for this guide.

## 15. Final installation verification

Run these commands inside your activated virtual environment:

```cmd
python --version
python -m pip --version
java -version
echo %JAVA_HOME%
python -c "import pyspark; print(pyspark.__version__)"
git --version
where python
where java
```

## 16. Final project structure

Your GitHub repository should look like this:

```text
pyspark-windows-setup/
│
├── README.md
├── first_spark.py
├── requirements.txt
└── .gitignore
```

Do not upload `.venv/`.

## 17. Official resources

| Software | Download |
| --- | --- |
| Python | [Python 3.11.9](https://www.python.org/downloads/release/python-3119/) |
| Java | [Eclipse Temurin](https://adoptium.net/) |
| Git | [Git for Windows](https://git-scm.com/downloads/win) |
| VS Code | [VS Code](https://code.visualstudio.com/download) |
| PySpark | [PySpark 4.0.2 documentation](https://spark.apache.org/docs/4.0.2/api/python/getting_started/install.html) |
| GitHub | [GitHub](https://github.com/) |

---

Author: Created as a beginner-friendly Windows PySpark installation guide.

GitHub: [itejashiwarde/pyspark-windows-setup](https://github.com/itejashiwarde/pyspark-windows-setup)

If this guide helps you, please give the repository a ⭐ star!

Happy Learning and Happy Data Engineering!
