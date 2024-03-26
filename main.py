import os
import discord
from discord.ext import commands
import pandas as pd
from balance import balance
import re
from util import tabla_misiones, barra_de_carga
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$misiones ', intents=intents)
cols = ['Numero', 'Mision', 'Valor', 'Saldo']
df = pd.DataFrame(columns = cols)
misiones = tabla_misiones(tabla_misiones = df)


@bot.command()
async def test(ctx, arg):
    await ctx.send(barra_de_carga(int(arg)))

@bot.command()
async def add(ctx, *, arg):
    global tabla_misiones
    nombre = re.findall(r'\b[a-zA-Z]+\b', arg)
    nombre = ' '.join(nombre)
    valor = re.findall(r'\b\d+\b', arg)
    valor = ' '.join(valor)
    tabla_misiones = misiones.nueva_mision(nombre=nombre,valor=valor)
    texto_df = ''
    for idx, cols in enumerate(tabla_misiones.Mision):
        total = tabla_misiones.Valor.iloc[idx]
        saldo = tabla_misiones.Saldo.iloc[idx]
        texto_df += f'{idx+1}. {cols} ${tabla_misiones.Valor.iloc[idx]}, Saldo: ${saldo} {barra_de_carga(saldo)}\n'
    #texto_df += f'test: {tabla_misiones}'
    embed = discord.Embed(title='Misiones',
                          description= texto_df,
                          color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def deposito(ctx, numero_mision: int, valor_deposito: int):
    pos = tabla_misiones['Numero'] == numero_mision
    pos_mision = tabla_misiones.loc[pos]
    saldo = balance(int(pos_mision.Valor.iloc[0]))
    deposito = saldo.deposito(valor_deposito=int(valor_deposito))
    text = f'Se deposita {valor_deposito} para mision {numero_mision} con valor de {pos_mision.Valor.iloc[0]} saldo actual de la mision {saldo.saldo_actual} lleva un {saldo.porcentaje:.2f}%'
    embed = discord.Embed(title='Deposito',
                          description= text,
                          color=0x00ff00)
    tabla_misiones['Saldo'].loc[pos] = saldo.saldo_actual
    await ctx.send(embed=embed)


"""
TODO:
$mision add [nombre misión] [precio] -> ingresa misión a la lista
$mision delete [numero] -> borra misión
$mision deposito [nr.mision] [valor deposito] -> suma saldo a la misión 
$mision stats -> barra de progreso
"""

bot.run('token here')
