import customtkinter as ctk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# dados do grafo
CIDADES = {
    "ITU": "Ituporanga",
    "AGR": "Agronomica",
    "ATA": "Atalanta",
    "AUR": "Aurora",
    "CDL": "Chapadao do Lageado",
    "IMB": "Imbuia",
    "PET": "Petrolandia",
    "PNE": "Presidente Nereu",
    "VRA": "Vidal Ramos",
    "AGL": "Agrolandia",
    "TCE": "Trombudo Central",
    "BTR": "Braco do Trombudo",
    "LAU": "Laurentino",
    "PRE": "Pouso Redondo",
    "RDO": "Rio do Oeste",
    "RDS": "Rio do Sul",
    "PGE": "Presidente Getulio",
    "DEM": "Dona Emma",
}

# origem, destino, distancia_km, tempo_min
ARESTAS = [
    ("ITU", "AGR", 37.8, 57),
    ("ITU", "ATA", 20.8, 19),
    ("ITU", "AUR", 13.9, 18),
    ("ITU", "CDL", 25.5, 39),
    ("ITU", "IMB", 25.6, 28),
    ("ITU", "PET", 19.1, 21),
    ("ITU", "PNE", 37.6, 59),
    ("ITU", "VRA", 31.7, 34),
    ("AGR", "ATA", 25.6, 37),
    ("AGR", "AGL", 25.5, 30),
    ("AGR", "TCE", 11.5, 13),
    ("AGR", "LAU", 9.0, 12),
    ("AGR", "AUR", 17.2, 32),
    ("AGL", "BTR", 13.8, 24),
    ("AGL", "TCE", 14.1, 17),
    ("AGL", "ATA", 6.4, 8),
    ("AGL", "PET", 31.5, 45),
    ("ATA", "PET", 21.0, 38),
    ("PET", "CDL", 28.1, 47),
    ("TCE", "BTR", 14.4, 17),
    ("TCE", "LAU", 19.0, 22),
    ("TCE", "PRE", 18.4, 18),
    ("TCE", "RDO", 25.6, 28),
    ("BTR", "PRE", 18.4, 22),
    ("LAU", "RDO", 8.5, 11),
    ("PRE", "RDO", 24.3, 32),
    ("VRA", "IMB", 19.8, 23),
    ("VRA", "PNE", 26.1, 49),
    ("RDS", "AGR", 10.7, 13),
    ("RDS", "AUR", 14.0, 17),
    ("RDS", "LAU", 13.3, 19),
    ("RDS", "PGE", 38.1, 49),
    ("PGE", "LAU", 29.2, 52),
    ("PGE", "RDO", 49.8, 78),
    ("PGE", "DEM", 16.1, 20),
    ("DEM", "RDO", 49.3, 76),
]

# posicoes aproximadas do trabalho
POS = {
    "DEM": (-1.1, 3.5),
    "PGE": (-0.7, 2.7),
    "RDO": (-2.1, 2.0),
    "LAU": (-0.7, 1.8),
    "RDS": (0.7, 1.5),
    "PRE": (-3.2, 0.9),
    "TCE": (-1.5, 0.6),
    "BTR": (-2.4, 0.0),
    "AGR": (-0.5, 0.4),
    "AUR": (1.4, 0.1),
    "AGL": (-1.9, -1.3),
    "ATA": (-0.7, -0.8),
    "PET": (0.0, -2.1),
    "ITU": (2.2, -1.5),
    "CDL": (1.7, -2.7),
    "IMB": (3.4, -1.6),
    "PNE": (3.2, 0.5),
    "VRA": (4.1, -0.4),
}

GRAFO = nx.Graph()
for sigla, nome in CIDADES.items():
    GRAFO.add_node(sigla, nome=nome)

for origem, destino, distancia, tempo in ARESTAS:
    GRAFO.add_edge(
        origem,
        destino,
        distancia=distancia,
        tempo=tempo,
    )


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dijkstra - Alto Vale do Itajai")
        self.geometry("1250x780")
        self.minsize(1050, 680)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.caminho = []
        self._montar_controles()
        self._montar_grafo()
        self.desenhar()

    def _montar_controles(self):
        painel = ctk.CTkFrame(self, width=310, corner_radius=0)
        painel.grid(row=0, column=0, sticky="nsew")
        painel.grid_propagate(False)

        ctk.CTkLabel(
            painel,
            text="Dijkstra\nAlto Vale do Itajai",
            font=ctk.CTkFont(size=24, weight="bold"),
            justify="left",
        ).pack(anchor="w", padx=22, pady=(26, 24))

        opcoes = [f"{sigla} - {nome}" for sigla, nome in CIDADES.items()]

        ctk.CTkLabel(painel, text="Origem").pack(anchor="w", padx=22)
        self.origem = ctk.CTkComboBox(
            painel, values=opcoes, width=265, state="readonly"
        )
        self.origem.pack(padx=22, pady=(6, 16))
        self.origem.set("ITU - Ituporanga")

        ctk.CTkLabel(painel, text="Destino").pack(anchor="w", padx=22)
        self.destino = ctk.CTkComboBox(
            painel, values=opcoes, width=265, state="readonly"
        )
        self.destino.pack(padx=22, pady=(6, 16))
        self.destino.set("RDO - Rio do Oeste")

        ctk.CTkLabel(painel, text="Criterio").pack(anchor="w", padx=22)
        self.criterio = ctk.CTkSegmentedButton(
            painel, values=["Distancia", "Tempo"], width=265
        )
        self.criterio.pack(padx=22, pady=(6, 18))
        self.criterio.set("Distancia")

        ctk.CTkButton(
            painel,
            text="Calcular melhor caminho",
            width=265,
            height=40,
            command=self.calcular,
        ).pack(padx=22, pady=(0, 10))

        ctk.CTkButton(
            painel,
            text="Limpar",
            width=265,
            command=self.limpar,
        ).pack(padx=22, pady=(0, 20))

        self.resultado = ctk.CTkTextbox(
            painel,
            width=265,
            height=245,
            wrap="word",
            font=("Consolas", 12),
        )
        self.resultado.pack(padx=22, fill="x")
        self._mostrar("Selecione origem, destino e criterio.")

    def _montar_grafo(self):
        frame = ctk.CTkFrame(self, corner_radius=0)
        frame.grid(row=0, column=1, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.fig, self.ax = plt.subplots(figsize=(10, 7), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def _sigla(self, valor):
        return valor.split(" - ", 1)[0]

    def _mostrar(self, texto):
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", texto)
        self.resultado.configure(state="disabled")

    def calcular(self):
        origem = self._sigla(self.origem.get())
        destino = self._sigla(self.destino.get())

        if origem == destino:
            self._mostrar("Origem e destino precisam ser diferentes.")
            return

        atributo = "distancia" if self.criterio.get() == "Distancia" else "tempo"

        # networkx usa dijkstra quando ha peso
        caminho = nx.shortest_path(
            GRAFO,
            origem,
            destino,
            weight=atributo,
            method="dijkstra",
        )

        distancia = sum(
            GRAFO[a][b]["distancia"]
            for a, b in zip(caminho, caminho[1:])
        )
        tempo = sum(
            GRAFO[a][b]["tempo"]
            for a, b in zip(caminho, caminho[1:])
        )

        self.caminho = caminho
        rota = " -> ".join(CIDADES[cidade] for cidade in caminho)

        self._mostrar(
            f"Criterio: {self.criterio.get()}\n\n"
            f"Rota:\n{rota}\n\n"
            f"Distancia: {distancia:.1f} km\n"
            f"Tempo: {tempo} min"
        )
        self.desenhar()

    def limpar(self):
        self.caminho = []
        self._mostrar("Selecione origem, destino e criterio.")
        self.desenhar()

    def desenhar(self):
        self.ax.clear()

        nx.draw_networkx_edges(
            GRAFO,
            POS,
            ax=self.ax,
            edge_color="#9A9A9A",
            width=1.7,
        )

        if len(self.caminho) > 1:
            nx.draw_networkx_edges(
                GRAFO,
                POS,
                ax=self.ax,
                edgelist=list(zip(self.caminho, self.caminho[1:])),
                edge_color="#D62828",
                width=4,
            )

        cores = []
        for no in GRAFO.nodes:
            if self.caminho and no == self.caminho[0]:
                cores.append("#2A9D55")
            elif self.caminho and no == self.caminho[-1]:
                cores.append("#2878D0")
            else:
                cores.append("#111111")

        nx.draw_networkx_nodes(
            GRAFO,
            POS,
            ax=self.ax,
            node_color=cores,
            node_size=150,
        )

        nx.draw_networkx_labels(
            GRAFO,
            POS,
            ax=self.ax,
            labels={sigla: sigla for sigla in CIDADES},
            font_size=8,
            font_color="white",
        )

        # distancia e tempo ficam sempre visiveis
        labels = {
            (a, b): f"{d['distancia']:.1f} km\n{d['tempo']} min"
            for a, b, d in GRAFO.edges(data=True)
        }
        nx.draw_networkx_edge_labels(
            GRAFO,
            POS,
            ax=self.ax,
            edge_labels=labels,
            font_size=6,
            rotate=False,
            bbox={
                "facecolor": "white",
                "edgecolor": "none",
                "alpha": 0.75,
                "pad": 0.5,
            },
        )

        self.ax.set_title("Grafo do Alto Vale do Itajai", fontsize=15)
        self.ax.axis("off")
        self.fig.tight_layout()
        self.canvas.draw_idle()


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    app = App()
    app.mainloop()
