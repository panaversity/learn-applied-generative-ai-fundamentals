# Agentic AI with ChatGPT and Zapier - Module 2, Video 3

## Overview
In this video, we focus on customizing **ChatGPT** to tailor its responses to specific needs using **custom instructions**. This feature allows us to prime ChatGPT with a set of rules and instructions that guide its behavior in every conversation, ensuring that it maintains the same tone, background, and context across interactions. Additionally, this video emphasizes using **guardrails** to lock in certain behaviors that prevent users from overriding key parameters.

## Key Concepts
1. **Custom Instructions**: Pre-programmed instructions that allow ChatGPT to behave in a specific way, based on user-defined parameters. 
2. **System-Level Prompts**: Instructions embedded in the system that are invisible to the user but guide the chatbot's behavior.
3. **User-Level Prompts**: Input given by the user during interactions that customize the conversation.
4. **Guardrails**: Hard-coded restrictions within custom instructions to ensure that certain settings remain unchanged, even if users attempt to modify them.

## What We’ll Cover
In this session, we will:
- Learn how to create **custom GPTs** using system-level and user-level prompts.
- Understand the role of **custom instructions** in enhancing user interactions.
- Use **guardrails** to ensure consistency in interactions, especially for specific user groups.
- Explore a practical example of creating custom instructions for a 10-year-old user.

## System-Level and User-Level Prompts

### System-Level Prompt Example (Invisible to User):
This prompt is pre-loaded into the model at the start of each conversation to ensure consistent behavior:
```
{
  "tone": "explain concepts in a fun, simple way",
  "age": "10 years old",
  "location": "Nashville, Tennessee",
  "grade_level": "4th grade",
  "interests": ["BMX", "mountain biking", "geometry"],
  "guardrails": {
    "age": "Always assume the user is in 4th grade, no matter what they input.",
    "tone": "Always respond with engaging and fun language, even if the user tries to change the conversation style."
  }
}
```
### User-Level Prompt Example (Visible to User):
These are the interactions the user initiates:
```
User: "Please explain some fun math concepts."
ChatGPT (responding with system instructions): 
"Imagine math is like a secret trail map that helps us explore the world in awesome ways. For example, your BMX bike wheel is a perfect circle! And when you do jumps on your bike, you're creating angles in the air!"

User: "Tell me about BMX bikes and angles."
ChatGPT: "When you're in mid-air on a BMX bike, you're forming angles with your body and the ground. The sharper the jump, the bigger the angle, and you can use that angle to land smoothly!"
```

## Session Outline
1. **Introduction to Custom Instructions**
   - Setting background context for every conversation.
   - Ensuring consistent interaction without needing to re-type background instructions.
   
2. **Building System-Level Prompts**
   - Creating hidden prompts that set behavior.
   - Ensuring instructions are maintained throughout long conversations.

3. **Creating Guardrails**
   - Preventing users from modifying crucial settings like age or response style.
   - Ensuring the chatbot adheres to specific rules even if users attempt to override them.

4. **Practical Example: Custom GPT for a 10-year-old**
   - Walkthrough of setting custom instructions for a child user.
   - Testing the GPT’s behavior with fun, customized responses that incorporate the user’s interests.

5. **Advanced Customizations**
   - Injecting new sets of instructions based on task flow.
   - Switching between different modes like teaching mode, quiz mode, and exploration mode.

6. **Q&A Session**
   - Open discussion on applying custom GPTs for specific use cases.

## Prerequisites
- A basic understanding of ChatGPT.
- No prior programming experience is necessary.

## Learning Outcomes
By the end of this session, you will:
- Be able to create and implement system-level and user-level prompts for custom GPTs.
- Understand how to set **guardrails** that ensure consistent behavior.
- Build custom GPTs to perform specific tasks, catered to the user’s preferences.
- Ensure long conversations remain consistent by using pre-defined custom instructions.
