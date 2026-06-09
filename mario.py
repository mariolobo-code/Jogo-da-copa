import tkinter as tk

# ---------------- TIMES ----------------

times = {
    "Brasil": "🇧🇷 Brasil",
    "Marrocos": "🇲🇦 Marrocos",
    "Haiti": "🇭🇹 Haiti",
    "Escócia": "🏴 Escócia"
}

jogos = [
    ("Brasil", "Marrocos"),
    ("Brasil", "Haiti"),
    ("Brasil", "Escócia"),
    ("Marrocos", "Haiti"),
    ("Marrocos", "Escócia"),
    ("Haiti", "Escócia")
]

tabela = {t: {"pts": 0, "gp": 0, "gc": 0} for t in times}
entries = []

# ---------------- CORES PROFISSIONAIS ----------------

BG = "#06121f"
CARD = "#13263d"
ACCENT = "#00eaff"
WHITE = "white"

# ---------------- FUNÇÃO ----------------

def calcular():

    for t in tabela:
        tabela[t] = {"pts": 0, "gp": 0, "gc": 0}

    for i, (t1, t2) in enumerate(jogos):

        try:
            g1 = int(entries[i][0].get() or 0)
            g2 = int(entries[i][1].get() or 0)
        except:
            g1 = 0
            g2 = 0

        tabela[t1]["gp"] += g1
        tabela[t1]["gc"] += g2

        tabela[t2]["gp"] += g2
        tabela[t2]["gc"] += g1

        if g1 > g2:
            tabela[t1]["pts"] += 3
        elif g2 > g1:
            tabela[t2]["pts"] += 3
        else:
            tabela[t1]["pts"] += 1
            tabela[t2]["pts"] += 1

    atualizar()


def atualizar():

    for w in frame_tabela.winfo_children():
        w.destroy()

    lista = []

    for t in tabela:
        pts = tabela[t]["pts"]
        gp = tabela[t]["gp"]
        gc = tabela[t]["gc"]
        sg = gp - gc

        lista.append([times[t], pts, gp, gc, sg])

    lista.sort(key=lambda x: (x[1], x[4]), reverse=True)

    # HEADER
    header = tk.Frame(frame_tabela, bg=BG)
    header.pack(fill="x")

    labels = ["TIME", "PTS", "GP", "GC", "SG"]
    widths = [20, 6, 6, 6, 6]

    for i in range(5):
        tk.Label(
            header,
            text=labels[i],
            width=widths[i],
            bg=BG,
            fg=ACCENT,
            font=("Arial", 12, "bold")
        ).pack(side="left")

    # LINHAS
    for i, l in enumerate(lista):

        if i == 0:
            cor = "#2ecc71"
        elif i == len(lista) - 1:
            cor = "#e74c3c"
        else:
            cor = CARD

        row = tk.Frame(frame_tabela, bg=cor)
        row.pack(fill="x", pady=3)

        tk.Label(row, text=l[0], width=20, bg=cor, fg=WHITE).pack(side="left")
        tk.Label(row, text=l[1], width=6, bg=cor, fg=WHITE).pack(side="left")
        tk.Label(row, text=l[2], width=6, bg=cor, fg=WHITE).pack(side="left")
        tk.Label(row, text=l[3], width=6, bg=cor, fg=WHITE).pack(side="left")
        tk.Label(row, text=l[4], width=6, bg=cor, fg=WHITE).pack(side="left")


# ---------------- JANELA ----------------

janela = tk.Tk()
janela.title("⚽ Copa Pro")
janela.geometry("720x800")
janela.configure(bg=BG)

# TÍTULO ESTILO STADIUM
titulo = tk.Label(
    janela,
    text="🏟️ COPA INTERATIVA PRO",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=ACCENT
)
titulo.pack(pady=15)

# ---------------- JOGOS ----------------

frame_jogos = tk.Frame(janela, bg=BG)
frame_jogos.pack()

for t1, t2 in jogos:

    card = tk.Frame(frame_jogos, bg=CARD, pady=10)
    card.pack(pady=5, fill="x", padx=15)

    tk.Label(card, text=times[t1], width=18, bg=CARD, fg=WHITE, font=("Arial", 11)).pack(side="left")

    e1 = tk.Entry(card, width=4, font=("Arial", 14))
    e1.pack(side="left")

    tk.Label(card, text="  x  ", bg=CARD, fg=ACCENT, font=("Arial", 13, "bold")).pack(side="left")

    e2 = tk.Entry(card, width=4, font=("Arial", 14))
    e2.pack(side="left")

    tk.Label(card, text=times[t2], width=18, bg=CARD, fg=WHITE, font=("Arial", 11)).pack(side="left")

    entries.append((e1, e2))

# BOTÃO PRINCIPAL
tk.Button(
    janela,
    text="⚡ CALCULAR CLASSIFICAÇÃO",
    command=calcular,
    bg=ACCENT,
    fg="black",
    font=("Arial", 13, "bold"),
    padx=10,
    pady=6
).pack(pady=20)

# ---------------- TABELA ----------------

frame_tabela = tk.Frame(janela, bg=BG)
frame_tabela.pack(pady=10)

atualizar()

janela.mainloop()