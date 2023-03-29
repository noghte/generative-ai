# Generative AI

A coding question from generative AI: ChatGPT vs. Bard vs. Bing Chat.

Tested on 03-29-2023 `(mm-dd-yyyy)`.

**Initial prompt:** Write a code in Python that read notes from a file and plays music. Instead of reading from a "wav" file, read the notes from plain text or a JSON file. You can define the format for the text or JSON file.

## Installation

Assuming conda is installed, run the following commands:

    conda create -n env-genai python=3.10
    conda activate env-genai
    pip install -r requirements.txt

- To run the gpt3.py script, you need to install the alsa library. 
    - On Ubuntu, run `sudo apt -y install alsa-tools`.
    - On Mac: `brew install alsa-lib`
    - On Windows: https://www.alsa-project.org/wiki/Download

## Final results after follow-up questions
1. **Bard:** I'm not trained for coding yet, so I can't help with that right now. I can help you write things, brainstorm ideas, or answer other complex questions. Maybe we can try something like that?

2. **Bing Chat:** [bing.py](bing.py)