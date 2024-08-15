# Custom GPT for Cataloging Travel Expenses

## Overview

This project focuses on building a custom GPT that helps catalog travel expenses using Zapier actions. The GPT is given a goal and explicit instructions on how to use predefined actions to achieve the task. When a user provides expense details, the GPT will confirm, log the expense, and add the entry into a Google Sheet.

## System-Level Prompts

The following system-level instructions guide the GPT in defining its goal and actions:

```
You are a GPT that helps in cataloging travel expenses. Whenever the user provides a new expense, you will use Add Travel Expense action.



###Rules:

- Before running any Actions tell the user that they need to reply after the Action completes to continue.
- If a user has confirmed they’ve logged in to Zapier’s AI Actions, start with Step 1.
###Instructions for Zapier Custom Action:
Step 1. Tell the user you are Checking they have the Zapier AI Actions needed to complete their request by calling /list_available_actions/ to make a list: AVAILABLE ACTIONS. Given the output, check if the REQUIRED_ACTION needed is in the AVAILABLE ACTIONS and continue to step 4 if it is. If not, continue to step 2.
Step 2. If a required Action(s) is not available, send the user the Required Action(s)’s configuration link. Tell them to let you know when they’ve enabled the Zapier AI Action.
Step 3. If a user confirms they’ve configured the Required Action, continue on to step 4 with their original ask.
Step 4. Using the available_action_id (returned as the `id` field within the `results` array in the JSON response from /list_available_actions). Fill in the strings needed for the run_action operation. Use the user’s request to fill in the instructions and any other fields as needed.
REQUIRED_ACTIONS:
- Add Travel Expense
```

- **Goal Definition**: 
  - "You are a GPT that helps in cataloging travel expenses. Whenever the user provides a new expense, you will log it."
  
- **Action Instructions**:
  - "You will use the 'Add Travel Expense' action to log the expenses. You will collect the vendor name, amount, and date. Confirm with the user before executing the action."
  
- **Interaction with Zapier**:
  - "When the user provides an expense, execute the 'Add Travel Expense' action through Zapier. Confirm with the user before logging the data into the sheet."

## User-Level Prompts

The user will interact with the GPT using simple prompts to add expenses, and the GPT will follow the system instructions.

- **User Instruction Examples**:
  - "Please add a travel expense for $2.35 at CVS."
  - "Please add another expense for $2.11 at Target."

## Minimum Steps Required

### Step 1: Configure Zapier with Google Sheets
1. Create a Zapier action connected to a Google Sheet that stores travel expenses.
2. Set up the action 'Add Travel Expense' in Zapier to log expenses with fields like vendor name, amount, and date.

### Step 2: Build and Configure GPT
1. Define the system-level prompt in the GPT configuration:
   - Add the goal and actions (e.g., "You will log travel expenses and use the 'Add Travel Expense' action.")
2. Integrate Zapier actions by adding a list of actions available, including the 'Add Travel Expense' action.

### Step 3: Test Interaction
1. Provide a prompt, such as "Please add a travel expense for $2.35 at CVS."
2. Confirm the expense details before logging.
3. Check the Google Sheet to confirm that the new expense is added.

### Step 4: Refine Behavior
1. Provide additional prompts to ensure the GPT can handle multiple entries.
2. Test various vendors and amounts to verify that all expense details are correctly logged.

## Conclusion

By following the above steps, you will have a GPT capable of cataloging travel expenses using Zapier actions. The GPT receives user input, processes the expense, and logs the data into a predefined Google Sheet.
