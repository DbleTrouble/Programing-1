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
        self._label1.BackColor = System.Drawing.Color.Yellow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(145, 34)
        self._label1.TabIndex = 0
        self._label1.Text = "Pounds:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Yellow
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 106)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(145, 34)
        self._label2.TabIndex = 1
        self._label2.Text = "Shillings:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Yellow
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 182)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(145, 34)
        self._label3.TabIndex = 2
        self._label3.Text = "Pence:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Yellow
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 250)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(145, 34)
        self._label4.TabIndex = 3
        self._label4.Text = "Decimal pounds:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Aquamarine
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(225, 250)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(148, 34)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(225, 41)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(148, 20)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(225, 115)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(148, 20)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(225, 191)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(148, 20)
        self._textBox3.TabIndex = 7
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Transparent
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 305)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(168, 34)
        self._button1.TabIndex = 8
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Transparent
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(205, 305)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(168, 34)
        self._button2.TabIndex = 9
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Transparent
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(13, 345)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(360, 34)
        self._button3.TabIndex = 10
        self._button3.Text = "Calculate"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self.ClientSize = System.Drawing.Size(399, 389)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Po = float(self._textBox1.Text)
        Sh = float(self._textBox2.Text)
        Pe = float(self._textBox3.Text)
        DePo = round(Po + ((Sh / 20) + (Pe / 240)),2)
        self._label5.Text = str(DePo)
        

    def Button1Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = ""
        
        
    def Button2Click(self, sender, e):
        Application.Exit()