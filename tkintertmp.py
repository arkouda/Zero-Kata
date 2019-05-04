import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
from GifPlayLabel import ImageLabel
from helper import *

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Tic Tac Toe")
        # wh = self.winfo_screenheight()
        # ww = self.winfo_screenwidth() 
        self.geometry('800x600+300+50')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.startFrame = StartPage(parent=self.container, controller=self)
        self.startFrame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage", '',None)
    
    def show_frame(self, page_name, data, frameToDestroy):
        '''Show a frame for the given page name'''
        if StartPage.__name__ == page_name:
            if frameToDestroy : 
                frameToDestroy.destroy()
            self.startFrame.tkraise()
        elif GamePage.__name__ == page_name:
            frame = GamePage(parent=self.container, controller=self, metaData=data)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')

        # tic tac toe logo
        self.imagelogo = Image.open("assets/tictattoo_logo.png")
        self.imagelogotk = ImageTk.PhotoImage(self.imagelogo)

        self.logo_label = tk.Label(self, image = self.imagelogotk, bg='white')
        self.logo_label.photo = self.imagelogotk
        self.logo_label.place(x = 112, y = 10)
        ######################    

        # tic tac toe backdrop image
        self.backdrop_label = ImageLabel(self) 
        self.backdrop_label.place(x = 320, y = 130)
        self.backdrop_label.load('assets/moshedBackdrop.gif')
        ######################    



        ## game Profile (1P or 2P) ##
        self.image1 = Image.open("assets/1p.png")
        self.image1p = ImageTk.PhotoImage(self.image1)

        self.var = tk.IntVar()
        self.var.set(1)
        self.R1 = tk.Radiobutton(self, image = self.image1p, variable=self.var, value=1, bg = 'white' , fg= 'black',
                            padx = 0, pady = 0, highlightbackground = 'white', highlightcolor = 'white',
                            command = self.changeGamePlay)
        self.R1.photo = self.image1p
        self.R1.place(x= 50,y=150, width = 100, height= 70)        
        
        self.image2 = Image.open("assets/2p.png")
        self.image2p = ImageTk.PhotoImage(self.image2)

        self.R2 = tk.Radiobutton(self, image = self.image2p, variable=self.var, value=2, bg = 'white' , fg= 'black',
                            padx = 0, pady = 0,highlightbackground = 'white', highlightcolor = 'white',
                            command = self.changeGamePlay)
        self.R2.photo = self.image2p
        self.R2.place(x= 200,y=150, width = 100, height = 70)        
        ###############################

        ## Player 1 Area ##
        self.player1var = tk.StringVar()
        self.player1var.set('Player')
        self.player1_label = tk.Label(self, textvariable = self.player1var, bg='white', fg='black')
        self.player1_label.place(x=50, y=250)

        self.player1_entry = tk.Entry(self, bg= 'white',fg='black')
        self.player1_entry.place(x=150,y=250,width = 140)
        ###################

        vs_label = tk.Label(self, text ='vs',font=("Helvetica",20), bg='white', fg='black')
        vs_label.place(x=205, y=280)
        
        ## Player 2 Area ##
        self.player2var = tk.StringVar()
        self.player2var.set('CPU')

        self.player2_label = tk.Label(self, textvariable = self.player2var, bg='white', fg='black')
        self.player2_label.place(x=50, y=325)

        self.player2_entry = tk.Entry(self, bg= 'white',fg='black')

        self.cpuvar = tk.IntVar()
        self.cpuvar.set(1)
        self.noob_radio = tk.Radiobutton(self, text ="Noob", variable=self.cpuvar, value=1, bg='white', fg='black'
                                        , highlightbackground = 'white', highlightcolor = 'white')
        self.pro_radio = tk.Radiobutton(self, text ="Pro", variable=self.cpuvar, value=2,bg='white', fg='black'
                                        , highlightbackground = 'white', highlightcolor = 'white' )
        self.noob_radio.place(x=150, y=325)
        self.pro_radio.place(x=230, y=325)
        ###########################

        ## Grid size selection ##
        grid_label = tk.Label(self, text ='Grid Size', bg='white', fg='black')
        grid_label.place(x=50, y=380)

        self.gridvar = tk.StringVar(self)
        self.gridvar.set('  3 x 3  ')
        choices = {'  5 x 5  ','  3 x 3  ', '  4 x 4  '}

        gridDropDown = tk.OptionMenu(self, self.gridvar, *choices)
        gridDropDown.config(bg='white', fg='black')
        gridDropDown.place(x = 150, y=375)
        ############################

        ## Submit Button ##
        self.submit_button = tk.Button(self, text='Start', command=self.submitFunction)
        self.submit_button.place(x= 120, y=440)
        ############################

        ## Message label ##
        self.messagevar = tk.StringVar()
        self.message_label = tk.Label(self, textvariable=self.messagevar, bg='white')
        self.message_label.place(x=50, y=500)
        #########################
        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))

    def changeGamePlay(self):
        if self.var.get() == 1 :
            self.player1var.set('Player')
            self.player2var.set('CPU')
            self.player2_entry.place_forget()
            self.noob_radio.place(x=150, y=325)
            self.pro_radio.place(x=230, y=325)
            self.messagevar.set('')
        else :
            self.player1var.set('Player 1')
            self.player2var.set('Player 2')
            self.player2_entry.place(x=150,y=325, width = 140)
            self.noob_radio.place_forget()
            self.pro_radio.place_forget()
            self.messagevar.set('')

    def submitFunction(self):
        gridMetaData = {
            "playerCount" : 0,
            "player1" : "",
            "player2" : "",
            "gridSize": ""
        }  
        if self.var.get() == 1 :
            if self.player1_entry.get() == '':
                self.messagevar.set('Please enter Player name !!')
                return
            else:
                gridMetaData["playerCount"] = 1
                gridMetaData["player1"] = self.player1_entry.get().upper()
                gridMetaData["player2"] = self.cpuvar.get()
                gridMetaData["gridSize"] = (self.gridvar.get())[2]
                self.resetStartDisp()
        else:
            if self.player1_entry.get() == '' or self.player2_entry.get() == '':
                self.messagevar.set('Please enter Players name !!')
                return
            else:
                gridMetaData["playerCount"] = 2
                gridMetaData["player1"] = self.player1_entry.get().upper()
                gridMetaData["player2"] = self.player2_entry.get().upper()
                gridMetaData["gridSize"] = (self.gridvar.get())[2]
                self.resetStartDisp()
        self.controller.show_frame("GamePage",gridMetaData,None)

    def resetStartDisp(self):
        self.gridvar.set('  3 x 3  ')
        self.player1_entry.delete(0, 'end')
        self.player2_entry.delete(0, 'end')
        self.cpuvar.set(1)
        self.var.set(1)
        self.changeGamePlay()

class GamePage(tk.Frame):

    def __init__(self, parent, controller,metaData):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')

        ## Environment Variables ##
        self.chance = 'x'
        self.io = ImageTk.PhotoImage(Image.open("assets/"+metaData["gridSize"]+"o.png"))
        self.ix = ImageTk.PhotoImage(Image.open("assets/"+metaData["gridSize"]+"x.png"))
        self.metaData = metaData
        self.player1Wins = tk.IntVar()
        self.player1Wins.set(0)
        self.player2Wins = tk.IntVar()
        self.player2Wins.set(0)
        self.drawGames = tk.IntVar()
        self.drawGames.set(0)
        self.resetGameFlag = 0
        self.celebrationText = tk.StringVar()
        #########################
        
        ## tic tac toe logo ##
        imagelogotk = ImageTk.PhotoImage(Image.open("assets/tictattoo_logo.png"))
        logo_label = tk.Label(self, image = imagelogotk, bg='white')
        logo_label.photo = imagelogotk
        logo_label.place(x = 112, y = 10)
        ################################

        ## tic tac toe Tiles ##
        self.numberOfTiles = int(metaData["gridSize"])
        self.gridMatrix = [['' for _ in range(self.numberOfTiles)] for _ in range(self.numberOfTiles)]
        whOfTile = 450 // self.numberOfTiles
        self.buttonMatrix = []
        for i in range(self.numberOfTiles):
            buttons = []
            for j in range(self.numberOfTiles):
                button = tk.Button(self,bg='white',highlightbackground='#005280',command =lambda x=i,y=j: self.buttonController(x,y))
                button.place(x= j*whOfTile+25 ,y=130+i*whOfTile+5,width=whOfTile-10,height=whOfTile-10)
                buttons.append(button)
            self.buttonMatrix.append(buttons) 
        ####################################

        ##  Score Area ##
        pn_label = tk.Label(self,text='Player',bg='white',fg='black',font=controller.title_font)
        pn_label.place(x=540,y=180)

        pn_label = tk.Label(self,text='Wins',bg='white',fg='black',font=controller.title_font)
        pn_label.place(x=700,y=180)
        
        arrow_imageTk = ImageTk.PhotoImage(Image.open("assets/arrow.png"))
        self.arrow_image = tk.Label(self, image = arrow_imageTk, bg='white')
        self.arrow_image.photo = arrow_imageTk
        self.arrow_image.place(x = 500, y = 230)

        player1Name_Label = tk.Label(self,text=metaData["player1"]+" (X)",bg='white',fg='black',font=controller.title_font)
        player1Name_Label.place(x=540,y=220)

        player1Wins_Label = tk.Label(self,textvariable=self.player1Wins,bg='white',fg='black',font=controller.title_font)
        player1Wins_Label.place(x=700,y=220)
        player2Name = metaData["player2"]
        if (type(player2Name) == type(int(1))):
            player2Name = "CPU"
        player2Name_Label = tk.Label(self,text= player2Name+" (O)",bg='white',fg='black',font=controller.title_font)
        player2Name_Label.place(x=540,y=250)

        player2Wins_Label = tk.Label(self,textvariable=self.player2Wins,bg='white',fg='black',font=controller.title_font)
        player2Wins_Label.place(x=700,y=250)

        gameDraws_Label = tk.Label(self,text="Draw Games :",bg='white',fg='black')#,font=controller.title_font)
        gameDraws_Label.place(x=560,y=300)

        countDraw_Label = tk.Label(self,textvariable=self.drawGames,bg='white',fg='black')#,font=controller.title_font)
        countDraw_Label.place(x=660,y=300)
        ############################################

        ## Game Control Button Area ##
        newGame_Button = tk.Button(self,text='New Game',command=self.newGame_onclick)
        newGame_Button.place(x=500, y=330)

        resetGame_Button = tk.Button(self,text='Reset Game',command=self.resetGame)
        resetGame_Button.place(x=600, y=330)

        exitGame_Button = tk.Button(self,text='Exit',command=self.exit_onclick)
        exitGame_Button.place(x=710, y=330)
        ########################## 

        ## Celebration Area ##
        self.celebrationText_label = tk.Label(self, textvariable=self.celebrationText, bg='white',fg='black', font=("Symbol", 12))
        self.celebration_label = ImageLabel(self)
        ######################

    def buttonController(self,i,j):
        if self.resetGameFlag == 1:
            self.resetGrid()
            if self.metaData["playerCount"] == 1 and self.chance == 'o':
                if self.metaData["player2"]==1 :
                    [x,y] = noobplayer(self.gridMatrix)
                else:
                    [x,y] = proPlayer(self.gridMatrix,'x','o')
                self.after(1000,self.updateCPUMove,x,y)
            return
        if self.gridMatrix[i][j] == '' :
            if self.metaData["playerCount"] == 2 :
                self.gridMatrix[i][j] = self.chance
                if self.chance == 'x':
                    self.buttonMatrix[i][j].config(image=self.ix)
                    self.chance = 'o'
                    self.arrow_image.place(x = 500, y = 260)
                    if hasPlayerWon(i,j,self.numberOfTiles,self.gridMatrix):
                        self.player1Wins.set(self.player1Wins.get()+1)
                        self.matchWon(self.metaData["player1"])
                        #print(+" has won the match")
                else:
                    self.buttonMatrix[i][j].config(image=self.io)
                    self.chance = 'x'
                    self.arrow_image.place(x = 500, y = 230)
                    if hasPlayerWon(i,j,self.numberOfTiles,self.gridMatrix):
                        self.player2Wins.set(self.player2Wins.get()+1)
                        self.matchWon(self.metaData["player2"])
                        #print(self.metaData["player2"]+" has won the match")
            else :
                if self.chance == 'x':
                    self.gridMatrix[i][j] = 'x'
                    self.buttonMatrix[i][j].config(image=self.ix)
                    self.chance = 'o'
                    self.arrow_image.place(x = 500, y = 260)
                    if hasPlayerWon(i,j,self.numberOfTiles,self.gridMatrix):
                        self.player1Wins.set(self.player1Wins.get()+1) 
                        self.matchWon(self.metaData["player1"])
                        return
                    if not any([any([self.gridMatrix[i][j] == '' for i in range(self.numberOfTiles)]) for j in range(self.numberOfTiles)]) :
                        self.matchDrawn()
                        return
                    if self.metaData["player2"]==1 :
                        [x,y] = noobplayer(self.gridMatrix)
                    else:
                        [x,y] = proPlayer(self.gridMatrix,'o','x')
                    self.after(1000,self.updateCPUMove,x,y)

            if not any([any([self.gridMatrix[i][j] == '' for i in range(self.numberOfTiles)]) for j in range(self.numberOfTiles)]) :
                self.matchDrawn()

    def matchWon(self,playerName):
        self.celebrationText.set("!!"+playerName+" has won !!")
        self.celebrationText_label.place(x = 550, y = 370)
        self.celebration_label.place(x = 530, y = 400)
        self.celebration_label.load('assets/Youwin.gif')
        self.resetGameFlag = 1

    def matchDrawn(self):
        self.celebrationText.set("!! It's a Draw !!")
        self.celebrationText_label.place(x = 550, y = 370)
        self.drawGames.set(self.drawGames.get()+1)
        self.celebration_label.place(x = 530, y = 400)
        self.celebration_label.load('assets/Matchdraw.gif')
        self.resetGameFlag = 1
        return

    def updateCPUMove(self,i,j):
        self.gridMatrix[i][j] = 'o'
        self.arrow_image.place(x = 500, y = 230)
        self.buttonMatrix[i][j].config(image=self.io)
        self.chance = 'x'
        if hasPlayerWon(i,j,self.numberOfTiles,self.gridMatrix):
            self.celebrationText.set("!! "+self.metaData["player1"]+" has lost !!")
            self.celebrationText_label.place(x = 550, y = 370)
            self.player2Wins.set(self.player2Wins.get()+1)
            self.celebration_label.place(x = 530, y = 400)
            self.celebration_label.load('assets/Youlose.gif')
            self.resetGameFlag = 1
            return
        if not any([any([self.gridMatrix[i][j] == '' for i in range(self.numberOfTiles)]) for j in range(self.numberOfTiles)]) :
            self.matchDrawn() 
        return

    def resetGrid(self):
        self.gridMatrix = [['' for _ in range(self.numberOfTiles)] for _ in range(self.numberOfTiles)]
        self.celebration_label.place_forget()
        self.celebrationText_label.place_forget()
        self.resetGameFlag = 0
        for i in range(self.numberOfTiles):
            for j in range(self.numberOfTiles):
                self.buttonMatrix[i][j].config(image='')
    
    def newGame_onclick(self):
        self.celebrationText_label.place_forget()
        self.celebration_label.place_forget()
        self.controller.show_frame("StartPage", '',self)

    def resetGame(self) :
        self.resetGrid()
        self.chance = 'x'
        self.arrow_image.place(x = 500, y = 230)
        self.player1Wins.set(0)
        self.player2Wins.set(0)
        self.drawGames.set(0)
    
    def exit_onclick(self):
        self.controller.destroy()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()