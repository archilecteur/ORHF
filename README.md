# OR+HF

Un script Python permettant d’appeler dans le logiciel [OpenRefine](https://openrefine.org) via API un modèle de language (LLM) déployé sur [Hugging Face](https://huggingface.co). Adaptation d’un script original de [Michael Markert](https://github.com/MichaelMarkert/SODa/).

## Directives :
- Coller ce script dans la fenêtre ouverte en suivant > Edit column > Add column based on this column (OpenRefine).
- Dans le script (url), remplacer {model_name} et {model_lab} par les noms du modèle choisi et du lab qui en est l’auteur.
- Dans le script (api_key), remplacer 'hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' par votre clef d’identification générée dans votre espace d’utilisateur en suivant > Settings > Access Tokens (Hugging Face).
- Dans le script (prompt), remplacer l’invite 'Generate a basic JSON...' par celle de votre choix. Celle-ci peut être écrite en français.
- Dans le script (data), ajuster les valeurs des paramètres 'max_tokens' et 'temperature'.

***

A Python script for calling a language model (LLM) deployed on [Hugging Face](https://huggingface.co) in [OpenRefine](https://openrefine.org) via API. Adapted from an original script by [Michael Markert](https://github.com/MichaelMarkert/SODa/).

## Instructions:
- Paste this script into the following window > Edit column > Add column based on this column (OpenRefine).
- In the script (url), replace {model_name} and {model_lab} with the names of the chosen model and the lab that created it.
- In the script (api_key), replace 'hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' with your identification key generated in your user space by following > Settings > Access Tokens (Hugging Face).
- In the script (prompt), replace the 'Generate a basic JSON...' prompt with the one of your choice.
- In the script (data), adjust the values of the 'max_tokens' and 'temperature' parameters.
