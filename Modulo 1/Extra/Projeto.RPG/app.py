import streamlit as st
import random

st.set_page_config(page_title="Mini RPG", page_icon="⚔️")

st.title("⚔️ Mini RPG com Streamlit")

# --- Criar Personagem ---
st.header("📜 Criação de Personagem")
nome = st.text_input("Nome do seu herói:")
classe = st.selectbox("Classe", ["Guerreiro", "Mago", "Arqueiro", "Ladino"])

if classe == "Guerreiro":
    vida = 130
    ataque = 15
elif classe == "Mago":
    vida = 80
    ataque = 40
elif classe == "Arqueiro":
    vida = 100
    ataque = 27
elif classe== "Ladino":
    vida = 95
    ataque = 30

if nome:
    st.success(f"Herói criado: **{nome}** - Classe: {classe} 🛡️")
    st.write(f"Vida: {vida} | Ataque: {ataque}")


st.header("👹 Batalha")

inimigo = st.selectbox('Escola um inimigo para enfrentar: ', ['Tritão🧜🏻', 'Orc 🧌', 'Dragão🐲', 'Esqueleto💀'])
if inimigo == 'Tritão🧜🏻':
    vida_inimigo = 100
    ataque_inimigo = 25
elif inimigo == 'Orc 🧌':
    vida_inimigo = 140
    ataque_inimigo = 15

elif inimigo == 'Dragão🐲':
    vida_inimigo = 200
    ataque_inimigo = 30

elif inimigo == 'Esqueleto💀':
    vida_inimigo = 80
    ataque_inimigo = 20

if st.button('Vamos batalhar!⚔️'):


    round_num = 1

    while vida >= 0 and vida_inimigo >= 0:
        st.write(f'**Turno** {round_num}')

        dano_heroi = random.randint(ataque - 5, ataque + 5)
        vida_inimigo -= dano_heroi
        st.write(f'{nome} atacou {inimigo} e deu {dano_heroi} de dano')

        if vida_inimigo <= 0:
            st.success(f'{nome} derrotou um {inimigo}! 🎉🎉🎉')
            break

        dano_inimigo = random.randint(ataque_inimigo - 5, ataque_inimigo + 5)
        vida -= dano_inimigo
        st.write(f'{inimigo} atacou {nome} e deu {dano_inimigo}')

        if vida <= 0:
            st.error(f'{nome} foi derrotado por um {inimigo}. . . .')
            break

        st.write(f"Vida de {nome}: {vida} | Vida do {inimigo}: {vida_inimigo}")
        st.write("---")
        round_num += 1


