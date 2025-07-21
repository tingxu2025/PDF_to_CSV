import os
import tabula
from tkinter import Tk, filedialog, messagebox

# Hide the GUI root window
root = Tk()
root.withdraw()

pdf_files = filedialog.askopenfilenames(
    title="Select PDF files to convert",
    filetypes=[("PDF files", "*.pdf")]
)

if not pdf_files:
    print("No PDF files selected.")
    messagebox.showerror("No files selected", "You didn't select any PDF files.")
    exit()

for input_path in pdf_files:
    try:
        input_path = input_path.replace("/", os.sep)
        base_dir = os.path.dirname(input_path)
        filename = os.path.basename(input_path)
        output_filename = f"output_{os.path.splitext(filename)[0]}.csv"
        output_path = os.path.join(base_dir, output_filename)

        print(f"Converting {filename}")

        input_path = os.path.normpath(input_path)
        output_path = os.path.normpath(output_path)

        tabula.convert_into(
            input_path=input_path,
            output_path=output_path,
            output_format="csv",
            pages="all",
            lattice=True
        )
        print(f"Done: {output_path}")
        messagebox.showinfo("Done", f"Converted: {filename}\nSaved as:\n{output_filename}")
    except Exception as e:
        print(f"Error converting {filename}: {e}")
        messagebox.showerror("Error", f"ailed to convert {filename}\n\n{e}")
