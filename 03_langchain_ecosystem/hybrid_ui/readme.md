# Hybrid UI: Frontend for AI Agents

[Claude.ai Artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) and [OpenAI Canvas](https://openai.com/index/introducing-canvas/) exemplify a hybrid UI approach, merging conversational and graphical user interfaces to enhance user interaction. We will using this Hybrid UI approach to build our AI Agent frontends. 

[Simple Canvas/artifact Example](https://claude.site/artifacts/7b323d27-63f9-4d55-8160-b70a3b3cd89f)

**Claude.ai Artifacts** combines chat-based interactions with interactive, visual elements.

Example: A user might ask Claude to create a vocabulary quiz. The conversation flows naturally, but the output is an interactive quiz, blending text-based and visual interactions seamlessly.

[Claude AI Artifacts: Everything You Need to Know](https://www.youtube.com/watch?v=4oW4PBRqhQs)

[15 Powerful Claude Artifacts Use Cases You Should Try](https://www.youtube.com/watch?v=UA2W4xTqQzs)

[Calude AI Artifacts Hub](https://www.claudeaiartifacts.com/en/)

**OpenAI Canvas** offers a similar hybrid experience, particularly geared towards collaborative work in writing and coding

Example: A developer might work with OpenAI Canvas to debug code. They chat with the AI to identify issues, and then directly edit the code in Canvas, seeing immediate visual feedback and suggestions.

[OpenAI Canvas — Revolutionizing Human-AI Collaboration in Writing and Coding](https://medium.com/@artificialintelligencenews/openai-canvas-revolutionizing-human-ai-collaboration-in-writing-and-coding-02d840d44c90)

## Benefits of Hybrid UIs

**Enhanced Engagement:** Combines the intuitive nature of graphical interfaces with the flexibility of conversational AI.

**Improved Workflow:** Streamlines tasks by allowing seamless transitions between conversation and action.

**Interactivity:** Provides a more immersive and dynamic user experience.

This hybrid approach is transforming how we interact with AI, making it more engaging, productive, and user-friendly. Think of it as having the best of both worlds at your fingertips.



## Developing Hybrid UI For Your AI Agent

### Next.js Development

[Next.js Documentation](https://nextjs.org/docs)

[How to Build a NextJS MVP using v0, Claude, and Cursor](https://www.youtube.com/watch?v=2qU3SPPojDA)

## Libraries and Articles

**[Open Canvas by LangChain](https://github.com/langchain-ai/open-canvas)**

[Watch: Open Canvas Introduction](https://www.youtube.com/watch?v=TaL7Vfz85vk)

[Open Source AI Artifacts and Code Execution](https://vercel.com/templates/next.js/open-source-ai-artifacts)

[nextArtifacts](https://github.com/etrobot/nextArtifacts)

[Reverse engineering Claude Artifacts](https://www.reidbarber.com/blog/reverse-engineering-claude-artifacts)

[AI Artifacts App: An Open Source Version of Anthropic Artifacts that can Analyze Python Code, Generate HTML/CSS/JS and Next.js Code](https://www.marktechpost.com/2024/07/19/ai-artifacts-app-an-open-source-version-of-anthropic-artifacts-that-can-analyze-python-code-generate-html-css-js-and-next-js-code/)

[Fragments by E2B](https://github.com/e2b-dev/fragments)

Additional References:

[Open Artifacts](https://github.com/13point5/open-artifacts)


Here are some key patterns and considerations for implementing hybrid UIs:

1. Modal Context Switching:
- Toggle between conversation and graphical modes seamlessly
- Maintain context between modes (like the side panel)
- Keep the chat visible while using graphical tools

2. State Management:
- Track both conversation history and graphical state
- Handle transitions between different interaction modes
- Preserve user progress across mode switches

3. UI Integration Patterns:
- Inline previews of graphical content in chat
- Floating/docked panels for tools
- Contextual toolbars that appear when needed
- Drag-and-drop between modes

4. Other Real-World Examples:
- Figma's commenting system: Combines chat with design tools
- Miro's collaboration features: Chat + whiteboard
- GitHub Copilot Chat: Conversation + code editor
- Notion AI: Integrates AI chat with document editing

