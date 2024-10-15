import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(65, 374)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(195, 40)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(365, 374)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(195, 40)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(700, 374)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(195, 40)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(177, 38)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(127, 46)
        self._label1.TabIndex = 3
        self._label1.Text = "A:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(177, 95)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(127, 46)
        self._label2.TabIndex = 4
        self._label2.Text = "B:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(177, 152)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(127, 46)
        self._label3.TabIndex = 5
        self._label3.Text = "C:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(177, 223)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(127, 46)
        self._label4.TabIndex = 6
        self._label4.Text = "First Root:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(476, 223)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(188, 46)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(476, 48)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(188, 26)
        self._textBox1.TabIndex = 8
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(476, 105)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(188, 26)
        self._textBox2.TabIndex = 9
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(476, 162)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(188, 26)
        self._textBox3.TabIndex = 10
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(476, 300)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(188, 46)
        self._label6.TabIndex = 11
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(177, 300)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(127, 46)
        self._label7.TabIndex = 12
        self._label7.Text = "Second Root:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(953, 457)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold)
        self.Name = "MainForm"
        self.Text = "Prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = float(self._textBox1.Text)
        B = float(self._textBox2.Text)
        C = float(self._textBox3.Text)
        root = (-B + math.sqrt(B**2-4*A*C))/(2*A)
        root2 = (-B - math.sqrt(B**2-4*A*C))/(2*A)
        self._label5.Text = str(root)
        self._label6.Text = str(root2)

    def Button2Click(self, sender, e):
        self._label5.Text = ""
        self._label6.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()
