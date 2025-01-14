import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton, QMessageBox, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic

import sqlite3

from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFocusEvent
from PyQt5 import QtGui, QtCore
import numpy as np
import os
import math




class MyGUI(QMainWindow):
    
    def focusInEvent(self, event):
        self.line_edit.setCursorPosition(0)
    

    def create_database_and_table(self):
        conn=sqlite3.connect('my_database.db')
        cursor=conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_name TEXT,
                defect_number INTEGER
            )
        ''')
        conn.commit()
        conn.close()
        print("Database and table created successfully!")
        current_directory=os.getcwd()
        print("Current working directory:", current_directory)
    
    def insert_defect_number(self,project_name,defect_number):
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO my_table (project_name, defect_number) VALUES (?, ?)", (project_name, defect_number))
        conn.commit()
        conn.close()

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("new_ui.ui", self)
        self.show()
        self.line_edits = [self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5, self.lineEdit_6]

        
        for line_edit in self.line_edits:
            self.apply_line_edit_behavior(line_edit)

        self.apply_line_edit_behavior(self.lineEdit_2,"Requirements, design, and code are modified.")
        self.apply_line_edit_behavior(self.lineEdit_3,"Design and code are modified")
        self.apply_line_edit_behavior(self.lineEdit_4,"Code is modified but not design")
        self.apply_line_edit_behavior(self.lineEdit_5,"Reused code has been recently deployed and is completely unchanged for this version")
        self.apply_line_edit_behavior(self.lineEdit_6,"Autogenerated code meets the requirements and requires no modification")
        self.apply_line_edit_behavior(self.lineEdit_12,"Please enter the project name before pressing the Final Calculation button!!!!!!!!!!!!!!")
        self.apply_line_edit_behavior(self.lineEdit_13,"Total predicted fielded defects")
        self.apply_line_edit_behavior(self.lineEdit_14,"growth rate in operation")
        self.apply_line_edit_behavior(self.lineEdit_15,"number of continually operating months that software typically grows before reaching a plateau = (default = 48 months)")
        


        self.lineEdit_2.setInputMask("999999999")
        self.lineEdit_3.setInputMask("9999999999")
        self.lineEdit_4.setInputMask("999999999999")
        self.lineEdit_5.setInputMask("999999999999")
        self.lineEdit_6.setInputMask("999999999999")
        self.lineEdit_7.setInputMask("99999999999")
        self.lineEdit_8.setInputMask("999999999999")
        self.lineEdit_9.setInputMask("99999999999999")
        self.lineEdit_10.setInputMask("9999999999999999")
        self.lineEdit_11.setInputMask("999999999999999999")
        

        self.lineEdit_2.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_3.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_4.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_5.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_6.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_7.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_8.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_9.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_10.setMaxLength(10)  # For example, set to 10 characters
        self.lineEdit_11.setMaxLength(10)  # For example, set to 10 characters



        self.predicted_faults=[]
        



        self.yes_count = 0
        self.no_count = 0
        self.somewhat_count = 0
        self.yes_strength_count = 0
        self.yes_risk_count=0
        self.somewhat_strength_count=0
        self.somewhat_risk_count=0


        self.yes_checkboxes = [self.checkBox, self.checkBox_3, self.checkBox_5, self.checkBox_7, self.checkBox_9, self.checkBox_11, self.checkBox_13, self.checkBox_15,self.checkBox_17,self.checkBox_19,self.checkBox_21,self.checkBox_23,self.checkBox_25,self.checkBox_44,self.checkBox_27,self.checkBox_29,self.checkBox_31,self.checkBox_33,self.checkBox_35,self.checkBox_37,self.checkBox_39,self.checkBox_41]
        self.yes_strength_checkboxes = [self.checkBox, self.checkBox_3, self.checkBox_5, self. checkBox_7, self.checkBox_9, self.checkBox_11, self.checkBox_13, self.checkBox_15,self.checkBox_17,self.checkBox_19,self.checkBox_21,self.checkBox_23,self.checkBox_25,self.checkBox_44,self.checkBox_27]
        self.yes_risk_checboxes=[self.checkBox_29,self.checkBox_31,self.checkBox_33,self.checkBox_35,self.checkBox_37,self.checkBox_39,self.checkBox_41]
        self.no_checkboxes = [self.checkBox_2, self.checkBox_4, self.checkBox_6,self.checkBox_8,self.checkBox_10,self.checkBox_12,self.checkBox_14,self.checkBox_16,self.checkBox_18,self.checkBox_20,self.checkBox_22,self.checkBox_24,self.checkBox_26,self.checkBox_45,self.checkBox_28,self.checkBox_30,self.checkBox_32,self.checkBox_34,self.checkBox_36,self.checkBox_38,self.checkBox_40,self.checkBox_42]
        self.somewhat_checkboxes = [self.checkBox_43, self.checkBox_46, self.checkBox_47,self.checkBox_48,self.checkBox_49]
        self.somewhat_strength_checkboxes=[self.checkBox_43, self.checkBox_46, self.checkBox_47]
        self.somewhat_risk_checkboxes=[self.checkBox_48,self.checkBox_49]


        self.all_checkboxes=[self.checkBox, self.checkBox_3, self.checkBox_5, self.checkBox_7, self.checkBox_9, self.checkBox_11, self.checkBox_13, self.checkBox_15,self.checkBox_17,self.checkBox_19,self.checkBox_21,self.checkBox_23,self.checkBox_25,self.checkBox_44,self.checkBox_27,self.checkBox_29,self.checkBox_31,self.checkBox_33,self.checkBox_35,self.checkBox_37,self.checkBox_39,self.checkBox_41,self.checkBox_2, self.checkBox_4, self.checkBox_6,self.checkBox_8,self.checkBox_10,self.checkBox_12,self.checkBox_14,self.checkBox_16,self.checkBox_18,self.checkBox_20,self.checkBox_22,self.checkBox_24,self.checkBox_26,self.checkBox_45,self.checkBox_28,self.checkBox_30,self.checkBox_32,self.checkBox_34,self.checkBox_36,self.checkBox_38,self.checkBox_40,self.checkBox_42,self.checkBox_43, self.checkBox_46, self.checkBox_47,self.checkBox_48,self.checkBox_49]
        
        self.variables=[[self.checkBox,self.checkBox_2],[self.checkBox_3,self.checkBox_4],[self.checkBox_5,self.checkBox_6],[self.checkBox_7,self.checkBox_8,self.checkBox_43],[self.checkBox_9,self.checkBox_10],[self.checkBox_11,self.checkBox_12],[self.checkBox_13,self.checkBox_14],[self.checkBox_15,self.checkBox_16],[self.checkBox_17,self.checkBox_18],[self.checkBox_19,self.checkBox_20],[self.checkBox_21,self.checkBox_22],[self.checkBox_23,self.checkBox_24,self.checkBox_46],[self.checkBox_25,self.checkBox_26,self.checkBox_47],[self.checkBox_44,self.checkBox_45],[self.checkBox_27,self.checkBox_28],[self.checkBox_29,self.checkBox_30],[self.checkBox_31,self.checkBox_32],[self.checkBox_33,self.checkBox_34],[self.checkBox_35,self.checkBox_36,self.checkBox_48],[self.checkBox_37,self.checkBox_38,self.checkBox_49],[self.checkBox_39,self.checkBox_40],[self.checkBox_41,self.checkBox_42]]
       
        for group in self.variables:
            for checkbox in group:
                checkbox.stateChanged.connect(self.checkbox_state_changed)

        self.pushButton.clicked.connect(self.show_results)

        self.pushButton_2.clicked.connect(self.clear_all)

        self.pushButton_3.clicked.connect(self.defect_number)

        self.pushButton_4.clicked.connect(self.calculate_predicted_faults_button)

        self.pushButton_5.clicked.connect(self.calculate_predicted_failure_rate_per_hour)

        self.pushButton_6.clicked.connect(self.calculation_of_MTBF)

        self.pushButton_7.clicked.connect(self.calculation_of_reliability)
        

    def checkbox_state_changed(self,state):
        sender = self.sender()
        if state == Qt.Checked:
            for group in self.variables:
                if sender in group:
                    for checkbox in group:
                        if checkbox != sender:
                            checkbox.setChecked(False)
     
    
        

    def show_results(self):
        self.yes_count = 0
        self.no_count = 0
        self.somewhat_count = 0
        self.yes_strength_count = 0
        self.yes_risk_count=0
        self.somewhat_strength_count=0
        self.somewhat_risk_count=0




        for checkbox in self.yes_checkboxes:
            if checkbox.isChecked():
                self.yes_count += 1
                
                

        for checkbox in self.no_checkboxes:
            if checkbox.isChecked():
                self.no_count += 1
                
                
                
        for checkbox in self.somewhat_checkboxes:
            if checkbox.isChecked():
                self.somewhat_count += 1
                
                
        for checkbox in self.yes_strength_checkboxes:
            if checkbox.isChecked():
                self.yes_strength_count += 1
                
                

        for checkbox in self.yes_risk_checboxes:
            if checkbox.isChecked():
                self.yes_risk_count += 1
                
                

        for checkbox in self.somewhat_strength_checkboxes:
            if checkbox.isChecked():
                self.somewhat_strength_count += 1
                
                
        for checkbox in self.somewhat_risk_checkboxes:
            if checkbox.isChecked():
                self.somewhat_risk_count +=1
                
        
        defect_density=self.calculate_defect_density()
        
        self.textBrowser.setText(str(defect_density))
        self.textBrowser.setAlignment(Qt.AlignCenter)

        message = f"Yes Strength: {self.yes_strength_count}\nYes Risk: {self.yes_risk_count}\nNo: {self.no_count}\nSomewhat Strength: { self.somewhat_strength_count}\nSomewhat Risk: {self.somewhat_risk_count}"
        
        QMessageBox.information(self, "Survey Results", message)

        self.clear_all()

        
    def clear_all(self):
        for checkbox in self.all_checkboxes:
            checkbox.setChecked(False)
    
    def calculate_defect_density(self):
        
        
        if self.yes_strength_count*1+self.somewhat_strength_count*0.5+(self.somewhat_risk_count*(-0.5)+self.yes_risk_count*(-1))>=4:
            predicted_defect_density =0.11
            return predicted_defect_density
        elif self.yes_strength_count*1+self.somewhat_strength_count*0.5+(self.somewhat_risk_count*(-0.5)+self.yes_risk_count*(-1))<=0.5:
            predicted_defect_density=0.647
            return predicted_defect_density
        else:
            predicted_defect_density=0.239
            return predicted_defect_density
    def defect_number(self):
        ksloc = float(self.lineEdit.text())
        A = float(self.lineEdit_2.text())
        B = float(self.lineEdit_3.text())
        C = float(self.lineEdit_4.text())
        D = float(self.lineEdit_5.text())
        E = float(self.lineEdit_6.text())
        major_modified_ksloc=float(self.lineEdit_7.text())
        moderate_modified_ksloc=float(self.lineEdit_8.text())
        minor_modified_ksloc=float(self.lineEdit_9.text())
        reused_ksloc_without_modification=float(self.lineEdit_10.text())
        auto_generated_ksloc=float(self.lineEdit_11.text())


        result = ksloc + (A/100 * major_modified_ksloc) + (B/100 * moderate_modified_ksloc) + (C/100 * minor_modified_ksloc) + (D/100 * reused_ksloc_without_modification) + (E/100 * auto_generated_ksloc)
        

        self.normalization_conversion=0

        selected_index = self.comboBox.currentIndex()

        if selected_index == 0:
            self.normalization_conversion = 3  # Set normalization conversion for option 1
        elif selected_index == 1:
            self.normalization_conversion = 6.0  # Set normalization conversion for option 2
        elif selected_index == 2:
            self.normalization_conversion = 4.5

        normalized_result=result * self.normalization_conversion
        predicted_defect_density=self.calculate_defect_density()
        defect_number=predicted_defect_density*normalized_result
        self.textBrowser_2.setText(str(defect_number))
        self.textBrowser_2.setAlignment(Qt.AlignCenter)

        project_name = self.lineEdit_12.text()

        # Insert the data into the database
        self.insert_defect_number(project_name, defect_number)


        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()

        return defect_number


        
    def apply_line_edit_behavior(self, line_edit, explanation_text=""):
        line_edit.setPlaceholderText(explanation_text)
        line_edit.mousePressEvent = lambda event: self.line_edit_clicked(line_edit, event)

    def line_edit_clicked(self, line_edit, event):
        line_edit.setPlaceholderText("")
        focus_event = QtGui.QFocusEvent(QtCore.QEvent.FocusIn)
        line_edit.focusInEvent(focus_event)
    
        # Calculate the predicted faults using the Exponential Model formula
    def calculate_predicted_faults(self,N, Q, TF):
        predicted_faults = []

        for i in range(1, TF + 1):
            term1 = np.exp(-Q * (i - 1) / TF, dtype=np.float64)
            term2 = np.exp(-Q * i / TF, dtype=np.float64)
            predicted_faults_i = N * (term1 - term2)
            predicted_faults.append(predicted_faults_i)

            print(f"Month {i}:")
            print(f"term1: {term1}")
            print(f"term2: {term2}")
            print(f"predicted_faults_i: {predicted_faults_i}")

        return predicted_faults

    # Inside your method where you calculate the predicted faults:
    def calculate_predicted_faults_button(self):
        # Convert N, Q, TF values from lineEdit fields
        N = float(self.lineEdit_13.text())
        Q = float(self.lineEdit_14.text())
        TF = int(float((self.lineEdit_15.text())))

        print(f"N: {N}")
        print(f"Q: {Q}")
        print(f"TF: {TF}")

        # Calculate predicted faults
        self.predicted_faults = self.calculate_predicted_faults(N, Q, TF)

        


        # Display the result in textBrowser_3
        self.textBrowser_3.clear()  # Clear the textBrowser first
        self.textBrowser_3.append("Predicted Faults:")
        for i, faults in enumerate(self.predicted_faults, 1):
            self.textBrowser_3.append(f"Month {i}: {faults:.2f}")

    def calculate_predicted_failure_rate_per_hour(self):
        try:
            # Get the predicted duty cycle hours from the lineEdit
            predicted_duty_cycle_hours = float(self.lineEdit_16.text())

            if self.predicted_faults:
                # Calculate predicted failure rate per hour for each month
                self.predicted_failure_rate_per_hour = [fault / predicted_duty_cycle_hours for fault in self.predicted_faults]

                # Display the results in textBrowser_4
                self.textBrowser_4.clear()  # Clear textBrowser_4
                self.textBrowser_4.append("Predicted Failure Rate Per Hour:")
                for i, rate in enumerate(self.predicted_failure_rate_per_hour, 1):
                    self.textBrowser_4.append(f"Month {i}: {rate:.4f}")
            else:
            # Handle the case where predicted_faults are not available
                QMessageBox.warning(self, "Warning", "Calculate predicted faults first.")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid input for predicted duty cycle hours.")

    def calculation_of_MTBF(self):
        try:
            if self.predicted_faults:
                # Calculate MTBF for each month
                MTBF = [1 / rate for rate in self.predicted_failure_rate_per_hour]

                # Get the percentage of critical failures from lineEdit_17
                critical_severity_percentage = float(self.lineEdit_17.text())

                # Calculate MTBCF (Mean Time Between Critical Failures)
                self.MTBCF = [critical_severity_percentage * mtbf for mtbf in MTBF]

                # Display the results in textBrowser_5
                self.textBrowser_5.clear()  # Clear textBrowser_5
                self.textBrowser_5.append("MTBCF (Mean Time Between Critical Failures) for Each Month:")
                for i, mtbcf in enumerate(self.MTBCF, 1):
                    self.textBrowser_5.append(f"Month {i}: {mtbcf:.4f}")
            else:
                # Handle the case where predicted_faults are not available
                QMessageBox.warning(self, "Warning", "Calculate predicted faults first.")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid input for predicted duty cycle hours or critical severity percentage.")
        
    

    

    def calculation_of_reliability(self):
        try:
            # Get the mission time from the lineEdit_18 widget
            mission_time = float(self.lineEdit_18.text())

            if self.MTBCF:
                # Calculate and display reliability for each MTBCF value
                self.textBrowser_6.clear()  # Clear textBrowser_6
                self.textBrowser_6.append("Reliability for Each Month:")
                
                for i, mtbcf in enumerate(self.MTBCF, 1):
                    reliability = math.exp(-mission_time / mtbcf)
                    self.textBrowser_6.append(f"Month {i}: {reliability:.4f}")
            else:
                QMessageBox.warning(self, "Warning", "Calculate MTBCF first.")

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid input for mission time.")




        

        



  
def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.create_database_and_table()
    app.exec_()

if __name__ == '__main__':
            main()

