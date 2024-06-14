import tkinter as tk
from tkinter import messagebox

class BMICalculator:
  def __init__(self, root):
    self.root = root
    self.root.title("Calculadora de IMC")
    
    self.create_widgets()
    
  def create_widgets(self): 
    
    tk.Label(self.root, text="Altura (m):").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(self.root, text="Peso (kg):").grid(row=1, column=0, padx=10, pady=10)
    
    self.entry_altura = tk.Entry(self.root)
    self.entry_altura.grid(row=0, column=1, padx=10, pady=10)
    self.entry_peso = tk.Entry(self.root)
    self.entry_peso.grid(row=1, column=1, padx=10, pady=10)
    
    self.calc_button = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
    self.calc_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    self.result_label = tk.Label(self.root, text="")
    self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
  def calculate_bmi(self):
    try:
      altura = float(self.entry_altura.get())
      peso = float(self.entry_peso.get())
      imc = peso / (altura ** 2)
      self.result_label.config(text=f"Seu IMC é : {imc:.2f}")
      self.show_bmi_category(imc)
    except ValueError:
      messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")
      
  def show_bmi_category(self, imc):
    if imc < 18.5:
      categoria = "Abaixo do peso."
    elif 18.5 <= imc < 24.9:
      categoria = "Peso normal."
    elif 25 <= imc < 29.9:
      categoria = "Sobrepeso."
    else:
      categoria = "Obesidade."
    self.result_label.config(text=f"Seu IMC é: {imc:.2f} - {categoria}")
    
if __name__  == "__main__":
  root = tk.Tk()
  app = BMICalculator(root)
  root.mainloop()
 