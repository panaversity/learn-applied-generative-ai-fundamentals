# README.md - Video-03: Building a Custom GPT for Travel Expense Reporting with Zapier Integration

## Overview

In this video, we walk through the process of building a custom GPT to assist with travel expenses using agentic AI concepts. This custom GPT will allow users to automate the tracking and reporting of their travel expenses through voice input or receipt images. We will connect the GPT to Zapier to automate various actions, such as adding expenses to Google Sheets, identifying missed expenses, and crafting formatted emails for expense reimbursement submission.

## System-Level Prompts

- **Expense Logging**: The system should log all expenses received via speech or image input and store them in the Google Sheets. 
  - _System prompt_: "Track and log all travel expenses for the user, ensuring all necessary details such as amount, category (e.g., meals, transportation), and receipt (if provided) are recorded in the Google Sheet."

- **Receipt Processing**: The system should extract relevant information from uploaded receipts using OCR and add it to the log.
  - _System prompt_: "Extract key information (amount, date, category) from uploaded receipt images using OCR and log this data in the Google Sheet."

- **Error Detection**: The system should prompt the user if there is any potential missing data, such as a meal or transportation expense that could have been forgotten during a trip.
  - _System prompt_: "Analyze the expense log and identify common missing items such as meals or transportation based on the user's trip data. Prompt the user to fill in any gaps."

- **Email Generation**: The system should generate a formatted expense report email, summarizing all logged expenses, including attached receipts if needed, and ready to be submitted.
  - _System prompt_: "Generate a summary email for the user with all logged expenses, formatted in a professional report style, ready to be sent for reimbursement."

## User-Level Prompts

- **Adding an Expense**:
  - _User prompt_: "I spent $15 on breakfast at a cafe. Log it as a meal expense."
  - _User prompt_: "Add a $50 Uber ride from the hotel to the airport."

- **Uploading a Receipt**:
  - _User prompt_: "Here’s a photo of my lunch receipt. Please add it to my expense report."

- **Reviewing Missing Expenses**:
  - _User prompt_: "Did I forget to log any meals during my trip?"

- **Generating an Expense Report Email**:
  - _User prompt_: "Create an expense report email with all the logged expenses for my recent trip and include the receipts."

## Minimum Steps for Custom GPT Creation

1. **Set Up a Google Sheet for Expense Logging**:
   - Create a Google Sheet with columns for `Date`, `Category`, `Amount`, `Details`, and `Receipt`.

2. **Connect GPT to Google Sheets Using Zapier**:
   - Set up a Zap that triggers when the GPT receives an expense input and logs it into the Google Sheet.
   - Create another Zap to process uploaded receipts using OCR, extract the necessary details, and add them to the Google Sheet.

3. **Implement GPT Prompts for Expense Tracking**:
   - Design system-level prompts to handle various user inputs, such as logging expenses, identifying missed expenses, and generating emails.

4. **Receipt Processing via OCR**:
   - Use an OCR tool (e.g., Google Vision API or Zapier OCR) to extract details from receipt images and log them automatically.

5. **Generate and Send an Expense Report**:
   - Allow the GPT to craft a summary email with all the expenses logged and format it properly with any attached receipts.
 