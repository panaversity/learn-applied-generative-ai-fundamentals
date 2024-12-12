## **Project 01: User-Chat-Interactions**

---

### **Objective:**
Make your chat-agent developed in 00_chat_agent smarter by allowing it to:
1. Get help from a human assistant when needed.
2. Pause and ask the user for extra information if something is unclear.
3. Personalize its answers using long-term memory.
4. Offloading conversation to Human

**Note:** This project builds on the skills learned in Project 00 and prepares you for advanced Agentic AI features like dynamic workflows and user personalization.

---

### **Requirements:**

1. **Human Assistant Interrupts (Static Interrupts):**
   - Add a feature where your chatbot can **pause** and connect to a human assistant if needed.
   - This can be a **static interrupt**—you decide when the chatbot needs help from a human.
   - Example: If the chatbot can’t answer a question or doesn’t have enough information, it stops and sends the question to a human for assistance.

**Reference Material:**
- [Static Breakpoints](https://github.com/panaversity/learn-agentic-ai/blob/main/12_langchain_ecosystem/langgraph/course-notebooks/module-3/2_breakpoints.ipynb)

2. **Ask the User for More Information (Dynamic Interrupts):**
   - Make the chatbot smart enough to **pause its workflow** and ask the user for more information when it’s confused.
   - Steps:
     - Add a **decision step** after each user message.
     - If the chatbot detects a question or needs more details, it pauses and asks the user to clarify.
     - The user can:
       - **Answer the question** to help the chatbot.
       - **Skip the question** and let the chatbot guess the best answer.

**Reference Material:**
- [Dynamic Breakpoints](https://github.com/panaversity/learn-agentic-ai/blob/main/12_langchain_ecosystem/langgraph/course-notebooks/module-3/4_dynamic_breakpoints.ipynb)
- [Editing State](https://github.com/panaversity/learn-agentic-ai/blob/main/12_langchain_ecosystem/langgraph/course-notebooks/module-3/3_edit_state_human_feedback.ipynb)

3. **(Optional) Personalize Using Long-Term Memory:**
   - Use a memory system to **save important details** about the user.
   - Examples of what to remember:
     - Preferences (e.g., favorite subjects, preferred clothing styles).
     - Recurring needs (e.g., study schedules, favorite recipes).
   - Use this memory to give **better and more personal answers** over time.

**Tools:** Use **LangGraph Memory Store** to save and retrieve user data.

**Reference Material:**
- [Concept](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory)
- [Memory Template](https://github.com/langchain-ai/memory-template)

*Note:* This is an optional step. Focus on completing the first two requirements before attempting long-term memory integration if you feel confident.

---

### **Deliverables:**
- A working chatbot prototype with:
  1. Human assistant interrupts.
  2. Dynamic user clarifications.
  3. Long-term memory for personalization (Optional).

---

## **Submission Form**

Submit your projects here:  
[**Project Submission Form**](https://forms.gle/yB6X4TzE2dCVThCj8)

---

### **Example Scenarios:**

1. **Human Assistant Interrupt:**
   - User asks: *"Can you help with tax calculations?"*
   - Chatbot: *"Let me connect you to a human assistant for this question."*
   
2. **Dynamic Interrupt:**
   - User asks: *"Plan a study schedule for me."*
   - Chatbot: *"What is your next exam date? Should I include break times?"*

3. **Personalized Memory (Optional):**
   - User: *"What should I study today?"*
   - Chatbot: *"Last time, you said your math exam is next week. Let’s focus on trigonometry today."*

---

### **Outcomes:**
By completing this project, you will:
1. Learn how to connect a chatbot with a human assistant.
2. Understand how to make chatbots pause and ask for clarifications when needed.
3. Use long-term memory to personalize chatbot responses.