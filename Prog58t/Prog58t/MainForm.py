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
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(222, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(155, 34)
        self._label1.TabIndex = 0
        self._label1.Text = "Purchase Price:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(222, 81)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(155, 34)
        self._label2.TabIndex = 1
        self._label2.Text = "Amount Recived: "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(222, 131)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(155, 34)
        self._label3.TabIndex = 2
        self._label3.Text = "Change Due:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(222, 188)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(155, 34)
        self._label4.TabIndex = 3
        self._label4.Text = "Dollars:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(222, 232)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(155, 34)
        self._label5.TabIndex = 4
        self._label5.Text = "Quarters:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(222, 275)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(155, 34)
        self._label6.TabIndex = 5
        self._label6.Text = "Dimes:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(222, 320)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(155, 34)
        self._label7.TabIndex = 6
        self._label7.Text = "Nickels:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(222, 365)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(155, 34)
        self._label8.TabIndex = 7
        self._label8.Text = "Pennies:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(513, 188)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(155, 34)
        self._label9.TabIndex = 8
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(513, 232)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(155, 34)
        self._label10.TabIndex = 9
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(513, 275)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(155, 34)
        self._label11.TabIndex = 10
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(513, 320)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(155, 34)
        self._label12.TabIndex = 11
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(513, 365)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(155, 34)
        self._label13.TabIndex = 12
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(513, 39)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(155, 20)
        self._textBox1.TabIndex = 13
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(513, 90)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(155, 20)
        self._textBox2.TabIndex = 14
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(513, 140)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(155, 20)
        self._textBox3.TabIndex = 15
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 420)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(146, 36)
        self._button1.TabIndex = 16
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(369, 420)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(146, 36)
        self._button2.TabIndex = 17
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(733, 420)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(146, 36)
        self._button3.TabIndex = 18
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(953, 470)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        purchase_price = float(self._textBox1.Text)
        amount_recived = float(self._textBox2.Text)
        change_due = (amount_recived - purchase_price)
        self._textBox3.Text = str(change_due)
        
        dollar = (change_due // 1)
        quarter = ((change_due - dollar) // .25)
        dime = ((change_due - dollar - (quarter * .25)) // .10)
        nickel = ((change_due - dollar - (quarter * .25) - (dime * .10)) // .05)
        penny = ((change_due - dollar - (quarter * .25) - (dime * .10) - (nickel * .05)) // .01)
        
        self._label9.Text = str(dollar)
        self._label10.Text = str(quarter)
        self._label11.Text = str(dime)
        self._label12.Text = str(nickel)
        self._label13.Text = str(penny)

    def Button2Click(self, sender, e):
        self._label9.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()