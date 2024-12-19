from Commands.Command import Command
from PyPDF2 import PdfMerger
import os
class MergeCommand(Command):

    def __init__(self, input_path, output_path, file_name):
        self.input_path = input_path
        self.output_path = output_path
        self.file_name = file_name

    def execute(self) -> None:
        merger = PdfMerger()
        pdf_files = [f for f in os.listdir(self.input_path) if f.endswith('.pdf')]
        pdf_files.sort()
        for pdf_file in pdf_files:
            merger.append(os.path.join(self.input_path, pdf_file))
        

        _output_path = os.path.join(self.output_path, self.file_name)
        try:
            merger.write(_output_path)
        except PermissionError as e:
            print(f"Permission denied: {e}. Please check the output path and permissions.")
        finally:
            merger.close()


