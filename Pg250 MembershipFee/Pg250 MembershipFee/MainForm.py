﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.Gold
        self._groupBox1.Controls.Add(self._radioButton4)
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(237, 158)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Type of Membership"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.Gold
        self._groupBox2.Controls.Add(self._checkBox3)
        self._groupBox2.Controls.Add(self._checkBox2)
        self._groupBox2.Controls.Add(self._checkBox1)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(269, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(237, 158)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Options"
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.Gold
        self._groupBox3.Controls.Add(self._textBox1)
        self._groupBox3.Controls.Add(self._label1)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(13, 204)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(237, 158)
        self._groupBox3.TabIndex = 1
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Membership Length"
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(36, 22)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(145, 24)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Yoga"
        self._checkBox1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(36, 65)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(145, 24)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Karate"
        self._checkBox2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(36, 109)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(145, 24)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(23, 22)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(182, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Standard Adult"
        self._radioButton1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(23, 52)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(182, 24)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Child (12 and under)"
        self._radioButton2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(23, 82)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(182, 24)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Student"
        self._radioButton3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(23, 112)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(182, 24)
        self._radioButton4.TabIndex = 3
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Senior Citizen"
        self._radioButton4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 368)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(136, 66)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # groupBox4
        # 
        self._groupBox4.BackColor = System.Drawing.Color.Gold
        self._groupBox4.Controls.Add(self._label5)
        self._groupBox4.Controls.Add(self._label4)
        self._groupBox4.Controls.Add(self._label3)
        self._groupBox4.Controls.Add(self._label2)
        self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox4.Location = System.Drawing.Point(269, 204)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(237, 158)
        self._groupBox4.TabIndex = 1
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Membership Fees"
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(194, 368)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(136, 66)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(370, 368)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 66)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(23, 38)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(182, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter the Number of Months:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(23, 100)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(182, 22)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(36, 38)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 0
        self._label2.Text = "Monthly Fee:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(36, 99)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 1
        self._label3.Text = "Total:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(157, 38)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(74, 23)
        self._label4.TabIndex = 2
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(157, 99)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(74, 23)
        self._label5.TabIndex = 3
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(518, 446)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg250 MembershipFee"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self._groupBox3.PerformLayout()
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)



    def Button1Click(self, sender, e):
        BF = 0.0
        D  = 0.0
        TF = 0.0
        M  = 0.0
        
        try:
            M = int(self._textBox1.Text)
        except:
            MessageBox.Show("Months must be a valid integer", "Input Error")
            return
        if M < 1 or M > 12:
            MessageBox.Show("Months must be a valid integer", "Input Error")
            return
        if self._radioButton1.Checked == True:
            BF = 40
        elif self._radioButton2.Checked == True:
            BF = 20
        elif self._radioButton3.Checked == True:
            BF = 25
        elif self._radioButton4.Checked == True:
            BF = 30
        
        if self._checkBox1.Checked == True:
            BF += 10
        elif self._checkBox2.Checked == True:
            BF += 30
        elif self._checkBox3.Checked == True:
            BF += 50
        
        if M <= 3:
            D = 0.0
        elif M >= 4 and M <= 6:
            D = BF * .05
        elif M >= 7 and M <= 9:
            D = BF * .08
        elif M >= 10:
            D = BF * .1
        
        BF -= D
        TF = BF * M
        
        self._label4.Text = str(round(BF, 2))
        self._label5.Text = str(round(TF, 2))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()