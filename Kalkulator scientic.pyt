import tkinter as tk
import math


ekspresi = ""
hasil_terakhir = "0"
memori = 0.0  
def tekan_tombol(num):
    global ekspresi
    if num == "Ans":
        ekspresi = ekspresi + str(hasil_terakhir)
    else:
        ekspresi = ekspresi + str(num)
    persamaan.set(ekspresi)

def hitung_kalkulator():
    global ekspresi, hasil_terakhir
    try:
        persamaan_hitung = ekspresi.replace('×', '*').replace('÷', '/')
        total = str(eval(persamaan_hitung))
        
        if float(total).is_integer():
            total = str(int(float(total)))
        else:
            total = str(round(float(total), 6))
            
        persamaan.set(total)
        hasil_terakhir = total
        ekspresi = total
    except:
        persamaan.set("Error")
        ekspresi = ""

def hapus_semua():
    global ekspresi
    ekspresi = ""
    persamaan.set("0")

def hapus_satu():
    global ekspresi
    ekspresi = ekspresi[:-1]
    if ekspresi == "":
        persamaan.set("0")
    else:
        persamaan.set(ekspresi)

def fungsi_memori(aksi):
    global memori, ekspresi, hasil_terakhir
    try:
        val = float(persamaan.get() if persuasion_valid() else 0)
        if aksi == "M+":
            memori += val
            lbl_status_memori.config(text="M") # Tanda indikator memori aktif di kalkulator real
        elif aksi == "M":
            # Menampilkan isi memori ke layar
            if memori.is_integer():
                ekspresi = str(int(memori))
            else:
                ekspresi = str(round(memori, 6))
            persamaan.set(ekspresi)
    except:
        persamaan.set("Error")
        ekspresi = ""

def persuasion_valid():
    return persuasion.get() and persuasion.get() != "Error"

def hitung_saintifik(fungsi):
    global ekspresi, hasil_terakhir
    try:
        val = float(persamaan.get() if persuasion_valid() else 0)
        
        if fungsi in ["sqrt", "ln", "log"] and val <= 0 if fungsi in ["ln", "log"] else val < 0:
            raise ValueError

        if fungsi == "sqrt":
            hasil = math.sqrt(val)
        elif fungsi == "sin":
            hasil = math.sin(math.radians(val))
        elif fungsi == "cos":
            hasil = math.cos(math.radians(val))
        elif fungsi == "tan":
            hasil = math.tan(math.radians(val))
        elif fungsi == "kuadrat":
            hasil = val * val
        elif fungsi == "kubik":
            hasil = val * val * val
        elif fungsi == "abs":
            hasil = abs(val)
        elif fungsi == "10x":
            hasil = math.pow(10, val)
        elif fungsi == "ln":
            hasil = math.log(val)
        elif fungsi == "log":
            hasil = math.log10(val)
        
        if hasil.is_integer():
            res_str = str(int(hasil))
        else:
            res_str = str(round(hasil, 6))
            
        persamaan.set(res_str)
        hasil_terakhir = res_str
        ekspresi = res_str
    except:
        persamaan.set("Error")
        ekspresi = ""

def ubah_ke_sains1():

    for widget in frame_sains_dinamis.winfo_children():
        widget.destroy()
    
    tombol_sains1 = [
        ('sin', lambda: hitung_saintifik("sin")),
        ('cos', lambda: hitung_saintifik("cos")),
        ('tan', lambda: hitung_saintifik("tan")),
        ('√', lambda: hitung_saintifik("sqrt"))
    ]
    for idx, (teks, perintah) in enumerate(tombol_sains1):
        tk.Button(frame_sains_dinamis, text=teks, font=("Arial", 11, "bold"), command=perintah,
                  bg=BG_SAINS, fg=FG_SAINS, bd=2, relief="raised", height=2, width=6).grid(row=0, column=idx, padx=4, pady=2, sticky="ew")
    
    btn_toggle_sains.config(text="Mode: Sin/Cos/Tan ▾", bg="#a3c68f", fg="#000000")

def ubah_ke_sains2():
   
    for widget in frame_sains_dinamis.winfo_children():
        widget.destroy()
        
    tombol_sains2 = [
        ('ln', lambda: hitung_saintifik("ln")),
        ('log', lambda: hitung_saintifik("log")),
        ('x²', lambda: hitung_saintifik("kuadrat")),
        ('x³', lambda: hitung_saintifik("kubik"))
    ]
    for idx, (teks, perintah) in enumerate(tombol_sains2):
        tk.Button(frame_sains_dinamis, text=teks, font=("Arial", 11, "bold"), command=perintah,
                  bg=BG_SAINS, fg=FG_SAINS, bd=2, relief="raised", height=2, width=6).grid(row=0, column=idx, padx=4, pady=2, sticky="ew")
                  
    btn_toggle_sains.config(text="Mode: Pangkat/Log ▾", bg="#b0c4de", fg="#000000")

def toggle_mode_sains():
   
    global mode_sekarang
    if mode_sekarang == 1:
        ubah_ke_sains2()
        mode_sekarang = 2
    else:
        ubah_ke_sains1()
        mode_sekarang = 1

root = tk.Tk()
root.title("Casio fx-350ES Hybrid Edition")
root.geometry("380x630")
root.configure(bg="#1c1c1c")
root.resizable(False, False)

BG_SAINS = "#2b2b2b"      
FG_SAINS = "#ffffff"
BG_ANGKA = "#d6d6d6"      
FG_ANGKA = "#000000"      
BG_CASIO_GREEN = "#a3c68f" 
FG_CASIO_GREEN = "#000000"
BG_OPERASI = "#4d4d4d"    
FG_OPERASI = "#ffffff"

frame_layar_outer = tk.Frame(root, bg="#1c1c1c", padx=20, pady=10)
frame_layar_outer.pack(fill="x")

lbl_status_memori = tk.Label(frame_layar_outer, text="", font=("Courier New", 10, "bold"), bg="#e6ebd5", fg="#000000")
lbl_status_memori.place(x=35, y=18)

persamaan = tk.StringVar(value="0")
layar = tk.Entry(
    frame_layar_outer, textvariable=persamaan, font=("Courier New", 22, "bold"), 
    bd=0, bg="#e6ebd5", fg="#000000", borderwidth=12, justify="right", relief="sunken"
)
layar.pack(fill="x", ipady=15)

frame_atas_tombol = tk.Frame(root, bg="#1c1c1c", padx=15)
frame_atas_tombol.pack(fill="x")

btn_toggle_sains = tk.Button(frame_atas_tombol, text="Mode: Sin/Cos/Tan ▾", font=("Arial", 9, "bold"), command=toggle_mode_sains, height=2, width=18)
btn_toggle_sains.pack(side="left", padx=4, pady=5)

frame_sains_dinamis = tk.Frame(frame_atas_tombol, bg="#1c1c1c")
frame_sains_dinamis.pack(side="right", fill="x", expand=True)
for i in range(4): frame_sains_dinamis.grid_columnconfigure(i, weight=1)


frame_matriks_tetap = tk.Frame(root, bg="#1c1c1c", padx=15, pady=5)
frame_matriks_tetap.pack(fill="both", expand=True)
for i in range(4): frame_matriks_tetap.grid_columnconfigure(i, weight=1)

tombol_tetap = [

    ('(', 0, 0, lambda: tekan_tombol("("), BG_SAINS, FG_SAINS),     (')', 0, 1, lambda: tekan_tombol(")"), BG_SAINS, FG_SAINS),
    ('M', 0, 2, lambda: fungsi_memori("M"), BG_SAINS, FG_SAINS),    ('M+', 0, 3, lambda: fungsi_memori("M+"), BG_SAINS, FG_SAINS),
    
    ('DEL', 1, 0, hapus_satu, BG_CASIO_GREEN, FG_CASIO_GREEN),     ('AC', 1, 1, hapus_semua, BG_CASIO_GREEN, FG_CASIO_GREEN),
    ('×', 1, 2, lambda: tekan_tombol("×"), BG_OPERASI, FG_OPERASI), ('÷', 1, 3, lambda: tekan_tombol("÷"), BG_OPERASI, FG_OPERASI),
   
    ('7', 2, 0, lambda: tekan_tombol("7"), BG_ANGKA, FG_ANGKA),     ('8', 2, 1, lambda: tekan_tombol("8"), BG_ANGKA, FG_ANGKA),
    ('9', 2, 2, lambda: tekan_tombol("9"), BG_ANGKA, FG_ANGKA),     ('-', 2, 3, lambda: tekan_tombol("-"), BG_OPERASI, FG_OPERASI),
 
    ('4', 3, 0, lambda: tekan_tombol("4"), BG_ANGKA, FG_ANGKA),     ('5', 3, 1, lambda: tekan_tombol("5"), BG_ANGKA, FG_ANGKA),
    ('6', 3, 2, lambda: tekan_tombol("6"), BG_ANGKA, FG_ANGKA),
    
    ('1', 4, 0, lambda: tekan_tombol("1"), BG_ANGKA, FG_ANGKA),     ('2', 4, 1, lambda: tekan_tombol("2"), BG_ANGKA, FG_ANGKA),
    ('3', 4, 2, lambda: tekan_tombol("3"), BG_ANGKA, FG_ANGKA),
    
    ('0', 5, 0, lambda: tekan_tombol("0"), BG_ANGKA, FG_ANGKA),     ('.', 5, 1, lambda: tekan_tombol("."), BG_ANGKA, FG_ANGKA),
    ('Ans', 5, 2, lambda: tekan_tombol("Ans"), BG_OPERASI, FG_OPERASI), ('=', 5, 3, hitung_kalkulator, "#2e6da4", "#ffffff")
]

for (teks, b, k, perintah, warna_bg, warna_fg) in tombol_tetap:
    tk.Button(
        frame_matriks_tetap, text=teks, font=("Arial", 12, "bold"), command=perintah,
        bg=warna_bg, fg=warna_fg, bd=2, relief="raised", cursor="hand2", width=6, height=2
    ).grid(row=b, column=k, padx=4, pady=4, sticky="ew")

tk.Button(
    frame_matriks_tetap, text="+", font=("Arial", 12, "bold"), command=lambda: tekan_tombol("+"),
    bg=BG_OPERASI, fg=FG_OPERASI, bd=2, relief="raised", cursor="hand2", height=4
).grid(row=3, column=3, rowspan=2, padx=4, pady=4, sticky="ew")

mode_sekarang = 1
ubah_ke_sains1()

root.mainloop()
