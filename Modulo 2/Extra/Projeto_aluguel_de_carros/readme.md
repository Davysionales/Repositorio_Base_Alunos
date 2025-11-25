# 🚗 *Aluguel de Carros*

Uma aplicação web simples desenvolvida com *Python* e *Streamlit* para calcular o valor total de um aluguel de carro com base no modelo escolhido, a quantidade de dias alugados e a quilometragem rodada.  

O sistema exibe o preço final e uma mensagem personalizada junto com a imagem do veículo selecionado.  
Ideal para praticar conceitos de *entrada e saída de dados*, *expressões aritméticas*, *condicionais* e *frontend lowcode* com Streamlit.  

---

## 🧩 *Situação-Problema*

Você foi contratado por uma **locadora de veículos** para desenvolver uma ferramenta prática que auxilie clientes e atendentes no cálculo do valor final de um aluguel de carro.  

A empresa deseja que o sistema:

- Permita selecionar o modelo do veículo;
- Solicite a quantidade de dias alugados e a quilometragem rodada;
- Calcule automaticamente o valor total a pagar (diária + km rodados);
- Exiba uma mensagem personalizada com os detalhes do aluguel e o preço final;
- Mostre a foto do veículo selecionado para facilitar a identificação.

Essa ferramenta ajudará a tornar o atendimento mais rápido, transparente e interativo, permitindo que os clientes compreendam os custos do aluguel antes de fechar o contrato.  

---

## 🎯 *Objetivo Educacional*

- Trabalhar com *entrada de dados* em formulários interativos no Streamlit.  
- Praticar *operações aritméticas* para cálculo de valores.  
- Aplicar *condicionais* para organizar a lógica de cálculo.  
- Explorar o uso de *frontend lowcode* com Streamlit para criar uma aplicação web simples.  

---

## 📝 *Enunciado*

O projeto consiste em uma aplicação web que realiza os seguintes passos:

1. O usuário seleciona o modelo do carro por meio de um `st.selectbox`.  
2. Insere a quantidade de dias e os quilômetros rodados através de campos de texto (`st.text_input`).  
3. O sistema calcula:  
valor_total = (diária * dias) + (0.15 * km)

4. Exibe uma mensagem personalizada com:  
- Modelo do carro escolhido  
- Dias alugados  
- Km rodados  
- Valor total a pagar  

5. Mostra também a imagem do veículo correspondente.  

---

### Exemplo de uso:

1. O usuário seleciona o modelo **Sedan**, informa **3 dias** e **200 km**.  
2. O sistema calcula:  

- Valor de diárias = R\$ 90 * 3 = R\$ 270  
- Valor por km = R\$ 0,15 * 200 = R\$ 30  
- **Total = R$ 300**  

3. Saída esperada:  
Você alugou o modelo Sedan por 3 dias e percorreu 200 km.
O valor total a pagar é R$ 300,00


---

## 💻 *Como executar*

*Pré-requisito*: Python 3.8 ou superior  

### Passos:

1. Clone este repositório ou baixe os arquivos:

```bash
git clone https://github.com/TJfiles/Projeto_2_Aluguel_de_Carros.git
cd Projeto_2_Aluguel_de_Carros
```
2. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
3. Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```

4. Abra o navegador e acesse o endereço fornecido pelo Streamlit (geralmente http://localhost:8501).

Pronto! Agora você pode selecionar o veículo, informar os valores e calcular o total do aluguel. 🎉

--- 

## **🧠 Conceitos trabalhados**
- Entrada de dados com st.selectbox e st.text_input
- Operações aritméticas para cálculo do valor total
- Condicionais (if/elif/else) para organização da lógica
- Exibição dinâmica de mensagens e imagens no Streamlit
- Criação de interfaces web simples com frontend lowcode

---

## **📂 Estrutura do projeto**

A estrutura básica segue o repositório:
```bash
Projeto_2_Aluguel_de_Carros/
├─ app.py                # Arquivo principal do Streamlit
├─ requirements.txt      # Dependências do projeto
├─ logo.png              # Logo do projeto
├─ README.md             # Este arquivo

```

---
## **📝 Licença**

Este projeto está sob a licença MIT — sinta-se à vontade para usar, modificar e distribuir. ✨

---

## **🔧 Tecnologias utilizadas**

- Python 3.x
- Streamlit