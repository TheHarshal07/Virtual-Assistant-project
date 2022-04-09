

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
import mysql.connector as con
class LoginApp(QDialog):
      def __init__(self):
          super(LoginApp,self).__init__()
          loadUi("Login1.ui",self)
          self.l1.clicked.connect(self.login)
          self.signIn.clicked.connect(self.show_reg)

      def login(self):
          un = self.u1.text()
          pw = self.p1.text()
          db = con.connect(host="localhost",user="root",password="Harshal",database="userlist",port="3307")
          cursor = db.cursor()  
          cursor.execute("select * from users where username = '"+ un +"' and password = '"+ pw +"' ")
          result = cursor.fetchone()
          if result:
              QMessageBox.information(self,"Login Output","login seuccessfully!")
              p = LoginApp()
              p.close()
          else:
              QMessageBox.information(self,"Login Output","Invalid User.. Register for new user ")
        
      def show_reg(self):
          Widget.setCurrentIndex(1)

          

class RegAPP(QDialog):
      def __init__(self):
          super(RegAPP,self).__init__()
          loadUi("SIGNup1.ui",self)   
          self.pushButton.clicked.connect(self.reg)
          self.pushButton_2.clicked.connect(self.show_login) 
      def reg(self):
          un = self.user.text()
          pw = self.passw.text()
          em = self.email.text()
          pnum = self.pnum.text()
        
          db = con.connect(host="localhost",user="root",password="Harshal",database="userlist",port="3307")
          cursor= db.cursor()
          cursor.execute("select * from users where username = '"+ un +"' and password = '"+ pw +"'")
          result= cursor.fetchone()
        
          
          if result:
              QMessageBox.information(self,"Login form","The user already registered, try another username!!")
          else:
               if (un and pw and em and pnum):
                   if(pnum.isdigit()):
                    cursor.execute("insert into users values ('"+ un +"','"+ pw +"','"+ em +"','"+ pnum +"')")
                    db.commit()
                    QMessageBox.information(self,"Login form","The user registered successfully ")
                    p1 = LoginApp()
                    p1.show()
                    
                    
                   else:
                        QMessageBox.information(self,"invalid","Please enter valid mobile number ")
                       
               else:
                   QMessageBox.information(self,"invalid","please enter valid detalis ")



      def show_login(self):
          Widget.setCurrentIndex(0)

app = QApplication(sys.argv)
Widget = QtWidgets.QStackedWidget()
loginform = LoginApp()
registrationform = RegAPP() 
Widget.addWidget(loginform)
Widget.addWidget(registrationform)
Widget.setCurrentIndex(0)
Widget.show()
Widget.setFixedWidth(1141)
Widget.setFixedHeight(756)
app.exec_()