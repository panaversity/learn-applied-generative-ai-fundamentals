# creating-the-zapier-action-tool-for-our-agent

This project demonstrates how to create a custom GPT that can perform actions using Zapier. Specifically, this GPT will be used as a travel helper, automating the process of adding travel expenses and other tasks by interacting with various applications through Zapier.

## System-Level Prompts

These prompts define the GPT's capabilities and allow it to invoke actions in Zapier.

```plaintext
You are a travel helper GPT designed to assist users in logging travel expenses and automating various tasks using Zapier actions. Your primary function is to interact with the Zapier API, invoke actions, and provide a seamless user experience for task automation. You have access to the following actions: 
- Add travel expense 
- Send a receipt
- Update expense report in Google Sheets

Always follow the user's input and translate their commands into the corresponding actions on Zapier.
```

## User-Level Prompts

These are examples of prompts the user can input to interact with the GPT and utilize Zapier actions.

```plaintext
- "Add a new travel expense for $150 on August 12, 2024, to my Google Sheets expense tracker."
- "Send a receipt for the flight booked on August 10th to my email."
- "Update the total in my expense report for July."
```

## Minimum Steps to Create Custom GPT with Zapier Actions

1. **Create a New GPT:**
   - Go to OpenAI's platform and create a new GPT.
   - Name it appropriately, e.g., "Travel Helper."

2. **Define Actions:**
   - Navigate to the **Actions** section in the GPT settings.
   - Click **Create new action**.
   - In the schema menu, define the actions you want the GPT to perform, such as `Add travel expense`, `Send receipt`, etc.
   
3. **Import Zapier Actions Schema:**
   - Copy the URL to the Zapier Actions API documentation: `actions.zapier.com/docs/platform/gpt`.
   - Import this into the GPT by selecting **Import from URL**. This will give the GPT access to predefined Zapier actions.

4. **Define System and User-Level Prompts:**
   - Add system-level instructions that define the purpose and available actions of the GPT.
   - Provide sample user-level prompts so the user knows how to interact with the GPT.

5. **Test the GPT:**
   - Try some user-level prompts to ensure the GPT correctly invokes the Zapier actions.

6. **Deploy and Refine:**
   - Once tested, deploy the GPT and refine it as needed by adding more actions or improving the user interaction flow.

