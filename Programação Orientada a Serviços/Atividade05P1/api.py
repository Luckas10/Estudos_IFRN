from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI(title="API de Pedidos")

df = pd.read_csv("pedidos.csv", sep=";", dtype=str, encoding="utf-16")
df.columns = df.columns.str.strip()
if "IdPedido" not in df.columns:
    raise Exception("⚠️ Coluna 'IdPedido' não encontrada no CSV.")

df.set_index("IdPedido", inplace=True)

@app.get("/pedido/{id_pedido}")
def get_pedido(id_pedido: str):
    if id_pedido in df.index:
        return df.loc[id_pedido].dropna().to_dict()
    else:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
