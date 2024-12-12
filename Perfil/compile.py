import subprocess
import os

def main():
    # Change the current working directory to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Create the 'build' directory
    build_dir = os.path.join(script_dir, 'build')
    os.makedirs(build_dir, exist_ok=True)

    # Run the LaTeX compilation process
    for command in [
        ('pdflatex', '--output-directory=build', 'main.tex'),
        ('biber', '--output-directory=build', 'main'),
        ('pdflatex', '--output-directory=build', 'main.tex'),
        ('pdflatex', '--output-directory=build', 'main.tex')
    ]:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=open(os.path.join(build_dir, f'{command[0]}.log'), 'w'))
        print(f"{command[0]}...")

if __name__ == "__main__":
    main()
