### in this i am unable to plot the data instead with every entry, the axis gets reinitialised on the basis of given input


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()  # Create a Figure instance
        self.canvas = FigureCanvas(self.figure)  # Create a FigureCanvas instance and pass the Figure
        layout = QVBoxLayout()  # Create a QVBoxLayout to hold the FigureCanvas
        layout.addWidget(self.canvas)  # Add the FigureCanvas to the layout
        self.setLayout(layout)  # Set the layout for the GraphWidget

    def plot_graph(self, x_data, y_data):
        self.figure.clear()  # Clear the previous plot
        ax = self.figure.add_subplot(111)  # Add a subplot to the Figure
        ax.plot(x_data, y_data)  # Plot the data on the subplot
        self.canvas.draw()  # Redraw the FigureCanvas


class DataInputWidget(QWidget):
    def __init__(self, graph_widget, parent=None):
        super().__init__(parent)
        self.graph_widget = graph_widget  # Reference to the GraphWidget

        layout = QVBoxLayout()  # Create a QVBoxLayout for the DataInputWidget

        self.label = QLabel("Enter Data:")  # Create a QLabel for the data input label
        layout.addWidget(self.label)

        self.line_edit = QLineEdit()  # Create a QLineEdit for the data input field
        layout.addWidget(self.line_edit)

        self.button = QPushButton("Plot Data")  # Create a QPushButton for plotting the data
        self.button.clicked.connect(self.plot_data)  # Connect the button's clicked signal to the plot_data method
        layout.addWidget(self.button)

        self.setLayout(layout)  # Set the layout for the DataInputWidget

    def plot_data(self):
        data = self.line_edit.text()  # Get the text from the QLineEdit
        self.line_edit.clear()
        # Parse the data and extract x and y values
        try:
            x_data, y_data = [float(val) for val in data.split(",")]
        except ValueError:
            print("Invalid input format. Please enter comma-separated numeric values.")
            return

        self.graph_widget.plot_graph([x_data], [y_data])  # Plot the data on the GraphWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graph_widget = GraphWidget()  # Create an instance of the GraphWidget
        self.data_input_widget = DataInputWidget(self.graph_widget)  # Create an instance of the DataInputWidget

        main_layout = QVBoxLayout()  # Create a QVBoxLayout for the main layout
        main_layout.addWidget(self.data_input_widget)  # Add the DataInputWidget to the main layout
        main_layout.addWidget(self.graph_widget)  # Add the GraphWidget to the main layout

        main_widget = QWidget()  # Create a QWidget for the main widget
        main_widget.setLayout(main_layout)  # Set the main layout for the main widget
        self.setCentralWidget(main_widget)  # Set the main widget as the central widget for the MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
