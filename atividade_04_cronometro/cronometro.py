import tkinter as tk
from tkinter import messagebox

class Stopwatch:
   def __init__(self):
      self.root = tk.Tk()
      self.root.title("Cronômetro")
      
      self.hours = 0
      self.minutes = 0
      self.secunds = 0
      self.running = False
      
      self.time_label = tk.Label(self.root, text=self.format_time(), font=("Helvetica", 48))
      self.time_label.pack()
      
      self.start_button = tk.Button(self.root, text="Iniciar", command=self.start)
      self.start_button.pack(side="left")
      
      self.stop_button = tk.Button(self.root, text="Parar", command=self.stop)
      self.stop_button.pack(side="left")
      
      self.reset_button = tk.Button(self.root, text="Resetar", command=self.reset)
      self.reset_button.pack(side="left")
      
   def format_time(self):
      return f"{self.hours:02}:{self.minutes:02}:{self.secunds:02}"
   
   def update_time(self):
      if self.running:
         self.secunds += 1
         if self.secunds == 60:
            self.secunds = 0
            self.minutes += 1
            if self.minutes == 60:
               self.minutes = 0
               self.hours += 1
         self.time_label.config(text=self.format_time())
         self.root.after(1000, self.update_time)
         
   def start(self):
      if not self.running:
         self.running = True
         self.update_time()
         
   def stop (self):
      self.running = False
      
   def reset(self):
      self.running = False
      self.hours = 0
      self.minutes = 0
      self.secunds = 0
      self.time_label.config(text=self.format_time())
      
   def run(self):
      self.root.mainloop()
      
if __name__ == "__main__":
   stopwatch = Stopwatch()
   stopwatch.run()