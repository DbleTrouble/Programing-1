import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(65, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(247, 143)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Quantity Sold"
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(6, 18)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Package A:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(6, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Package B:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(6, 103)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Package C:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(141, 18)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 22)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(141, 60)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 22)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(141, 103)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 22)
        self._textBox3.TabIndex = 5
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 180)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(177, 147)
        self._listBox1.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(231, 180)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(158, 39)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(231, 234)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(158, 39)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(231, 288)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(158, 39)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(401, 340)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg269 SoftwareSales"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        P1 = int(self._textBox1.Text)
        P2 = int(self._textBox1.Text)
        P3 = int(self._textBox1.Text)
        Pa = P1 * 99
        Pb = P2 * 199
        Pc = P3 * 299
        
        if P1 >= 10 and P1 <= 19:
            a = Pa * .2
            Total1 = Pa - a
            self._listBox1.Items.Add("Package A: $" + str(Total1))
        elif P1 >= 20 and P1 <= 49:
            a = Pa * .3
            Total1 = Pa - a
            self._listBox1.Items.Add("Package A: $" + str(Total1))
        elif P1 >= 50 and P1 <= 99:
            a = Pa * .4
            Total1 = Pa - a
            self._listBox1.Items.Add("Package A: $" + str(Total1))
        elif P1 >= 100:
            a = Pa * .5
            Total1 = Pa - a
            self._listBox1.Items.Add("Package A: $" + str(Total1))
            
        if P2 >= 10 and P2 <= 19:
            b = Pb * .2
            Total2 = Pb - b
            self._listBox1.Items.Add("Package B: $" + str(Total2))
        elif P2 >= 20 and P2 <= 49:
            b = Pb * .3
            Total2 = Pb - b
            self._listBox1.Items.Add("Package B: $" + str(Total2))
        elif P2 >= 50 and P2 <= 99:
            b = Pb * .4
            Total2 = Pb - b
            self._listBox1.Items.Add("Package B: $" + str(Total2))
        elif P2 >= 100:
            b = Pb * .5
            Total2 = Pb - b
            self._listBox1.Items.Add("Package B: $" + str(Total2))

        if P3 >= 10 and P3 <= 19:
            c = Pc * .2
            Total3 = Pc - c
            self._listBox1.Items.Add("Package C: $" + str(Total3))
        elif P3 >= 20 and P3 <= 49:
            c = Pc * .3
            Total3 = Pc - c
            self._listBox1.Items.Add("Package C: $" + str(Total3))
        elif P3 >= 50 and P3 <= 99:
            c = Pc * .4
            Total3 = Pc - c
            self._listBox1.Items.Add("Package C: $" + str(Total3))
        elif P3 >= 100:
            c = Pc * .5
            Total3 = Pc - c
            self._listBox1.Items.Add("Package C: $" + str(Total3))
            
        grand = Total1 + Total2 + Total3
        self._listBox1.Items.Add("Grand Total: $" + str(grand))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._listBox1.Items.Clear

    def Button3Click(self, sender, e):
        Application.Exit()