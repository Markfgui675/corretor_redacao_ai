import google.generativeai as genai
from corretor_ia.models import RedacaoComentario
import textwrap
import pathlib
import markdown
from IPython.display import display
from IPython.display import Markdown
from decouple import config
from django.contrib.auth.models import User
from corretor_ia.inteligencia.system_instruction import system_instruction

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def corretor_redacao(redacao: str, user: User) -> RedacaoComentario:

    genai.configure(api_key=config('api_key'))

    # Set up the model
    generation_config = {
        "temperature": 0.95,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        safety_settings=safety_settings,
        system_instruction=system_instruction
    )

    response = model.generate_content(redacao)
    response = to_markdown(response.text)
    response = markdown.markdown(response.data)

    comentario = RedacaoComentario.objects.create(comentario=str(response))

    user.avaliacoes.add(comentario)
    comentario.avaliacoes.add(user)

    return comentario
