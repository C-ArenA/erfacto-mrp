import subprocess
import os

def is_valid(filename):
  """
  Verifica que el proceso se esté corriendo de forma válida, dentro
  del directorio esperado y con un archivo existente
  """
  if not os.path.isfile(filename):
    raise Exception("No hay un archivo main.tex en esta carpeta")


def compile_latex(filename):
  """
  Compiles a LaTeX document using the given recipe.

  Args:
    filename: The name of the LaTeX file (including .tex extension).
  """
  is_valid(filename)
  # Formatea código
  subprocess.run(["npm", "run", "prettier"])
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
