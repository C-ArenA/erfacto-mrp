import subprocess

def compile_latex(filename):
  """
  Compiles a LaTeX document using the given recipe.

  Args:
    filename: The name of the LaTeX file (including .tex extension).
  """
  # Compile with pdflatex
  subprocess.run(["pdflatex", filename])
  print("1:pdflatex")

  # Run Biber for bibliography processing
  subprocess.run(["biber", filename[:-4]])  # Remove .tex extension
  print("2:biber")

  # Compile with pdflatex twice (can be adjusted as needed)
  for _ in range(2):
    subprocess.run(["pdflatex", filename])
    print("3:pdflatex")


# Example usage
filename = "main.tex"
compile_latex(filename)

print("Compilation complete!")
