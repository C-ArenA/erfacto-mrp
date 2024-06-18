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

# Example usage
filename = "main.tex"
compile_latex(filename)

print("Compilation complete!")
