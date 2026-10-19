import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

COR_NO = "#2878D0"
COR_BORDA = "#6FA8E8"
COR_ARESTA = "#777777"
COR_BRANCO = "#FFFFFF"

COR_BUSCA = "#2A9D55"
COR_BORDA_BUSCA = "#75D69A"


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)

        if self.raiz is None:
            self.raiz = novo
            return True

        atual = self.raiz

        while True:
            if valor == atual.valor:
                return False

            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return True

                atual = atual.esquerda

            else:
                if atual.direita is None:
                    atual.direita = novo
                    return True

                atual = atual.direita

    def buscar(self, valor):
        atual = self.raiz

        while atual is not None:
            if valor == atual.valor:
                return atual

            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return None

    def limpar(self):
        self.raiz = None


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Arvore Binaria de Busca")
        self.minsize(1050, 680)
        self.after(0, self._maximizar)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.arvore = ArvoreBinariaBusca()
        self.no_destacado = None

        self._montar_controles()
        self._montar_grafico()
        self.desenhar()

    def _maximizar(self):
        if self.tk.call("tk", "windowingsystem") == "win32":
            self.state("zoomed")
        else:
            self.attributes("-zoomed", True)

    def _montar_controles(self):
        painel = ctk.CTkFrame(
            self,
            width=350,
            corner_radius=0,
        )
        painel.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        painel.grid_propagate(False)

        ctk.CTkLabel(
            painel,
            text="Arvore Binaria\nde Busca",
            font=ctk.CTkFont(
                size=24,
                weight="bold",
            ),
            justify="left",
        ).pack(
            anchor="w",
            padx=22,
            pady=(30, 30),
        )

        ctk.CTkLabel(
            painel,
            text="Valor",
        ).pack(
            anchor="w",
            padx=22,
        )

        self.entrada = ctk.CTkEntry(
            painel,
            width=305,
            height=36,
            placeholder_text="Ex: 50",
        )
        self.entrada.pack(
            padx=22,
            pady=(6, 14),
        )
        self.entrada.bind(
            "<Return>",
            lambda evento: self.inserir(),
        )

        ctk.CTkButton(
            painel,
            text="Inserir",
            width=305,
            height=40,
            command=self.inserir,
        ).pack(
            padx=22,
            pady=(0, 10),
        )

        ctk.CTkButton(
            painel,
            text="Buscar",
            width=305,
            height=40,
            command=self.buscar,
        ).pack(
            padx=22,
            pady=(0, 10),
        )

        ctk.CTkButton(
            painel,
            text="Limpar arvore",
            width=305,
            command=self.limpar,
        ).pack(
            padx=22,
            pady=(0, 20),
        )

        self.resultado = ctk.CTkTextbox(
            painel,
            width=305,
            height=120,
            wrap="word",
            font=("Consolas", 12),
        )
        self.resultado.pack(
            padx=22,
            fill="x",
        )

        self._mostrar("Insira um valor para iniciar a arvore.")

    def _montar_grafico(self):
        frame = ctk.CTkFrame(
            self,
            corner_radius=0,
        )
        frame.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.fig, self.ax = plt.subplots(
            figsize=(10, 7),
            dpi=100,
        )

        self.canvas = FigureCanvasTkAgg(
            self.fig,
            master=frame,
        )

        self.canvas.get_tk_widget().grid(
            row=0,
            column=0,
            sticky="nsew",
        )

    def _mostrar(self, texto):
        self.resultado.configure(
            state="normal",
        )
        self.resultado.delete(
            "1.0",
            "end",
        )
        self.resultado.insert(
            "1.0",
            texto,
        )
        self.resultado.configure(
            state="disabled",
        )

    def inserir(self):
        texto = self.entrada.get().strip()

        try:
            valor = int(texto)
        except ValueError:
            self._mostrar("Digite um numero inteiro valido.")
            return

        if not self.arvore.inserir(valor):
            self._mostrar(f"O valor {valor} ja existe na arvore.")
            return

        self.entrada.delete(0, "end")

        self.no_destacado = None

        self._mostrar(f"Valor {valor} inserido.")

        self.desenhar()

    def buscar(self):
        texto = self.entrada.get().strip()

        try:
            valor = int(texto)
        except ValueError:
            self._mostrar("Digite um numero inteiro valido.")
            return

        encontrado = self.arvore.buscar(valor)

        if encontrado is None:
            self.no_destacado = None
            self._mostrar(f"O valor {valor} nao pertence a arvore.")
        else:
            self.no_destacado = encontrado
            self._mostrar(f"O valor {valor} pertence a arvore.")

        self.desenhar()

    def limpar(self):
        self.arvore.limpar()
        self.no_destacado = None

        self._mostrar("Arvore limpa.")

        self.desenhar()

    def _calcular_posicoes(self):
        posicoes = {}
        coluna = 0

        def percorrer(no, nivel):
            nonlocal coluna

            if no is None:
                return

            percorrer(
                no.esquerda,
                nivel + 1,
            )

            posicoes[no] = (
                coluna,
                -nivel,
            )
            coluna += 1

            percorrer(
                no.direita,
                nivel + 1,
            )

        percorrer(
            self.arvore.raiz,
            0,
        )

        return posicoes

    def _desenhar_no(
        self,
        no,
        posicoes,
    ):
        if no is None:
            return

        x, y = posicoes[no]

        for filho in (
            no.esquerda,
            no.direita,
        ):
            if filho is None:
                continue

            filho_x, filho_y = posicoes[filho]

            self.ax.plot(
                [x, filho_x],
                [y, filho_y],
                color=COR_ARESTA,
                linewidth=2,
                zorder=1,
            )

            self._desenhar_no(
                filho,
                posicoes,
            )

        destacado = no is self.no_destacado

        self.ax.scatter(
            x,
            y,
            s=1800,
            color=COR_BUSCA if destacado else COR_NO,
            edgecolors=COR_BORDA_BUSCA if destacado else COR_BORDA,
            linewidths=2,
            zorder=2,
        )

        self.ax.text(
            x,
            y,
            str(no.valor),
            color=COR_BRANCO,
            fontsize=11,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=3,
        )

    def desenhar(self):
        self.ax.clear()

        self.ax.set_title(
            "Arvore Binaria de Busca",
            fontsize=15,
        )

        if self.arvore.raiz is None:
            self.ax.text(
                0.5,
                0.5,
                "Arvore vazia",
                transform=self.ax.transAxes,
                ha="center",
                va="center",
                fontsize=14,
            )
        else:
            posicoes = self._calcular_posicoes()

            self._desenhar_no(
                self.arvore.raiz,
                posicoes,
            )

            valores_x = [x for x, y in posicoes.values()]

            valores_y = [y for x, y in posicoes.values()]

            self.ax.set_xlim(
                min(valores_x) - 1,
                max(valores_x) + 1,
            )

            self.ax.set_ylim(
                min(valores_y) - 1,
                1,
            )

        self.ax.axis("off")
        self.fig.tight_layout()
        self.canvas.draw_idle()


if __name__ == "__main__":
    ctk.set_appearance_mode("system")

    app = App()
    app.mainloop()
