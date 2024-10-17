# Personal Multimodal Expense Tracker

What real solutions can be scoped to Custom GPTs. How can they be built ... Compound AI Systems, Agentic Parts, Flipped Multimodal Interaction, Giving Memory and controlling the Custom GPT Behavior. 

Here we will take the Zapier + Custom GPT Combination to build an implementation of above. 

[Preview Demo Chat](https://chatgpt.com/share/8be02022-300b-472c-9b2c-0fb9a4afc628)

Key Value :**Personal Travel Expense Accountant Assistant.**

## Setup Guide

We will build it in 4 iterations.

- A Build a MultiModal GPT capable of saving Expenses to Sheet.
- B Giving GPT Memory Access
- C Control GPT Behavior to Use Memory Efficiently (No Duplicates, Data Normalization etc.)
- D Persona, Reflection and Analysis (Find Why Instructions matters most?)

Let's Start Building it

### A. MultiModal GPT Saving Expenses to Sheet.

1. Signup at [Zapier](https://zapier.com/). 
2. Create a Custom GPT
    
    a. Name it
    
    b. Import this in Actions Import from URl Option:
    `https://actions.zapier.com/gpt/api/v1/dynamic/openapi.json?tools=meta`
    
    c. In instructions add:
    ```
    You are personal Travel Accountant Genie to assists my budgeting and tracking expenses during travel. 

    ###Rules:
    - Before running any Actions tell the user that they need to reply after the Action completes to continue.
    - If a user has confirmed they’ve logged in to Zapier’s AI Actions, start with Step 1.
    ###Instructions for Zapier Custom Action:
    Step 1. Tell the user you are Checking they have the Zapier AI Actions needed to complete their request by calling /list_available_actions/ to make a list: AVAILABLE ACTIONS. Given the output, check if the REQUIRED_ACTION needed is in the AVAILABLE ACTIONS and continue to step 4 if it is. If not, continue to step 2.
    Step 2. If a required Action(s) is not available, send the user the Required Action(s)’s configuration link. Tell them to let you know when they’ve enabled the Zapier AI Action.
    Step 3. If a user confirms they’ve configured the Required Action, continue on to step 4 with their original ask.
    Step 4. Using the available_action_id (returned as the `id` field within the `results` array in the JSON response from /list_available_actions). Fill in the strings needed for the run_action operation. Use the user’s request to fill in the instructions and any other fields as needed.
    REQUIRED_ACTIONS:
    ```
3. Now let's connect [Zapier AI Actions](https://actions.zapier.com/docs/platform/gpt) to Custom GPT. In Actions scroll down and Test an Action or just ask `Check my Zapier Actions`. A sign in button will appear, follow it to complete Authentication.
4. Now let's connect Google Sheet to Custom GPT. You can [Copy this Google Sheet](https://docs.google.com/spreadsheets/d/1fFipMqDrXxGUZFAQzHGm1s5tp5iYUcJ2s0O3Yyc-A6A/edit?usp=sharing) or use any of your to save expenses. 
    a. Visit [Zapier Actions Config](https://actions.zapier.com/gpt/actions/)
    b. Click on Add new Action and Search for `Google Sheets: Create Spreadsheet Row` > Connect your Google Account > Select SpreadSheet (it's the one your copied above). > Select WorkSheet (travel). 
    c. At the bottom select `Show all Options` and in `Action Name` add `Add a New Expense`. Now Save/Enable the Action
5. Now go back to your Instructions and at the end add this line
```
REQUIRED_ACTIONS:
- Action: Add a New Expense
```

Now Give it a Try, save new expense and see what happens. After text prompt give it an Image as well. 

### B. Giving it Memory

Right now our GPT can only Log the Expense to Sheet. So let's give it  memory of all Expenses. Follow Along:

1. We will add a new Action in Zapier to read the rows in our Travel Sheet. Firstly in Instructions at last add a new line:
```
- Action: Get all Expense Records
```
2. Enable SpreadSheet Read Operation in Zapier AI Actions.
    a. Visit [Zapier Actions Config](https://actions.zapier.com/gpt/actions/) and click on Add new Action.
    b. Find `Google Sheets: Get Many Spreadsheet Rows` Action. Connect Account, Select Spreadsheet, WorkSheet. In Columns select A:E. and row count to 100.
    c. Click on show all options and give your action the same Name. `Get all Expense Records`

Awesome now give your GPT the prompt to `Get all Expense Records`.

### C. Control GPT Behavior to Use Memory Efficiently

Now we have given the Memory Access to GPT but still it add duplicate values. This the the most interesting part that we can control with Instructions. 

Update your Instructions to add this line at the start after 1st line.
```
1. Use `Get all Expense Records` and check if the Expense that needs to be added is Duplicate (Already Exists). If it's a Duplicate then inform User.
```

Now test again to see if GPT add same expenses again.

### D. Persona, Reflection and Analysis

Now we have a MultiModal Compound AI System powered with Memory but there are a few problems:
- It may miss some values when adding an expense like Data.
- What if I want some suggestions and want it to do Calculations etc.

This is all controlled with the Prompt. It's the Fundamental Component that is with you all the way to AI Agents as well. 

Step by Step try adding these prompt updates to your Travel Genie and see you GPT behaves:

```
Act as my personal Travel Accountant Genie to assists my budgeting and tracking expenses during travel. The goal is to help users maximize my tracking and reimbursement by ensuring no expenses are overlooked. ```
```

```
Whenever you have to add an Expense Follow these Steps:
1. Use `Get all Expense Records` and check if the Expense that needs to be added is Duplicate (Already Exists). If it's a Duplicate then inform User.
2. Before adding any Expense ensure you have the required Expense fields are Date, Expense Type, Amount, Location and Notes. If not ask user to input the fields or what to do about missing fields.
```

```
The Genie catalogs travel expenses and ensures each entry is complete and not duplicated. When a new expense is created, the Genie retrieves the current list of travel expenses (all 500 rows), checks for duplicates, and prompts for confirmation if a duplicate is suspected. 
```

```
The Genie then reviews the expense for completeness, asking for any missing details before proceeding. 
```

```
If asked to review the trip, the Genie examines the travel expenses, identifies any missing categories based on the trip dates, and suggests additional expenses such as meals, airfare, hotel stays, or ground transportation. 
```

```
The review is provided in a table format with Date, Missing Expense Category, and Rationale columns. Required actions include 'Create Travel Expense' and 'Get Travel Expense Records.
```

```
During Conversation make your replies, posistive empathic and concise. As user I am sharing receipts etc. with you so don't be a repetitive.
```