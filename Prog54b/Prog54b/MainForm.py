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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label8 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(202, 46)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(141, 37)
        self._label1.TabIndex = 0
        self._label1.Text = "First Digit"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(202, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(141, 37)
        self._label2.TabIndex = 1
        self._label2.Text = "Second Digit"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(202, 120)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(141, 37)
        self._label3.TabIndex = 2
        self._label3.Text = "Third Digit"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(70, 213)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(273, 37)
        self._label4.TabIndex = 3
        self._label4.Text = "The sum of the four numbers is:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(42, 261)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(301, 37)
        self._label5.TabIndex = 4
        self._label5.Text = "The average of the four numbers is:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label6.Cursor = System.Windows.Forms.Cursors.Default
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(502, 213)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(261, 37)
        self._label6.TabIndex = 5
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(502, 261)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(261, 37)
        self._label7.TabIndex = 6
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label7.UseCompatibleTextRendering = True
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(147, 323)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(181, 39)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(401, 323)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(181, 39)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(675, 323)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(181, 39)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(202, 157)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(141, 37)
        self._label8.TabIndex = 10
        self._label8.Text = "Fourth Digit"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(502, 62)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(261, 20)
        self._textBox1.TabIndex = 11
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(502, 93)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(261, 20)
        self._textBox2.TabIndex = 12
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(502, 130)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(261, 20)
        self._textBox3.TabIndex = 13
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(502, 167)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(261, 20)
        self._textBox4.TabIndex = 14
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(964, 465)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        First_digit = int(self._textBox1.Text)
        Second_digit = int(self._textBox2.Text)
        Third_digit = int(self._textBox3.Text)
        Fourth_digit = int(self._textBox4.Text)
        Sum = First_digit + Second_digit + Third_digit + Fourth_digit
        Average = (First_digit + Second_digit + Third_digit + Fourth_digit) / 4.0
        self._label6.Text = str(Sum)
        self._label7.Text = str(Average)

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label6.Text = ""
        self._label7.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""