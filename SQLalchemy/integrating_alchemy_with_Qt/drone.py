import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from sqlalchemy import Column, Integer, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Drone(Base):
    __tablename__ = 'drones'

    drone_id = Column(Integer, primary_key=True)
    speed = Column(Float)
    altitude = Column(Float)

    def __init__(self, drone_id, speed, altitude):
        self.drone_id = drone_id
        self.speed = speed
        self.altitude = altitude


class DroneForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the GUI
        self.setWindowTitle("Drone Form")
        layout = QVBoxLayout()

        self.id_label = QLabel("Drone ID:")
        self.id_line_edit = QLineEdit()

        self.speed_label = QLabel("Speed:")
        self.speed_line_edit = QLineEdit()

        self.altitude_label = QLabel("Altitude:")
        self.altitude_line_edit = QLineEdit()

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_drone)

        layout.addWidget(self.id_label)
        layout.addWidget(self.id_line_edit)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_line_edit)
        layout.addWidget(self.altitude_label)
        layout.addWidget(self.altitude_line_edit)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Set up the database connection
        database_url = 'sqlite:///drones2.db'
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def save_drone(self):
        # Get the input values
        drone_id = int(self.id_line_edit.text())
        speed = float(self.speed_line_edit.text())
        altitude = float(self.altitude_line_edit.text())

        # Create a new Drone object and add it to the session
        new_drone = Drone(drone_id=drone_id, speed=speed, altitude=altitude)
        self.session.add(new_drone)
        self.session.commit()

        # Clear the input fields
        self.id_line_edit.clear()
        self.speed_line_edit.clear()
        self.altitude_line_edit.clear()




if __name__ == '__main__':
    app = QApplication(sys.argv)

    drone_form = DroneForm()
    drone_form.show()

    sys.exit(app.exec_())
