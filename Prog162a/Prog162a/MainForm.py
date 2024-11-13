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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DodgerBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(128, 42)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DodgerBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(160, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(128, 42)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DodgerBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(311, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(128, 42)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(311, 105)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(128, 39)
        self._label1.TabIndex = 4
        self._label1.Text = "Enter Number:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(311, 258)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(128, 39)
        self._label2.TabIndex = 5
        self._label2.Text = "The Factorial:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(311, 329)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(128, 39)
        self._label3.TabIndex = 6
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(311, 181)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(128, 20)
        self._textBox1.TabIndex = 7
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 105)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(276, 264)
        self._listBox1.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self.ClientSize = System.Drawing.Size(451, 383)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog162a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        text = int(self._textBox1.Text)
        x = 1
        for num in range(1,text+1):
            x = x * num
            line = str(num)
            self._listBox1.Items.Add(line)
            self._label3.Text = str(x)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label3.Text = ""
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()