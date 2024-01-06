import gradio as gr
from detection_cip import *
import os
from io import StringIO
import tempfile
import pandas as pd

username = os.getenv('GRADIO_USERNAME', 'default_username')
password = os.getenv('GRADIO_PASSWORD', 'default_password')


def process_and_download(text):
    # Call the find_unique_numbers function
    numbers = find_unique_numbers(text)
    
    # Create a DataFrame with an additional column with the value 1 for each number
    df = pd.DataFrame({'Number': numbers, 'Value': [1] * len(numbers)})
    
    # Create a temporary file to store the CSV
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w')
    
    # Write the CSV data to the temporary file without the header and with ';' as the delimiter
    df.to_csv(temp_file.name, index=False, header=False, sep=';')
    
    # Close the file so Gradio can read it
    temp_file.close()
    
    # Return the path to the temporary file
    return temp_file.name


# Set up the Gradio interface
iface = gr.Interface(
    fn=process_and_download,
    inputs=gr.Textbox(lines=2, placeholder="Entrer ici l'email ou le texte..."),
    outputs=gr.File(label="Télécharger le CSV des numéros CIP"),
    title="Extraction du numéro CIP",
    description="Entrez du texte et cliquez sur soumettre pour trouver des chaînes uniques de 7 ou 13 chiffres (Code CIP) et les télécharger sous forme de fichier CSV. La quantité est toujours égale à 1."    
)

# Run the interface
iface.launch(auth=(username, password),server_name='0.0.0.0', server_port=7860)