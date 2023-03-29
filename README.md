# Generative AI

A coding question from generative AI: ChatGPT vs. Bard vs. Bing Chat.

Tested on 03-29-2023 `(mm-dd-yyyy)`.

**Initial prompt:** Write a code in Python that read notes from a file and plays music. Instead of reading from a "wav" file, read the notes from plain text or a JSON file. You can define the format for the text or JSON file.

## Installation

Assuming conda is installed, run the following commands:

```bash
conda create -n env-genai python=3.10
conda activate env-genai
pip install -r requirements.txt
```

## Final results after follow-up questions
1. **Bard:** _I'm not trained for coding yet, so I can't help with that right now. I can help you write things, brainstorm ideas, or answer other complex questions. Maybe we can try something like that?_

2. **Bing Chat:** [bing.py](bing.py) (example notes: [notes/bing.json](notes/bing.json))

3. **ChatGPT 3.5:** [gpt3.5.py](gpt3.5.py) (example notes: [notes/gpt3.5.json](notes/gpt3.5.json) - it also created [note_map.json](note_map.json)

4. **ChatGPT 4.0:** [gpt4.py](gpt4.0.py) (example notes: [notes/gpt4.json](notes/gpt4.json))