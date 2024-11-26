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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(185, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "First Name:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(185, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "Last Name:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(13, 141)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(185, 36)
        self._label3.TabIndex = 2
        self._label3.Text = "Full Name:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(237, 141)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(185, 36)
        self._label4.TabIndex = 3
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 203)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(185, 43)
        self._button1.TabIndex = 4
        self._button1.Text = "Show Name"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(237, 203)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(185, 43)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(237, 23)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(185, 20)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(237, 85)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(185, 20)
        self._textBox2.TabIndex = 7
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(434, 258)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg119 FullName"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        FN = str(self._textBox1.Text)
        LN = str(self._textBox2.Text)
        
        self._label4.Text = str(FN + " " + LN)

    def Button2Click(self, sender, e):
        self._label4.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""