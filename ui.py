import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit,
    QLabel, QFileDialog, QMessageBox
)
from PyQt5.QtCore import QStandardPaths
from Commands.Invoker import Invoker
from Commands.MergeCommand import MergeCommand


class PDFMergerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input Folder Path
        self.input_label = QLabel("Input Folder Path:")
        self.input_path = QLineEdit()
        self.input_browse = QPushButton("Browse")
        self.input_browse.clicked.connect(self.browse_input_folder)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_path)
        input_layout.addWidget(self.input_browse)

        # Output Folder Path
        self.output_label = QLabel("Output Folder Path:")
        default_output_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        self.output_path = QLineEdit(default_output_path)
        self.output_browse = QPushButton("Browse")
        self.output_browse.clicked.connect(self.browse_output_folder)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(self.output_browse)

        # File Name
        self.file_name_label = QLabel("File Name:")
        self.file_name_input = QLineEdit()
        self.file_name_input.setText("merged")

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.merge_pdfs)

        # Add widgets to layout
        layout.addWidget(self.input_label)
        layout.addLayout(input_layout)
        layout.addWidget(self.output_label)
        layout.addLayout(output_layout)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def browse_input_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Input Folder")
        if folder:
            self.input_path.setText(folder)

    def browse_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_path.setText(folder)

    def validate_file_name(self):
        file_name = self.file_name_input.text().strip()
        if not file_name:
            QMessageBox.warning(self, "Input Error", "File name cannot be empty.")
            return

        if not file_name.lower().endswith(".pdf"):
            file_name += ".pdf"

        QMessageBox.information(self, "Success", f"File will be saved as: {file_name}")
        return file_name


    def merge_pdfs(self):
        invoker = Invoker()
        invoker.set_command(MergeCommand(self.input_path.text(), self.output_path.text(), self.validate_file_name()))
        invoker.run()

