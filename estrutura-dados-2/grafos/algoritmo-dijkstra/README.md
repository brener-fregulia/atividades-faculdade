# Dijkstra - Alto Vale do Itajai

## Rodar (linux - CachyOS/Arch-Based)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

O menor caminho pode ser calculado por distancia ou tempo.
O NetworkX usa Dijkstra quando `weight` e `method="dijkstra"` sao informados.
