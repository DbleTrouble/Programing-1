import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 16
        self._listBox1.Location = System.Drawing.Point(13, 13)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(225, 436)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(245, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(124, 32)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(245, 70)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(124, 32)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(245, 127)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(124, 32)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Gold
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(245, 210)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(124, 34)
        self._label1.TabIndex = 4
        self._label1.Text = "Hours"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Gold
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(245, 326)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(124, 34)
        self._label2.TabIndex = 5
        self._label2.Text = "Rate of Pay"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(245, 272)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(124, 20)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(245, 385)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(124, 20)
        self._textBox2.TabIndex = 7
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(381, 470)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        heading = "Hours\t\tPay"
        self._listBox1.Items.Add(heading)
        
        hour = int(self._textBox1.Text)
        
        
        for num in range(1, hour+1):
            rate = float(self._textBox2.Text)
            pay = num * rate
            line = str(num) + "\t\t" + str(pay)
            self._listBox1.Items.Add(line)
                
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()