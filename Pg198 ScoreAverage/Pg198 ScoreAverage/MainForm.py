﻿import System.Drawing
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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Cyan
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(123, 37)
        self._label1.TabIndex = 0
        self._label1.Text = "Score 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Cyan
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 104)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(123, 37)
        self._label2.TabIndex = 1
        self._label2.Text = "Score 2:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Cyan
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 177)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(123, 37)
        self._label3.TabIndex = 2
        self._label3.Text = "Score 3:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Cyan
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 250)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(123, 37)
        self._label4.TabIndex = 3
        self._label4.Text = "Average:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumSpringGreen
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(203, 250)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(123, 37)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 306)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(100, 52)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(119, 306)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(100, 52)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(226, 306)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(100, 52)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(203, 39)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(123, 20)
        self._textBox1.TabIndex = 8
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(203, 113)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(123, 20)
        self._textBox2.TabIndex = 9
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(203, 186)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(123, 20)
        self._textBox3.TabIndex = 10
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(338, 370)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg198 ScoreAverage"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        S1 = float(self._textBox1.Text)
        S2 = float(self._textBox2.Text)
        S3 = float(self._textBox3.Text)
        
        A = round((S1 + S2 + S3) / 3, 2)
        self._label5.Text = str(A)

    def Button2Click(self, sender, e):
        self._label5.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()