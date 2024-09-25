# AI Music Compositor 

An AI Music Compositor using LangGraph and OpenAI's language models generates custom musical compositions based on user input. The system processes the input through specialized components, each contributing to the final musical piece, which is then converted to a playable MIDI file.

LangGraph orchestrates a workflow that transforms user input into a musical composition, using ChatOpenAI (GPT-4) to generate melody, harmony, and rhythm, which are then style-adapted. The final AI-generated composition is converted to a MIDI file using music21 and can be played back using pygame.

You are going to take this base project and enhance it's functionality.

Note: You are free to use any other LLM APIs as well.