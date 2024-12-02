# OR+HF
Script simple en langage Python au moyen duquel appeler dans le logiciel OpenRefine <https://openrefine.org> par API un modèle de langue déployé sur Hugging Face <https://huggingface.co>. Adaptation d’un script original de Michael Markert <https://github.com/MichaelMarkert/SODa/>.

## Directives :
- Coller ce script dans la fenêtre ouverte en suivant > Edit column > Add column based on this column (OpenRefine).
- Dans le script (url), remplacer {model_name} et {model_lab} par les noms du modèle choisi et du lab qui en est l’auteur.
- Dans le script (api_key), remplacer 'hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' par votre clef d’identification générée dans votre espace d’utilisateur en suivant > Settings > Access Tokens (Hugging Face).
- Dans le script (prompt), remplacer l’invite 'Generate a basic JSON...' par celle de votre choix. Celle-ci peut être écrite en français.
- Dans le script (data), ajuster les valeurs des paramètres 'max_tokens' et 'temperature'.
