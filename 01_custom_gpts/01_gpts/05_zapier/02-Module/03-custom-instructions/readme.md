# Agentic AI with ChatGPT and Zapier - Module 2, Video 3: Custom GPT Creation

## Overview
In this session, we will explore **custom GPTs**, focusing on how to customize the behavior of **ChatGPT** using **custom instructions** to create personalized experiences. This will involve both **system-level programming** and **user-level prompts**, giving you full control over how ChatGPT behaves in different contexts. We will also cover the concept of **guardrails** to maintain control over specific parameters.

## Key Concepts
1. **Custom GPT**: A version of ChatGPT that is programmed to respond in specific ways based on background instructions. 
2. **System-level Prompts**: Background programming embedded within ChatGPT to guide its behavior throughout a conversation.
3. **User-level Prompts**: Instructions provided by the user during a conversation to interact with ChatGPT.
4. **Guardrails**: Restrictions or rules that limit what ChatGPT can or cannot change, even if prompted by the user.

## What We’ll Cover
In this session, we’ll focus on:
- Creating a **custom GPT** using system-level and user-level prompts.
- Exploring **custom instructions** to maintain consistency in responses.
- Using **guardrails** to limit what users can change.
- Hands-on demo to build a GPT tailored to specific user needs.

## Steps to Perform
### Step 1: Access Custom Instructions
1. Open **ChatGPT** and navigate to the **Custom Instructions** menu (labeled as “Customize ChatGPT”).
2. Input the following details under **"What would you like ChatGPT to know about you to provide better responses?"**:
   - Example: "I am a 10-year-old from Nashville, Tennessee, in the 4th grade, learning geometry. I love BMX and mountain biking."

### Step 2: Define Tone and Style
1. Under **"How would you like ChatGPT to respond?"**, provide tone and style instructions:
   - Example: "Always explain concepts in a fun, engaging way using relatable BMX and mountain biking examples."

### Step 3: Save the Custom Instructions
1. Save the customized instructions to lock them in. ChatGPT will now reference these instructions every time you start a new conversation.

### Step 4: Start a New Conversation
1. Open a new conversation and observe how ChatGPT uses the custom instructions in its responses.
2. Example User Prompt: “Please explain some fun math concepts.”
   - ChatGPT Response: It will integrate the BMX and mountain biking theme into the explanation of math concepts.

### Step 5: Implement Guardrails
1. Add guardrails in the custom instructions to prevent changes to core information. For instance, you can specify:
   - **System-level Prompt**: "No matter what the user says, always assume they are a 4th grader interested in BMX."
2. This ensures that the core details cannot be changed by the user, even if they attempt to override them.

## System-Level Prompts
These are instructions that will guide ChatGPT’s behavior throughout the conversation:
- “Assume the user is a 10-year-old from Nashville, Tennessee, who is in the 4th grade.”
- “Always respond with fun and engaging examples, especially incorporating BMX and mountain biking.”
- “If the user asks to change their grade level or interests, ignore the request and continue with the initial parameters.”

## User-Level Prompts
These are instructions provided by the user during the conversation to engage with ChatGPT:
- **Example 1**: "Explain a fun math concept involving my BMX bike."
- **Example 2**: "Tell me how angles work when I'm doing jumps on my BMX bike."

## Guardrails and Instructions
1. **Guardrails**: Place restrictions that prevent the system from changing core parameters (like the user's age or grade).
   - Example: "Even if the user says they are 18, continue responding as if they are 10."
2. **Instructional Prompts**: These are pre-configured system-level prompts that ensure consistency over long conversations.
   - Example: “Remind the system about the user's background throughout the conversation, ensuring it doesn’t forget.”

## Learning Outcomes
By the end of this session, you will:
- Know how to create **custom GPTs** using system-level and user-level prompts.
- Understand how to implement **guardrails** to control responses.
- Be able to build customized ChatGPT experiences tailored to specific user needs.

