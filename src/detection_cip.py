import re
import pandas as pd
import gradio as gr
from io import StringIO
import tempfile
import os


username = os.getenv('GRADIO_USERNAME', 'default_username')
password = os.getenv('GRADIO_PASSWORD', 'default_password')

def find_unique_numbers(string):
    # This regular expression matches sequences of exactly 7 or 13 digits
    # The word boundaries (\b) ensure that these sequences are not part of longer digit sequences
    pattern = r'\b\d{7}\b|\b\d{13}\b'

    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, string)

    return matches

# Example usage:
example_string = "My numbers are 1234567, 12345678, and 1234567890123."
unique_numbers = find_unique_numbers(example_string)
print("Unique 7 or 13 digit sequences found:", unique_numbers)


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