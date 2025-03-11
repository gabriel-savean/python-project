import streamlit as st
import requests
from groq import Groq

# Configuration de la page
st.set_page_config(page_title=" Projet Python - Chatbot IT", page_icon="🤖", layout="wide")

# Définition directe de la clé API Groq
groq_api_key = "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"

# Initialisation du client Groq
client = Groq(api_key=groq_api_key)


# Fonction pour interroger l'API Groq
def query_groq(question):
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Contexte\nTu es un assistant spécialisé en transformation digitale et en gestion de projets IT. Ton objectif est de répondre de manière précise, concise et professionnelle aux questions des utilisateurs sur ces sujets.\n\nRègles du chatbot :\nRéponds en 1 à 3 phrases maximum pour être clair et efficace.\nUtilise un ton professionnel, structuré et neutre.\nNe fournis pas d'informations non vérifiées ou spéculatives.\nSi une question est hors sujet, dis simplement : \"Je suis spécialisé en transformation digitale et gestion IT. Pouvez-vous reformuler votre question ?\"."
            },
            {"role": "user", "content": question}
        ],
        "temperature": 1,
        "max_completion_tokens": 1024,
        "top_p": 1,
        "stream": False
    }

    completion = client.chat.completions.create(**payload)
    return completion.choices[0].message.content if completion.choices else "Désolé, je n'ai pas la réponse."


# Interface utilisateur Streamlit améliorée
st.markdown(
    """
    <style>
        .chat-container {
            max-width: 800px;
            margin: auto;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }
        .message {
            padding: 12px 16px;
            border-radius: 20px;
            margin-bottom: 10px;
            max-width: 80%;
            word-wrap: break-word;
            display: inline-block;
            font-size: 16px;
        }
        .user-message {
            background-color: #0984fc; /* Couleur de fond pour les messages utilisateur */
            color: #ffffff; /* Couleur du texte pour les messages utilisateur */
            align-self: flex-end; /* Alignement à droite */
            text-align: left;
            margin-left: auto; /* Pousse le message vers la droite */
            margin-right: 0;
        }
        .bot-message {
            background-color: #EAEAEA; /* Couleur de fond pour les messages du chatbot */
            color: #000; /* Couleur du texte pour les messages du chatbot */
            align-self: flex-start; /* Alignement à gauche */
            text-align: left;
            margin-left: 0;
            margin-right: auto; /* Pousse le message vers la gauche */
        }
        @media (prefers-color-scheme: dark) {
            .user-message {
                background-color: #0984fc; /* Couleur de fond pour les messages utilisateur en mode sombre */
                color: #ffffff;
            }
            .bot-message {
                background-color: #424242; /* Couleur de fond pour les messages du chatbot en mode sombre */
                color: #ffffff;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Chatbot FAQ IT")
st.write("Posez vos questions sur la transformation digitale et les projets IT !")

# Historique des messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Affichage des messages avec alignement correct et largeur adaptée
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    role, text = msg
    class_name = "user-message" if role == "user" else "bot-message"
    st.markdown(f"<div class='message {class_name}'>{text}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Champ de saisie utilisateur
question = st.text_input("💬 Posez votre question :", key="chat_input")
if st.button("Envoyer") and question:
    st.session_state["messages"].append(("user", question))
    response = query_groq(question)
    st.session_state["messages"].append(("bot", response))
    st.rerun()

# Ajout d'une section d'exemples de questions
st.markdown("---")
st.subheader("💡 Exemples de questions :")
st.write("- Qu'est-ce que le cloud computing ?")
st.write("- Quels sont les avantages de l'automatisation en entreprise ?")
st.write("- Comment l'IA transforme-t-elle le secteur bancaire ?")

# Footer
st.markdown("---")
st.markdown("*Chatbot alimenté par l'API Groq* 🚀")
st.markdown("Projet python réalisé par [Gabriel Savean](https://www.linkedin.com/in/gabrielsavean/) pour appuyer sa candidature au poste de Consultant Stagiaire IT & Business Transformation Programs chez KPMG - Connected Tech.")
st.subheader("📌 Technologies utilisées")
st.markdown("""
- **Streamlit** → Interface utilisateur interactive 💻  
- **Groq API (Llama model)** → Génération de réponses intelligentes 🧠  
- **Requests** → Communication avec l'API Groq 🔗  
- **HTML / CSS (via st.markdown)** → Personnalisation de l'affichage 🎨  
""")

