import streamlit as st


st.sidebar.image('logo.png')
st.sidebar.title('Instituto de Medicina e Ciência (IMC)')
st.sidebar.title('IMC')





st.title('Instituto de Medicina e Ciência (IMC)')

st.markdown('---')

peso = st.text_input('Digite quantos kilos você tem?')
altura = st.text_input('Digite qual a sua altura?')
if st.button('Calcular'):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)

    if imc < 18.5:
        st.warning(f'Um simples vento pode te derrubar. Coma mais, pois seu IMC é {imc:.2f}')
        st.image('magrao.png')

    elif imc <= 24.9:
        st.warning(f'É, você está normal, seu imc é {imc:.2f}')
        st.image('normal.png')

    elif imc <= 29.9:
        st.warning(f'Mais saúdavel do que agrião, seu imc é {imc:.2f}')
        st.image('musculoso.png')

    elif imc <= 34.9:
        st.warning(f'Se acalma nos big mac, seu imc é {imc:.2f}')
        st.image('gordinho.png')

    elif imc <= 39.9:
        st.warning(f'Meu Deus, não pula, a terra saíra da orbita do sol. Seu imc é {imc:.2f}')
        st.image('gordo.png')

    else:
        st.warning(f'Seu quarto deve ter 57² metros pra caber você (é sério). Seu imc é {imc:.2f}')
        st.image('gordão.jpg')

