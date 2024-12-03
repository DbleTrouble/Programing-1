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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(33, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(135, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "Class A:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(33, 99)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(135, 41)
        self._label2.TabIndex = 1
        self._label2.Text = "Class B:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(33, 179)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(135, 41)
        self._label3.TabIndex = 2
        self._label3.Text = "Class C:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(346, 31)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(135, 41)
        self._label4.TabIndex = 3
        self._label4.Text = "Class A Price:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(346, 99)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(135, 41)
        self._label5.TabIndex = 4
        self._label5.Text = "Class B Price:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(346, 179)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(135, 41)
        self._label6.TabIndex = 5
        self._label6.Text = "Class C Price:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(144, 272)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(135, 41)
        self._label7.TabIndex = 6
        self._label7.Text = "Total Revenue:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(368, 272)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(135, 41)
        self._label8.TabIndex = 7
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(190, 42)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 8
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(190, 110)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 9
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(190, 190)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 10
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(497, 42)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 20)
        self._textBox4.TabIndex = 11
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(497, 110)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 20)
        self._textBox5.TabIndex = 12
        # 
        # textBox6
        # 
        self._textBox6.Location = System.Drawing.Point(497, 190)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(100, 20)
        self._textBox6.TabIndex = 13
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 342)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(155, 44)
        self._button1.TabIndex = 14
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(245, 342)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(155, 44)
        self._button2.TabIndex = 15
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(469, 342)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(155, 44)
        self._button3.TabIndex = 16
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.WindowFrame
        self.ClientSize = System.Drawing.Size(636, 398)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg186 StadiumSeating"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = float(self._textBox1.Text)
        B = float(self._textBox2.Text)
        C = float(self._textBox3.Text)
        AP = float(self._textBox4.Text)
        BP = float(self._textBox5.Text)
        CP = float(self._textBox6.Text)
        
        TR = (A * AP) + (B * BP) + (C * CP)
        self._label8.Text = str(TR)

    def Button2Click(self, sender, e):
        self._label8.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()