import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(110, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "Sales for the month:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 65)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(110, 40)
        self._label2.TabIndex = 1
        self._label2.Text = "Advance pay awarded:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 123)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(110, 40)
        self._label3.TabIndex = 2
        self._label3.Text = "Commission Rate:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 180)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(110, 40)
        self._label4.TabIndex = 3
        self._label4.Text = "Commission:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 238)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(110, 40)
        self._label5.TabIndex = 4
        self._label5.Text = "Net Pay:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(172, 123)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(110, 40)
        self._label6.TabIndex = 5
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(172, 180)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(110, 40)
        self._label7.TabIndex = 6
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(172, 238)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(110, 40)
        self._label8.TabIndex = 7
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 297)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(84, 61)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(110, 297)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(84, 61)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(200, 297)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(84, 61)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(172, 20)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(110, 20)
        self._textBox1.TabIndex = 11
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(172, 76)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(110, 20)
        self._textBox2.TabIndex = 12
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(296, 370)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg240 CommissionCalculator"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button1Click(self, sender, e):
        S = float(self._textBox1.Text)
        A = float(self._textBox2.Text)
        CR = 0.0
        C = 0.0
        
        if S < 10000:
            CR = 0.05
        elif S >= 10000 and S < 15000:
            CR = 0.1
        elif S >= 15000 and S < 18000:
            CR = 0.12
        elif S >= 18000 and S < 22000:
            CR = 0.14
        elif S >= 22000:
            CR = 0.15
        C = S * CR   

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()